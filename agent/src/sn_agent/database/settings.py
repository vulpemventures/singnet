from urllib3.util import Url

from sn_agent import SettingsBase, Required


class DatabaseSettings(SettingsBase):
    def __init__(self, **custom_settings):
        self._ENV_PREFIX = 'SN_DB_'
        self.URL = Required(Url)
        super().__init__(**custom_settings)
