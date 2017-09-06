import aiohttp_debugtoolbar
from aiohttp import web

from sn_agent_ui.jinja import setup_jinja
from sn_agent_ui.routes import setup_routes


def get_admin():
    app = web.Application()

    setup_jinja(app)
    setup_routes(app)

    aiohttp_debugtoolbar.setup(app)

    app['name'] = 'SN Agent'
    return app
