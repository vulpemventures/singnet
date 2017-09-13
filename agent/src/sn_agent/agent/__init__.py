
from sn_agent.agent.settings import AgentSettings
from sn_agent.utils import import_string


def setup_agent(app):
    settings = AgentSettings()
    agent_id = settings.ID
    klass = import_string(settings.CLASS)
    app['agent'] = klass(app, agent_id)
