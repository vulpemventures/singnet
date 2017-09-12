import logging
from json import loads

from aiohttp.hdrs import METH_POST
from aiohttp.web_exceptions import HTTPFound
from aiohttp_jinja2 import template
from aiohttp_session import get_session
from jinja2.utils import import_string
from settings import Settings

logger = logging.getLogger(__file__)


@template('network/index.jinja')
async def index(request):
    settings = Settings()

    if request.method == METH_POST:
        # the 302 redirect is processed as an exception, so if this coroutine returns there's a form error
        form_errors = await process_form(request)
    else:
        form_errors = None

    network_klass = import_string(settings.NETWORK_CLASS)
    network_api = network_klass()
    network_status = network_api.status()

    return {
        'page_title': 'Network',
        'network_status': network_status,
        'form_errors': form_errors
    }


async def process_form(request):
    settings = Settings()

    new_job = {}
    missing_fields = []

    fields = ['ontology_id', 'json_content']

    data = await request.post()
    for f in fields:
        new_job[f] = data.get(f)
        if not new_job[f]:
            missing_fields.append(f)

    if missing_fields:
        return 'Invalid form submission, missing fields: {}'.format(', '.join(missing_fields))

    ontology_id = new_job['ontology_id']
    json_content = loads(new_job['json_content'])

    session = await get_session(request)
    session['ontology_id'] = ontology_id

    service_klass = import_string(settings.SERVICE_CLASS)

    agent_id = service_klass().find_provider(ontology_id)

    if not service_klass.can_perform(agent_id, ontology_id):
        return 'The service indicates that this service cannot be performed at this time'

    result = service_klass.perform(agent_id, ontology_id, json_content)

    # TODO Record the result of the perform so we can check on its status

    redirect_url = request.app.router['jobs'].url()

    raise HTTPFound(redirect_url)
