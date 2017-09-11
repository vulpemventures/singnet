from pathlib import Path

from sn_agent import SettingsBase, Required


class ServiceAdapterSettings(SettingsBase):
    def __init__(self, **custom_settings):
        self._ENV_PREFIX = 'SN_SERVICE_ADAPTER_'

        # This is a yaml config file
        self.CONFIG_FILE = Required(Path)

        super().__init__(**custom_settings)
