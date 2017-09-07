import yaml
from jinja2.utils import import_string

from sn_agent.worker.jsonrpc import JsonRpcWorker
from sn_agent.worker.opencog import OpenCogWorker
from sn_agent.worker.settings import WorkerSettings


def setup_workers(app):
    settings_obj = WorkerSettings()

    config_file = settings_obj.WORKER_CONFIG_FILE

    with open(config_file, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    workers = []

    for section, data in cfg.items():
        ontology_node_id = data.get('ontology_node_id')
        if ontology_node_id is None:
            raise RuntimeError('You must supply a ontology_node_id for each worker')

        required_ontology_node_ids = data.get('required_ontology_node_ids')

        if section == 'opencog':
            host = data['host']
            port = data['port']
            worker = OpenCogWorker(app, ontology_node_id, required_ontology_node_ids, host, port)

        elif section == 'jsonrpc':
            url = data['url']
            worker = JsonRpcWorker(app, ontology_node_id, required_ontology_node_ids, url)

        elif section == 'module':
            name = data['name']
            module_klass = import_string(name)
            worker = module_klass(app, ontology_node_id, required_ontology_node_ids, name)

        else:
            raise RuntimeError('Unknown worker type specified: %s' % section)

        workers.append(worker)

    # All worker objects loaded, now init them

    for worker in workers:
        worker.init()
