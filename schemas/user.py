from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):

    username   :Optional[str]
    password   :Optional[str]
    email      :Optional[str]
    first_name :Optional[str]
    last_name  :Optional[str]
    is_staff   :Optional[bool]
    status     :Optional[bool]

    class Config:
        orm_mode = True


class UserShow(BaseModel):

    id         :Optional[str]
    username   :Optional[str]
    password   :Optional[str]
    email      :Optional[str]
    first_name :Optional[str]
    last_name  :Optional[str]
    is_staff   :Optional[bool]
    status     :Optional[bool]

    class Config:
        orm_mode = True