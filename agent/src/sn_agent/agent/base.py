#
# sn_agent/base.py - implementation of abstract class defining API for Network
# communication with block-chain implementations through connections with
# smart contracts and block-chain messaging systems.
#
# Copyright (c) 2017 SingularityNET
#
# Distributed under the MIT software license, see LICENSE file.
#

from sn_agent.network.enum import NetworkStatus
from sn_agent.ontology.service_descriptor import ServiceDescriptor
from enum import Enum

import logging
from abc import abstractmethod, ABC

from sn_agent.ontology.service_descriptor import ServiceDescriptor

logger = logging.getLogger(__name__)


class AgentABC(ABC):
    def __init__(self, app, agent_id):
        self.app = app
        self.agent_id = agent_id

    @abstractmethod
    def can_perform(self, service: ServiceDescriptor) -> bool:
        """
        :param service: the service to perform
        :result: can this agent perform the described service?
        """
        pass

    @abstractmethod
    def perform(self, agent_id, service: ServiceDescriptor):
        """
        :param service: the service to perform
        """
        pass

    @abstractmethod
    def list_providers(self, service: ServiceDescriptor) -> list:
        """
        This is used for creating the tree of subprovider services behind a given service

        :param service: the service for which to list sub-providers.
        :return:
        """
        pass
