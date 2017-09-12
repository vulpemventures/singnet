#
# sn_agent/provider.py - implementation of wrapper for  external service provider agents.
# ExternalServiceProviders use the network to connect with other Agents to have them
# perform service sub-services required for this agent to implement a service.
#
# For example, a machine learning agent that processes large amounts of data might
# use an AWS-centered service provider to store input and output files. So one of
# the services required to perform a service is to obtain input and output URLs
# which can be used for performing this agent's service. The Singnet agent
# will keep a reference to this external provider
#
# Copyright (c) 2017 SingularityNET
#
# Distributed under the MIT software license, see LICENSE file.
#

from sn_agent.agent.base import AgentABC
from sn_agent.ontology.service_descriptor import ServiceDescriptor

class ExternalServiceProvider(AgentABC):
    def __init__(self, net, agent_id, service: ServiceDescriptor):
        self.net = net
        self.agent_id = agent_id
        self.service = service

    def can_perform(self, service: ServiceDescriptor) -> bool:
        return self.net.ask_agent_if_can_perform(self.agent_id, self.service)

    def perform(self, service: ServiceDescriptor):
        return self.net.ask_agent_to_perform(self.agent_id, self.service)

    def list_providers(self, service: ServiceDescriptor) -> list:
        """
        External providers do not list their sub-providers by default.

        :param service:
        :return:
        """
        pass
