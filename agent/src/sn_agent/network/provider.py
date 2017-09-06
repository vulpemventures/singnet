class Provider:
    def __init__(self, net, agent_id, ontology_node_id):
        self.net = net
        self.agent_id = agent_id
        self.ontology_node_id = ontology_node_id

    def can_perform(self):
        return self.net.ask_agent_if_can_perform(self.agent_id, self.ontology_node_id)
