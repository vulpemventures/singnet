from sn_agent.worker.base import WorkerBase


class ServiceWorker(WorkerBase):
    type_name = "Service"

    def __init__(self, app, ontology_node_id, required_ontology_node_ids, name):
        super().__init__(app, ontology_node_id, required_ontology_node_ids)
        self.name = name

    def perform(self, *args, **kwargs):
        pass
