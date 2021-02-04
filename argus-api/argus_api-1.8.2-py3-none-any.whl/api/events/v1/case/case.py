"""Autogenerated API"""
from argus_api import session
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module
from requests import Response

log = logging.getLogger(__name__)


@register_command(
    extending=("events", "v1", "case"),
    module=argus_cli_module
)
def get_events_for_case(
    caseID: int,
    limit: int = 25,
    offset: int = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> Response:
    """Fetch events associated with specified case (PUBLIC)
    
    :param int caseID: Case ID
    :param int limit: Maximum number of returned results
    :param int offset: Skip a number of results:param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises ValidationFailedException: on 412
    :raises ArgusException: on other status codes
    
    :returns: requests.Response object or dictionary translated from JSON
    """

    route = "/events/v1/case/{caseID}".format(limit=limit,
        caseID=caseID,
        offset=offset)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
        'content': None
    }
    if json:
        headers['content'] = 'application/json'

    body = body or {}

    query_parameters = {}
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    # Only send offset if the argument was provided, dont send null values
    if offset is not None:
        query_parameters.update({"offset": offset})

    log.debug("GET %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.get(
        route,
        params=query_parameters or None,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json() if json else response

