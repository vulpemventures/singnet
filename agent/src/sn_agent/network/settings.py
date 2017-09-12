import uuid

from sn_agent import SettingsBase, Required

class NetworkSettings(SettingsBase):
    def __init__(self, **custom_settings):
        self._ENV_PREFIX = 'SN_NETWORK_'
        self.NETWORK_CLASS = 'sn_agent.network.test.TestNetwork'
        self.AGENT_ID = Required(uuid.UUID)
        super().__init__(**custom_settings)
