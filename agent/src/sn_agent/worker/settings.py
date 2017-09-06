from pathlib import Path

from sn_agent import SettingsBase, Required


class WorkerSettings(SettingsBase):
    def __init__(self, **custom_settings):
        self._ENV_PREFIX = 'SN_WORKER_'

        # This is a yaml config file
        self.WORKER_CONFIG_FILE = Required(Path)

        super().__init__(**custom_settings)
