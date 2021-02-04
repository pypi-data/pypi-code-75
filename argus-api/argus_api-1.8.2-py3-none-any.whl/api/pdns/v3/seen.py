"""Autogenerated API"""
from argus_api import session
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module

log = logging.getLogger(__name__)


@register_command(
    extending=("pdns", "v3", "seen"),
    module=argus_cli_module
)
def exists_records_of_tlp_levels(
    query: str,
    tlp: str = None,
    ignoreOwnRecords: bool = True,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Search against PassiveDNS and return true if matching records are found (DEV)
    
    :param str query: Search by query, can be IP, not subnet, or domain
    :param list tlp: Search by TLP
    :param bool ignoreOwnRecords: Whether to ignore user's customer's own records, defaults to true:param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises ResourceLimitExceededException: on 402
    :raises AccessDeniedException: on 403
    :raises ValidationFailedException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/pdns/v3/{query}/seen".format(ignoreOwnRecords=ignoreOwnRecords,
        query=query,
        tlp=tlp)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send ignoreOwnRecords if the argument was provided, dont send null values
    if ignoreOwnRecords is not None:
        query_parameters.update({"ignoreOwnRecords": ignoreOwnRecords})
    # Only send tlp if the argument was provided, dont send null values
    if tlp is not None:
        query_parameters.update({"tlp": tlp})

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
    return response.json()

