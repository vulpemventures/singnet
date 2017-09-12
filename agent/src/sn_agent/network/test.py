import logging

from sn_agent.network.base import NetworkABC
from sn_agent.network.enum import NetworkStatus

from sn_agent.agent.base import AgentBase
from sn_agent.ontology.ontology import Ontology
from sn_agent.ontology.service_descriptor import ServiceDescriptor
from sn_agent.network.provider import ExternalServiceProvider

logger = logging.getLogger(__name__)


class TestNetwork(NetworkABC):
    def __init__(self, app):
        super().__init__(app)
        logger.debug('Test Network Started')

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
        return NetworkStatus.STATUS_NON_MEMBER

    def am_i_a_member(self) -> bool:
        """
        Determine what the current network status is (joined or not joined)
        """
        return self.get_network_status() == NetworkStatus.STATUS_MEMBER

    def update_ontology(self):
        """
        Updates self.ontology from the blockchain with any changes since the last
        time update was called.
        """
        pass

    def advertise_service(self, service: ServiceDescriptor):
        """
        Given an ontology, advertise it as a service that the agent provides
        :param service: a service objects defining a service spec
        """
        pass

    def remove_service_advertisement(self, service: ServiceDescriptor):
        """
        Remove the advertisement of the service for a given agent
        :param service:
        """
        pass

    def find_service_providers(self, service: ServiceDescriptor) -> list:
        """
        Called by the UI as well as find_provider - should return a list that contains
        information about all the providers that have indicated that they can proved
        the designated service.
        :param service:
        :return: a list of external agents which provide the service requested
        """
        pass
