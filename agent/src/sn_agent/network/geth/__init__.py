from network.base import NetworkBase


class GethNetwork(NetworkBase):
    def join_network(self):
        raise NotImplementedError()

    def leave_network(self):
        raise NotImplementedError()
