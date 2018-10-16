import time
import asyncio as a
from enum import Enum

from aiohttp import web, WSMsgType
from typing import NamedTuple, Any

import logging


class ChatSocketMessageType(Enum):
    PLAINTEXT = 'PLAINTEXT'
    UNKNOWN = 'UNKNOWN'


class ChatSocketMessage(NamedTuple):
    message_type: ChatSocketMessageType
    payload: Any = None


def uri_of(route):
    """
    returns uri for given sub-route
    """
    return route


routes = web.RouteTableDef()


def not_implemented(message):
    return web.json_response(status=501, data={'error_message': message})


class PushSubscription(object):
    def __init__(self):
        pass

    def __aiter__(self):
        return self

    async def __anext__(self):
        await a.sleep(1)
        return 'hello!'


@routes.view('/subscribe/')
class MessageSubscribeView(web.View):
    def __init__(self, request):
        super().__init__(request)
        self.app = self.request.app

    @property
    def user(self):
        if not hasattr(self, '_user'):
            self._user = self.request.query.get('user', '')
        return self._user

    async def message_push_reader(self, ws):
        from .subscriptions import Subscription
        pub = self.app.message_publisher
        with Subscription(pub) as queue:
            while not ws.closed:
                msg = await queue.get()
                if msg['user'] == self.user:
                    await ws.send_json({'message': msg['message']})
                else:
                    print(f"{msg['user']} is not {self.user}")

    async def client_messages(self, ws):
        async for msg in ws:

            if msg.type == WSMsgType.ERROR:
                print('connection closed with exception {}'.format(
                    ws.exception()))
            elif msg.type == WSMsgType.TEXT:

                await ws.send_json({
                    'message':
                    f'hello, {self.user}, {msg.data}'
                })

            elif msg.type == WSMsgType.CLOSE:
                await ws.close()

    async def get(self):
        ws = web.WebSocketResponse()
        await ws.prepare(self.request)

        await a.gather(self.message_push_reader(ws), self.client_messages(ws))

        return ws


@routes.get('/publish/')
async def push_message(request):
    pub = request.app.message_publisher
    user = request.query.get('user', None)
    msg = request.query.get('msg', '')
    if not user:
        return web.json_response(
            status=400,
            data={
                'err': 'Bad Request',
                'reason': "no 'user' parameter"
            })

    pub.publish({'user': user, 'message': msg})

    return web.json_response({'res': 'ok'})


@routes.get('/')
def index_view(request):
    return web.json_response({'links': [r.path for r in routes]})
