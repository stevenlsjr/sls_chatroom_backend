import aiohttp
from aiohttp import web
import pytest
import asyncio

@pytest.fixture
def app_client(loop: asyncio.AbstractEventLoop, aiohttp_client):
    from .app import app
    return loop.run_until_complete(aiohttp_client(app))


async def test_index_view(app_client: aiohttp.ClientSession):
    resp = await app_client.get('/')
    assert resp.status == 200
    js = await resp.json()
    assert 'links' in js