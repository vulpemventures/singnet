from sn_agent.ontology.service_descriptor import ServiceDescriptor


class Provider:
    def __init__(self, net, agent_id, service: ServiceDescriptor):
        self.net = net
        self.agent_id = agent_id
        self.service = service

    def can_perform(self):
        return self.net.ask_agent_if_can_perform(self.agent_id, self.service)
