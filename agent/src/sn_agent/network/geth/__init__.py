from sn_agent.network.base import NetworkBase
from sn_agent.network.geth.poller import setup_poller


class GethNetwork(NetworkBase):


    def __init__(self, app):
        super().__init__(app)
        setup_poller(app)

    def join(self) -> bool:
        """
        Agent calls this the first time to connect to the network. An Private and Public key should be returned
        """
        raise NotImplementedError()

    def leave(self) -> bool:
        """
        Should this do something in the blockchain or just delete the public and private keys?
        """
        raise NotImplementedError()

    def status(self) -> bool:
        """
        Determine what the current network status is (joined or not joined)
        :return:
        """
        raise NotImplementedError()

    def get_ontology(self):
        """
        Asks for the latest ontology from wherever it is stored.
        :return:
        """
        raise NotImplementedError()

    def advertise(self, agent_id: str, ontology_node_id) -> bool:
        """
        Given an ontology, advertise it as a service that the agent provides
        :param agent_id:
        :param ontology_node_id:
        :return:
        """
        raise NotImplementedError()

    def deadvertise(self, agent_id: str, ontology_node_id) -> bool:
        """
        Remove the advertisement of the service for a given agent
        :param agent_id:
        :param ontology_node_id:
        :return:
        """
        raise NotImplementedError()

    def find_providers(self, ontology_node_id) -> list:
        """
        Called by the UI as well as find_provider - should return a list that contains information about all the providers that have indicated that they can proved the designated service
        :param ontology_node_id:
        :return:
        """
        raise NotImplementedError()

    def ask_agent_if_can_perform(self, agent_id, ontology_node_id) -> bool:
        """
        :param agent_id:
        :param ontology_node_id:
        :return:
        """
        raise NotImplementedError()

    def ask_agent_to_perform(self, agent_id, ontology_id, json_content) -> bool:
        """

        :return:
        """
        raise NotImplementedError()

    def ask_agent_for_their_providers(self, agent_id, ontology_node_id) -> list:
        """
        This is used for creating the tree of services behind a given ontology

        :param agent_id:
        :param ontology_node_id:
        :return:
        """
        raise NotImplementedError()

    def can_i_perform(self, ontology_node_id) -> bool:
        """
        This is a request coming from the network asking if I can actually do the service

        :param ontology_node_id:
        :return:
        """

    def perform(self, ontology_node_id, json_content) -> bool:
        """
        This will instruct the worker to do the task requested

        :param ontology_node_id:
        :param json_content:
        :return:
        """
