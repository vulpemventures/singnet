#
# sn_agent/base.py - implementation of abstract class defining API for Network
# communication with block-chain implementations through connections with
# smart contracts and block-chain messaging systems.
#
# Copyright (c) 2017 SingularityNET
#
# Distributed under the MIT software license, see LICENSE file.
#

from sn_agent.agent.base import AgentBase
from sn_agent.network.enum import NetworkStatus
from sn_agent.ontology.ontology import Ontology
from sn_agent.ontology.service import Service
from enum import Enum


class TestAgent(AgentBase):
    def __init__(self, app, agent_id):
        self.app = app
        self.agent_id = agent_id

    def can_perform(self, service: Service) -> bool:
        pass

    def perform(self, service: Service) -> bool:
        pass

    def list_providers(self, service: Service) -> list:
         pass
