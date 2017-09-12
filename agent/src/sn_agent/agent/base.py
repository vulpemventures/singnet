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
from sn_agent.network.enum import NetworkStatus
from sn_agent.ontology.ontology import Ontology
from enum import Enum


class AgentBase(metaclass=ABCMeta):
    def __init__(self, app, agent_id):
        self.app = app
        self.agent_id = agent_id

    @abstractmethod
    def can_perform(self, agent_id, ontology_node_id) -> bool:
        """
        :param agent_id:
        :param ontology_node_id:
        :return:
        """
        pass

    @abstractmethod
    def perform(self, agent_id, ontology_id, json_content) -> bool:
        """

        :return:
        """
        pass

    @abstractmethod
    def list_providers(self, agent_id, ontology_node_id) -> list:
        """
        This is used for creating the tree of services behind a given ontology

        :param agent_id:
        :param ontology_node_id:
        :return:
        """
        pass
