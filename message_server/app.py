import time
import asyncio as a

from aiohttp import web, WSMsgType

routes = web.RouteTableDef()


@routes.get('/')
async def handle(request):
    return web.json_response(data=["Hello world!!!"])

        
@routes.post('/message/')
async def message_posted(request):
    msg = 'no message'
    web.json_response()



@routes.get('/ws')
async def socket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    

    print(f'socket {ws} closing')
    return ws

app = web.Application()
app.add_routes(routes)



