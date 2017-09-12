from jinja2.utils import import_string

from sn_agent.ontology.settings import OntologySettings


def setup_ontology(app):
    settings = OntologySettings()
    ontology_klass = import_string(settings.ONTOLOGY_CLASS)
    app['ontology'] = ontology_klass(app)
