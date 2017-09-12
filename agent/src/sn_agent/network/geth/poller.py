import asyncio
import datetime
import logging
from contextlib import suppress

from aiohttp import web

logger = logging.getLogger(__file__)


class Periodic:
    def __init__(self, func, time):
        self.func = func
        self.time = time
        self.is_started = False
        self._task = None

    async def start(self):
        logger.debug('Starting periodic task')
        if not self.is_started:
            self.is_started = True
            # Start task to call func periodically:
            self._task = asyncio.ensure_future(self._run())

    async def stop(self):
        logger.debug('Stopping periodic task')
        if self.is_started:
            self.is_started = False
            # Stop task and await it stopped:
            self._task.cancel()
            with suppress(asyncio.CancelledError):
                await self._task

    async def _run(self):
        while True:
            await asyncio.sleep(self.time)
            self.func()


def task_to_run():
    print('Periodic Task: %s' % datetime.datetime.now())


async def startup(app: web.Application):
    poller = Periodic(task_to_run, 5)
    await poller.start()
    app['eth_client_poller'] = poller


async def cleanup(app: web.Application):
    await app['eth_client_poller'].stop()


def setup_poller(app):
    app.on_startup.append(startup)
    app.on_cleanup.append(cleanup)
