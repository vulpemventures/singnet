import os

from aiohttp import web

from sn_agent.app import create_app

os.environ.setdefault('SN_AGENT_ID', 'b545478a-971a-48ec-bc56-4b9b7176799c')


os.environ.setdefault('SN_SERVICE_ADAPTER_CONFIG_FILE', 'service_adapter_config_example.yml')

app = create_app()
web.run_app(app, host='localhost', port=8000)
