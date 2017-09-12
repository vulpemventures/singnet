import logging

from sn_agent.ontology.base import OntologyABC

logger = logging.getLogger(__name__)


class TestOntology(OntologyABC):
    def __init__(self, app):
        super().__init__(app)
        logger.debug('Test Ontology Started')

    def get_service_description(self, node_id) -> str:
        pass
