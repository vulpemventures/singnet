from aiohttp import web
from jsonrpcserver.aio import methods


@methods.add
async def ping():
    return 'pong'


@methods.add
async def disable_service(service_descriptor):
    return 'pong'


async def handler(request):
    request = await request.text()
    response = await methods.dispatch(request)
    if response.is_notification:
        return web.Response()
    else:
        return web.json_response(response, status=response.http_status)
