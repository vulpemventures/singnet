
from sn_agent.ontology.settings import OntologySettings
from sn_agent.utils import import_string


def setup_ontology(app):
    settings = OntologySettings()
    ontology_klass = import_string(settings.ONTOLOGY_CLASS)
    app['ontology'] = ontology_klass(app)
