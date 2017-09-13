from sn_agent import SettingsBase, Required


class UISettings(SettingsBase):
    def __init__(self, **custom_settings):
        self._ENV_PREFIX = 'SN_AGENT_'
        self.COOKIE_SECRET = Required(str)
        super().__init__(**custom_settings)
