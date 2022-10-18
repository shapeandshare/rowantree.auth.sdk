""" JWT Related Utilities """

from datetime import datetime, timedelta

from jose import jwt

from rowantree.common.sdk import demand_env_var, demand_env_var_as_float

from ..contracts.dto.token import Token
from ..contracts.dto.user.user import User
from .claims import get_issuer


def create_user_access_token(user: User) -> Token:
    """
    Create bearer Token from user instance.

    Parameters
    ----------
    user: User
        An instance of a UserInDB object.

    Returns
    -------
    token: Token
        A bearer token for the requested user.
    """

    # Currently these are the claims we pull from the database.  A larger body
    # of work to migrate to actual claims will update this logic in the future.
    data: dict = {"sub": user.guid, "disabled": user.disabled, "admin": user.admin}
    return create_access_token(data=data)


def create_access_token(data: dict) -> Token:
    """
    Mints the access token.

    Parameters
    ----------
    data: dict
        The base set of claims to include in the token.

    Returns
    -------
    token: Token
        A newly minted token.
    """

    data: dict = data.copy()
    expire: datetime = datetime.utcnow() + timedelta(
        minutes=demand_env_var_as_float(name="ACCESS_TOKEN_EXPIRATION_TIME")
    )
    data.update({"iss": get_issuer(), "exp": expire})
    encoded_jwt: str = jwt.encode(
        data,
        demand_env_var(name="ACCESS_TOKEN_SECRET_KEY"),
        algorithm=demand_env_var(name="ACCESS_TOKEN_ALGORITHM"),
    )
    return Token(access_token=encoded_jwt, token_type="bearer")
