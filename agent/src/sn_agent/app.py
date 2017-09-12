import asyncio
import logging

import uvloop
from aiohttp import web

import sn_agent_ui
from sn_agent.agent import setup_agent
from sn_agent.log import setup_logging
from sn_agent.network import setup_network
from sn_agent.ontology import setup_ontology
from sn_agent.routes import setup_routes
from sn_agent.service_adapter import setup_service_manager

logger = logging.getLogger(__file__)


def create_app():
    # Significant performance improvement: https://github.com/MagicStack/uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    app = web.Application()
    setup_logging()
    setup_routes(app)

    setup_ontology(app)
    setup_network(app)
    setup_service_manager(app)
    setup_agent(app)

    app['name'] = 'SingularityNET Agent'

    # Leave this off until it is working
    if False:
        admin = sn_agent_ui.get_admin()
        app.add_subapp('/admin/', admin)

    return app
