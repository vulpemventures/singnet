
from sn_agent.service_adapter.base import ServiceAdapterBase


class OpenCogServiceAdapter(ServiceAdapterBase):
    type_name = "OpenCog"

    def __init__(self, app, ontology_node_id, required_ontology_node_ids, host, port):
        super().__init__(app, ontology_node_id, required_ontology_node_ids)
        self.host = host
        self.port = port

    def perform(self, *args, **kwargs):
        pass
