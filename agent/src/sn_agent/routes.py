from pathlib import Path

from sn_agent.views import index, stats, jobs, api

THIS_DIR = Path(__file__).parent
BASE_DIR = THIS_DIR.parent


def setup_routes(app):
    app.router.add_get('/', index.index, name='index')
    app.router.add_get('/stats', stats.index, name='stats')
    app.router.add_route('*', '/jobs', jobs.index, name='jobs')
    app.router.add_route('*', '/network', jobs.index, name='network')
    app.router.add_post('/api', api.handler)

    app.router.add_static('/static/', path=str(THIS_DIR / 'static'), name='static')
