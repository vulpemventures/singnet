#
# sn_agent/base.py - implementation of the ontology of services
#
# Copyright (c) 2017 SingularityNET
#
# Distributed under the MIT software license, see LICENSE file.
#

from abc import abstractmethod, ABC


class OntologyABC(ABC):
    def __init__(self, app):
        self.app = app
        self.version = None

    @abstractmethod
    def get_service_description(self, node_id) -> str:
        """
        This is used for creating the tree of services behind a given ontology

        :param node_id: the node whose description should be returned
        :return: the description of that node
        """
        pass
