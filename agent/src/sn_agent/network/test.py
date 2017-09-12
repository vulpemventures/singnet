from sn_agent.network.base import NetworkBase
from sn_agent.network.enum import NetworkStatus
from sn_agent.agent.base import AgentBase
from sn_agent.ontology.ontology import Ontology
from sn_agent.ontology.service import Service
from sn_agent.network.provider import Provider

from sn_agent.network.settings import NetworkSettings

class TestNetwork(NetworkBase):
    def __init__(self, app, agent : AgentBase):
        super().__init__(app, agent)

    def join_network(self) -> bool:
        """
        Agent calls this the first time to connect to the network. An Private and Public key
        should be returned
        """
        pass

    def leave_network(self) -> bool:
        """
        Should this do something in the blockchain or just delete the public and private keys?
        """
        pass


    def logon_network(self) -> bool:
        """
        Agent calls this to logon to the network prior to calling network operations
        """
        pass

    def logoff_network(self) -> bool:
        """
        Agent calls this to loff off the network after calling network operations
        """
        pass

    def get_network_status(self) -> NetworkStatus:
        """
        Determine what the current network status is (joined or not joined)
        """
        return STATUS_NON_MEMBER

    def am_i_a_member(self) -> NetworkStatus:
        """
        Determine what the current network status is (joined or not joined)
        """
        return self.get_network_status() == STATUS_MEMBER

    def update_ontology(self):
        """
        Updates self.ontology from the blockchain with any changes since the last
        time update was called.
        """
        pass

    def advertise_service(self, service: Service):
        """
        Given an ontology, advertise it as a service that the agent provides
        :param service: a service objects defining a service spec
        """
        pass

    def remove_service_advertisement(self, service: Service):
        """
        Remove the advertisement of the service for a given agent
        :param service:
        """
        pass

    def find_service_providers(self, service: Service) -> list:
        """
        Called by the UI as well as find_provider - should return a list that contains
        information about all the providers that have indicated that they can proved
        the designated service.
        :param ontology_node_id:
        :return: a list of external agents which provide the service requested
        """
        pass
