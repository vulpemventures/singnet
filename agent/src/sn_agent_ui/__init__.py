import aiohttp_debugtoolbar
from aiohttp import web

from sn_agent_ui.jinja import setup_jinja
from sn_agent_ui.middleware import setup_middleware
from sn_agent_ui.routes import setup_routes
from sn_agent_ui.session import setup_session


def get_admin():
    app = web.Application()

    setup_session(app)
    setup_middleware(app)
    setup_jinja(app)
    setup_routes(app)

    aiohttp_debugtoolbar.setup(app)

    app['name'] = 'SN Agent'
    return app
