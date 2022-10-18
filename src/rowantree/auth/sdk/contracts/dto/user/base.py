""" Auth Service User Base Definition """

from typing import Optional

from rowantree.contracts import BaseModel


class UserBase(BaseModel):
    """
    Auth Service User Base

    Attributes
    ----------
    username: str
        The username of the user.
    guid: str
        The optional user guid.
    email: Union[str, None] = None
        The optional user email address.
    disabled: Union[bool, None] = None
        Whether the account is enabled or not (optional).
    admin: Union[bool, None] = None
        Whether the account is an admin or not (optional).
    """

    username: str
    guid: Optional[str] = None
    email: Optional[str] = None
    disabled: Optional[bool] = None
    admin: Optional[bool] = None
