from urllib3.util import Url

from sn_agent import SettingsBase, Required


class GetSettings(SettingsBase):
    def __init__(self, **custom_settings):
        self._ENV_PREFIX = 'SN_GETH_'
        self.ETH_CLIENT = Required(Url)
        super().__init__(**custom_settings)
