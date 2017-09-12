#
# sn_agent/base.py - implementation of abstract class defining API for Network
# communication with block-chain implementations through connections with
# smart contracts and block-chain messaging systems.
#
# Copyright (c) 2017 SingularityNET
#
# Distributed under the MIT software license, see LICENSE file.
#

import logging
from abc import abstractmethod, ABC

from sn_agent.ontology.service_descriptor import ServiceDescriptor

logger = logging.getLogger(__name__)


class AgentABC(ABC):
    def __init__(self, app, agent_id):
        self.app = app
        self.agent_id = agent_id

    @abstractmethod
    def can_perform(self, agent_id, service: ServiceDescriptor) -> bool:
        """
        :param agent_id:
        :param service:
        :return:
        """
        pass

    @abstractmethod
    def perform(self, agent_id, service: ServiceDescriptor, json_content) -> bool:
        """

        :return:
        """
        pass

    @abstractmethod
    def list_providers(self, agent_id, service: ServiceDescriptor) -> list:
        """
        This is used for creating the tree of services behind a given ontology

        :param agent_id:
        :param service:
        :return:
        """
        pass
