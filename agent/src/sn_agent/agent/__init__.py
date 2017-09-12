from jinja2.utils import import_string

from sn_agent.agent.settings import AgentSettings


def setup_agent(app):
    settings = AgentSettings()
    agent_id = settings.ID
    klass = import_string(settings.CLASS)
    app['agent'] = klass(app, agent_id)
