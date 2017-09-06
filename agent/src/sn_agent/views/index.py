import logging

from aiohttp_jinja2 import template

logger = logging.getLogger(__file__)


@template('index.jinja')
async def index(request):
    """
    This is the view handler for the "/" url.

    :param request: the request object see http://aiohttp.readthedocs.io/en/stable/web_reference.html#request
    :return: context for the template.
    """
    logger.debug("Index requested")

    # Note: we return a dict not a response because of the @template decorator
    return {
        'title': request.app['name'],
        'intro': "Success! you've setup a basic aiohttp app.",
        'page_title': "SingularityNET"
    }
