"""Autogenerated API"""
from argus_api import session
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module

log = logging.getLogger(__name__)


@register_command(
    extending=("pdns", "v3", "cof"),
    module=argus_cli_module
)
def search_records_simplified_c_o_f(
    query: str,
    rrClass: str = None,
    rrType: str = None,
    customerID: int = None,
    tlp: str = None,
    aggregate: bool = True,
    includeAnonymous: bool = True,
    limit: int = 25,
    offset: int = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Search against PassiveDNS and return matching records in PDNS COF format (DEV)
    
    :param str query: Search by query
    :param list rrClass: Search by recordClass (rrclass)
    :param list rrType: Search by type (rrtype)
    :param list customerID: Search by customerID
    :param list tlp: Search by TLP
    :param bool aggregate: Whether aggregate records
    :param bool includeAnonymous: Whether include anonymous records
    :param int limit: Max number of records to be returned
    :param int offset: Skip a number of records:param json:
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

    route = "/pdns/v3/cof/{query}".format(aggregate=aggregate,
        includeAnonymous=includeAnonymous,
        limit=limit,
        query=query,
        rrClass=rrClass,
        rrType=rrType,
        customerID=customerID,
        tlp=tlp,
        offset=offset)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}
    # Only send aggregate if the argument was provided, dont send null values
    if aggregate is not None:
        query_parameters.update({"aggregate": aggregate})
    # Only send includeAnonymous if the argument was provided, dont send null values
    if includeAnonymous is not None:
        query_parameters.update({"includeAnonymous": includeAnonymous})
    # Only send limit if the argument was provided, dont send null values
    if limit is not None:
        query_parameters.update({"limit": limit})
    # Only send rrClass if the argument was provided, dont send null values
    if rrClass is not None:
        query_parameters.update({"rrClass": rrClass})
    # Only send rrType if the argument was provided, dont send null values
    if rrType is not None:
        query_parameters.update({"rrType": rrType})
    # Only send customerID if the argument was provided, dont send null values
    if customerID is not None:
        query_parameters.update({"customerID": customerID})
    # Only send tlp if the argument was provided, dont send null values
    if tlp is not None:
        query_parameters.update({"tlp": tlp})
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
    return response.json()

