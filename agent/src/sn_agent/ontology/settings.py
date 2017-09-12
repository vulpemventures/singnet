from sn_agent import SettingsBase


class OntologySettings(SettingsBase):
    def __init__(self, **custom_settings):
        self._ENV_PREFIX = 'SN_ONTOLOGY_'
        self.ONTOLOGY_CLASS = 'sn_agent.ontology.test.TestOntology'
        super().__init__(**custom_settings)
