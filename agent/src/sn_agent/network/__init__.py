
from sn_agent.network.settings import NetworkSettings
from sn_agent.utils import import_string


def setup_network(app):
    settings = NetworkSettings()
    klass = import_string(settings.CLASS)
    app['network'] = klass(app)
