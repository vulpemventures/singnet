from sn_agent import api


def setup_routes(app):
    app.router.add_post('/api', api.handler)
