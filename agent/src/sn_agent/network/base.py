#
# sn_agent/base.py - implementation of abstract class defining API for Network
# communication with block-chain implementations through connections with
# smart contracts and block-chain messaging systems.
#
# Copyright (c) 2017 SingularityNET
#
# Distributed under the MIT software license, see LICENSE file.
#

from abc import ABCMeta, abstractmethod
from sn_agent.network.settings import NetworkSettings
from sn_agent.network.enum import NetworkStatus
from sn_agent.ontology.ontology import Ontology
from sn_agent.ontology.service import Service
from sn_agent.agent.base import AgentBase
from enum import Enum

class NetworkBase(metaclass=ABCMeta):
    def __init__(self, app, agent : AgentBase):
        self.app = app
        self.agent = agent
        self.settings = NetworkSettings()
        self.ontology = Ontology(app, '0.70a1')

    @abstractmethod
    def join_network(self) -> bool:
        """
        Agent calls this the first time to connect to the network. An Private and Public key
        should be returned
        """
        pass

    @abstractmethod
    def leave_network(self) -> bool:
        """
        Should this do something in the blockchain or just delete the public and private keys?
        """
        pass


    @abstractmethod
    def logon_network(self) -> bool:
        """
        Agent calls this to logon to the network prior to calling network operations
        """
        pass

    @abstractmethod
    def logoff_network(self) -> bool:
        """
        Agent calls this to loff off the network after calling network operations
        """
        pass

    @abstractmethod
    def get_network_status(self) -> NetworkStatus:
        """
        Determine what the current network status is (joined or not joined)
        """
        pass

    def am_i_a_member(self) -> NetworkStatus:
        """
        Determine what the current network status is (joined or not joined)
        """
        return self.get_network_status() == STATUS_MEMBER

    @abstractmethod
    def update_ontology(self):
        """
        Updates self.ontology from the blockchain with any changes since the last
        time update was called.
        """
        pass

    @abstractmethod
    def advertise_service(self, service: Service):
        """
        Given an ontology, advertise it as a service that the agent provides
        :param service: a service objects defining a service spec
        """
        pass

    @abstractmethod
    def remove_service_advertisement(self, service: Service):
        """
        Remove the advertisement of the service for a given agent
        :param service:
        """
        pass

    @abstractmethod
    def find_service_providers(self, service: Service) -> list:
        """
        Called by the UI as well as find_provider - should return a list that contains
        information about all the providers that have indicated that they can proved
        the designated service.
        :param ontology_node_id:
        :return: a list of external agents which provide the service requested
        """
        pass
