from jinja2.utils import import_string

from sn_agent.network.settings import NetworkSettings


def setup_network(app):
    settings = NetworkSettings()
    klass = import_string(settings.CLASS)
    app['network'] = klass(app)
