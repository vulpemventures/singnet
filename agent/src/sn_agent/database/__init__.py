from aiohttp import web
from sqlalchemy import create_engine

from sn_agent.database.settings import DatabaseSettings


async def startup(app: web.Application):
    settings = DatabaseSettings()
    db_url = settings.URL
    app['db_engine'] = create_engine(db_url)


def setup_db(app):
    app.on_startup.append(startup)
