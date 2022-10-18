""" Token Claims Definition """

from datetime import datetime

from pydantic import BaseModel


class TokenClaims(BaseModel):
    """
    Token Claims

    Attributes
    ----------
    sub: str
        The subject of the token. (the target user guid)
    iss: str
        The issuer of the token (the auth url for the current domain)
    exp: datetime
        The expiry time of the token
    disabled: bool
        Whether the user is disabled
    admin: bool
        Whether the user is an admin.
    """

    sub: str
    iss: str
    exp: datetime

    # TODO: move to scopes
    disabled: bool
    admin: bool
