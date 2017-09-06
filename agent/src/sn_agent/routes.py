from pathlib import Path

from sn_agent import api

THIS_DIR = Path(__file__).parent
BASE_DIR = THIS_DIR.parent


def setup_routes(app):
    app.router.add_post('/api', api.handler)
