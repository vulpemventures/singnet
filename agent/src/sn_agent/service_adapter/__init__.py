import yaml
from jinja2.utils import import_string

from sn_agent.service_adapter.jsonrpc import JsonRpcServiceAdapter
from sn_agent.service_adapter.opencog import OpenCogServiceAdapter
from sn_agent.service_adapter.settings import ServiceAdapterSettings


class ServiceManager:
    def __init__(self, service_adapters):
        self.service_adapters = service_adapters

    def init_all(self):
        for service_adapter in self.service_adapters:
            service_adapter.init()

    def start(self, service_descriptor):
        # Find the service adapters for a given service descriptor and disable them
        for service_adapter in self.service_adapters:
            if service_adapter.id == service_descriptor.id:
                service_adapter.start()

    def stop(self, service_descriptor):
        # Find the service adapters for a given service descriptor and disable them
        for service_adapter in self.service_adapters:
            if service_adapter.id == service_descriptor.id:
                service_adapter.stop()


def setup_service_manager(app):
    settings_obj = ServiceAdapterSettings()

    config_file = settings_obj.CONFIG_FILE

    with open(config_file, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    service_adapters = []

    for section, data in cfg.items():
        ontology_node_id = data.get('ontology_node_id')
        if ontology_node_id is None:
            raise RuntimeError('You must supply a ontology_node_id for each worker')

        required_ontology_node_ids = data.get('required_ontology_node_ids')

        if section == 'opencog':
            host = data['host']
            port = data['port']
            service_adapter = OpenCogServiceAdapter(app, ontology_node_id, required_ontology_node_ids, host, port)

        elif section == 'jsonrpc':
            url = data['url']
            service_adapter = JsonRpcServiceAdapter(app, ontology_node_id, required_ontology_node_ids, url)

        elif section == 'module':
            name = data['name']
            module_klass = import_string(name)
            service_adapter = module_klass(app, ontology_node_id, required_ontology_node_ids, name)

        else:
            raise RuntimeError('Unknown worker type specified: %s' % section)

        service_adapters.append(service_adapter)

    service_manager = ServiceManager(service_adapters)
    service_manager.init_all()

    app['service_manager'] = service_manager
