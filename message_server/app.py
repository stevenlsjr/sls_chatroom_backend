import time
import asyncio as a
from aiohttp import web
from .views import routes

from .subscriptions import SubscriptionPublisher

app = web.Application()
app.message_publisher = SubscriptionPublisher()
app.add_routes(routes)



