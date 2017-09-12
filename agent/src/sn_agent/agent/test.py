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

from sn_agent.agent.base import AgentABC

logger = logging.getLogger(__name__)


class TestAgent(AgentABC):

    def __init__(self, app, agent_id):
        super().__init__(app, agent_id)
        logger.debug('Test Agent Started')

    def can_perform(self, agent_id, ontology_node_id) -> bool:
        pass

    def perform(self, agent_id, ontology_id, json_content) -> bool:
        pass

    def list_providers(self, agent_id, ontology_node_id) -> list:
        pass
