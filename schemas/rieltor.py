from pydantic import BaseModel
from typing import Optional, List
from db.models import Rieltor
from enum import Enum


class RieltorShow(BaseModel):

    id                       :Optional[str]
    first_name               :Optional[str]
    last_name                :Optional[str]
    patronym                 :Optional[str]
    birth_date               :Optional[str]
    pasport                  :Optional[str]
    phone_number             :Optional[str]
    email                    :Optional[str]
    address                  :Optional[str]
    work_experience          :Optional[str]
    image                    :Optional[str]
    power_of_attorney_date   :Optional[str]
    power_of_attorney_number :Optional[str]
    power_of_attorney_term   :Optional[str]
    certificate_date         :Optional[str]
    certificate_number       :Optional[str]
    certificate_file         :Optional[str]
    create_at                :Optional[str]
    update_at                :Optional[str]
    user_id                  :Optional[str]
    username                 :Optional[str]
    password                 :Optional[str]

    class Config:
        orm_mode = True


class RieltorCreate(BaseModel):

    first_name               :Optional[str]
    last_name                :Optional[str]
    patronym                 :Optional[str]
    birth_date               :Optional[str]
    pasport                  :Optional[str]
    phone_number             :Optional[str]
    email                    :Optional[str]
    address                  :Optional[str]
    work_experience          :Optional[str]
    image                    :Optional[str]
    power_of_attorney_date   :Optional[str]
    power_of_attorney_number :Optional[str]
    power_of_attorney_term   :Optional[str]
    certificate_date         :Optional[str]
    certificate_number       :Optional[str]
    certificate_file         :Optional[str]
    username                 :Optional[str]
    password                 :Optional[str]
    
    class Config:
        orm_mode = True