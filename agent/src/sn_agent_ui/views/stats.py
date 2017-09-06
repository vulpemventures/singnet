import json
import logging

import jsonrpcclient
from aiohttp_jinja2 import template

from sn_agent.network import NetworkSettings

logger = logging.getLogger(__file__)


@template('stats/index.jinja')
async def index(request):
    logger.debug('Stats page requested')

    settings = NetworkSettings()

    net_version = jsonrpcclient.request(settings.ETH_CLIENT, 'admin_nodeInfo')
    eth_client_modules = jsonrpcclient.request(settings.ETH_CLIENT, 'rpc_modules')

    shh_info = jsonrpcclient.request(settings.ETH_CLIENT, 'shh_info')

    accounts = jsonrpcclient.request(settings.ETH_CLIENT, 'personal_listAccounts')

    return {
        'net_version': json.dumps(net_version, indent=4, sort_keys=True),
        'eth_client_modules': json.dumps(eth_client_modules, indent=4, sort_keys=True),
        'shh_info': json.dumps(shh_info, indent=4, sort_keys=True),
        'accounts': json.dumps(accounts, indent=4, sort_keys=True),
        'page_title': "Stats"
    }
