"""Autogenerated API"""
from argus_api import session
import logging
from argus_cli.plugin import register_command
from argus_plugins import argus_cli_module

log = logging.getLogger(__name__)


@register_command(
    extending=("authentication", "v1", "apikey"),
    module=argus_cli_module
)
def initiate_1(
    description: str = None,
    validSources: str = None,
    password: str = None,
    expirationDays: int = None,
    sessionConstraints: dict = None,
    disableSourceRestriction: bool = None,
    disableExpiration: bool = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Initiate a new apikey for current user (PUBLIC)
    
    :param str description: [\s\w\{\}\$\-\(\)\.\[\]"\'_/\\,\*\+\#:@!?;=]*
    :param str validSources: Client IP/CIDR networks which the api key will be valid for.
    :param str password: User password to verify this request 
    :param int expirationDays: Requested expiration days, 0 means unlimited. Default is 3 months. If user does not have permissions to specify expiration period, an error will be returned. 
    :param dict sessionConstraints: 
    :param bool disableSourceRestriction: Request API-key without source restriction. If key without source restriction is not permitted, a 412 error will be returned. (default false)
    :param bool disableExpiration: Request API-key with unlimited expiration. If unlimited expiration is not permitted, a 412 error will be returned. (default false):param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises NotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/authentication/v1/apikey".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send description if the argument was provided, dont send null values
    if description is not None:
        body.update({"description": description})
    # Only send validSources if the argument was provided, dont send null values
    if validSources is not None:
        body.update({"validSources": validSources})
    # Only send password if the argument was provided, dont send null values
    if password is not None:
        body.update({"password": password})
    # Only send disableSourceRestriction if the argument was provided, dont send null values
    if disableSourceRestriction is not None:
        body.update({"disableSourceRestriction": disableSourceRestriction})
    # Only send expirationDays if the argument was provided, dont send null values
    if expirationDays is not None:
        body.update({"expirationDays": expirationDays})
    # Only send disableExpiration if the argument was provided, dont send null values
    if disableExpiration is not None:
        body.update({"disableExpiration": disableExpiration})
    # Only send sessionConstraints if the argument was provided, dont send null values
    if sessionConstraints is not None:
        body.update({"sessionConstraints": sessionConstraints})

    query_parameters = {}

    log.debug("POST %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.post(
        route,
        params=query_parameters or None,
        json=body,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json()


@register_command(
    extending=("authentication", "v1", "apikey"),
    module=argus_cli_module
)
def list_1(
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """List current user apikeys (PUBLIC)
    :param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises NotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/authentication/v1/apikey".format()

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}

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


@register_command(
    extending=("authentication", "v1", "apikey"),
    module=argus_cli_module
)
def renew_2(
    prefix: str,
    password: str = None,
    expirationDays: int = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Renew an apikey for current user
    
    :param str prefix: Key prefix on the form 1ab/2c
    :param str password: User password to verify this request 
    :param int expirationDays: Requested expiration days, 0 means unlimited. Default is 3 months. If user does not have permissions to specify expiration period, an error will be returned. :param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises NotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/authentication/v1/apikey/{prefix}".format(prefix=prefix)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send password if the argument was provided, dont send null values
    if password is not None:
        body.update({"password": password})
    # Only send expirationDays if the argument was provided, dont send null values
    if expirationDays is not None:
        body.update({"expirationDays": expirationDays})

    query_parameters = {}

    log.debug("PUT %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.put(
        route,
        params=query_parameters or None,
        json=body,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json()


@register_command(
    extending=("authentication", "v1", "apikey"),
    module=argus_cli_module
)
def renew_3(
    keyID: int,
    password: str = None,
    expirationDays: int = None,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """null (PUBLIC)
    
    :param int keyID: Key ID
    :param str password: User password to verify this request 
    :param int expirationDays: Requested expiration days, 0 means unlimited. Default is 3 months. If user does not have permissions to specify expiration period, an error will be returned. :param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :returns dictionary translated from JSON
    """

    route = "/authentication/v1/apikey/{keyID}".format(keyID=keyID)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}
    # Only send password if the argument was provided, dont send null values
    if password is not None:
        body.update({"password": password})
    # Only send expirationDays if the argument was provided, dont send null values
    if expirationDays is not None:
        body.update({"expirationDays": expirationDays})

    query_parameters = {}

    log.debug("PUT %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.put(
        route,
        params=query_parameters or None,
        json=body,
        verify=verify,
        apiKey=apiKey,
        authentication=authentication,
        server_url=server_url,
        headers=headers,
        proxies=proxies,
    )
    return response.json()


@register_command(
    extending=("authentication", "v1", "apikey"),
    module=argus_cli_module
)
def revoke_2(
    prefix: str,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """Revoke an apikey from current user
    
    :param str prefix: Key prefix on the form 1ab/2c:param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :raises AuthenticationFailedException: on 401
    :raises AccessDeniedException: on 403
    :raises NotFoundException: on 404
    :raises ValidationErrorException: on 412
    :raises ArgusException: on other status codes
    
    :returns dictionary translated from JSON
    """

    route = "/authentication/v1/apikey/{prefix}".format(prefix=prefix)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}

    log.debug("DELETE %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.delete(
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


@register_command(
    extending=("authentication", "v1", "apikey"),
    module=argus_cli_module
)
def revoke_3(
    keyID: int,
    json: bool = True,
    verify: bool = None,
    proxies: dict = None,
    apiKey: str = None,
    authentication: dict = {},
    server_url: str = None,
    body: dict = None,
  ) -> dict:
    """null (PUBLIC)
    
    :param int keyID: Key ID:param json:
    :param verify: path to a certificate bundle or boolean indicating whether SSL
    verification should be performed.
    :param apiKey: Argus API key.
    :param authentication: authentication override
    :param server_url: API base URL override
    :param body: body of the request. other parameters will override keys defined in the body.
    :returns dictionary translated from JSON
    """

    route = "/authentication/v1/apikey/{keyID}".format(keyID=keyID)

    headers = {
        'User-Agent': 'ArgusToolbelt/',
    }

    body = body or {}

    query_parameters = {}

    log.debug("DELETE %s (headers: %s, body: %s)" % (route, str(headers), str(body) or ""))

    response = session.delete(
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

