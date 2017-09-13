import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class ServiceAdapterABC(ABC):
    """
    This is the service adapter base, all other service adapters are based on it.
    """

    type_name = "Base"

    def __init__(self, app, ontology_node_id, required_ontology_node_ids) -> None:
        self.app = app
        self.ontology_node_id = ontology_node_id
        self.required_ontology_node_ids = required_ontology_node_ids
        self.requirements_met = False
        self.available = False

    def init(self):
        """
        This will hunt out all the agents required to fulfill the required ontology ids

        We should periodically call this if it is false - an agent might come alive that can support this
        :return:
        """

        self.requirements_met = self.has_all_requirements()

        logger.info('Service Adapter: %s initialized. Requirements met: %s', self.type_name, self.requirements_met)

    def has_all_requirements(self):
        """
        if self.required_ontology_node_ids is None:
            return True
        network = self.app['network']
        for required_ontology_node_id in self.required_ontology_node_ids:
            providers = network.find_providers(required_ontology_node_id)

            if len(providers) == 0:
                return False
        """
        return True

    def start(self):
        """
        If init sets up all the connections, start is here to ensure that the worker is actually alive and can process
        :return:
        """
        self.available = True

    def stop(self):
        """
        This will take the worker offline but does not need to be re-initialized
        :return:
        """
        self.available = False

    def can_perform(self) -> bool:
        """
        This is a boolean flag indicating if this worker can do whatever work it says it can.

        An answer of no can be because it is offline, or perhaps it is too busy.
        :return:
        """
        return self.requirements_met and self.available

    def all_required_agents_can_perform(self):

        if self.required_ontology_node_ids is None:
            return True

        network = self.app['network']
        for required_ontology_node_id in self.required_ontology_node_ids:
            providers = network.find_providers(required_ontology_node_id)

            if len(providers) == 0:
                return False
            else:
                # Grab the first one
                # TODO: this should be made smarter
                if providers[0].can_perform():
                    continue

        return True

    @abstractmethod
    def perform(self, *args, **kwargs):
        """
        This is where the work gets done, the worker will block here until the work itself is done
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError()
