from jinja2.utils import import_string

from sn_agent.network.settings import NetworkSettings


def setup_network(app):
    settings = NetworkSettings()
    network_klass = import_string(settings.NETWORK_CLASS)
    app['network'] = network_klass(app)
