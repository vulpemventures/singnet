from sn_agent import SettingsBase


class NetworkSettings(SettingsBase):
    def __init__(self, **custom_settings):
        self._ENV_PREFIX = 'SN_NETWORK_'
        self.CLASS = 'sn_agent.network.test.TestNetwork'
        super().__init__(**custom_settings)
