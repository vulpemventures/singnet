import aiohttp
from jsonrpcclient.aiohttp_client import aiohttpClient

from sn_agent.worker.base import WorkerBase


class JsonRpcWorker(WorkerBase):
    type_name = "JSON-RPC"

    def __init__(self, app, ontology_node_id, required_ontology_node_ids, url):
        super().__init__(app, ontology_node_id, required_ontology_node_ids)

        self.url = url
        self.loop = app.loop

    async def can_perform(self) -> bool:

        if not self.requirements_met:
            return False

        if not self.available:
            return False

        if not self.all_required_agents_can_perform():
            return False

        async with aiohttp.ClientSession(loop=self.loop) as session:
            client = aiohttpClient(session, self.url)
            response = await client.request('can_perform')
            return response

    async def perform(self, *args, **kwargs):
        async with aiohttp.ClientSession(loop=self.loop) as session:
            client = aiohttpClient(session, self.url)
            response = await client.request('perform', *args, **kwargs)
            return response
