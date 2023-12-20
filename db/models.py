from sqlalchemy import Column, Date, ForeignKey,  String,  Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    username = Column(String(25), unique=True)
    password = Column(String(255))
    email = Column(String(80), unique=True)
    first_name = Column(Text, nullable = True)
    last_name = Column(Text, nullable = True)
    is_staff = Column(Boolean, default = False)
    status = Column(Boolean, default = False)
    create_at = Column(String(50))
    update_at = Column(String(50))
    rieltors = relationship('Rieltor', back_populates = 'user')

    def __repr__(self):
        return f"<User {self.username}>"
    

class Rieltor(Base):
    __tablename__ = 'rieltors'

    id = Column(String, primary_key=True)
    username = Column(String(25), unique=True)
    password = Column(String(255))
    first_name = Column(String, nullable = True)
    last_name = Column(String, nullable = True)
    patronym = Column(String, nullable = True)
    birth_date = Column(String, nullable = True)
    pasport = Column(String, nullable = True, unique=True)
    phone_number = Column(String, nullable = True, unique=True)
    email = Column(String, nullable = True, unique=True)
    address = Column(String, nullable = True)
    work_experience = Column(String, nullable = True)
    image = Column(String, nullable = True)
    power_of_attorney_date = Column(String, nullable = True)
    power_of_attorney_number = Column(String, nullable = True)
    power_of_attorney_term = Column(String, nullable = True)
    certificate_date = Column(String, nullable = True)
    certificate_number = Column(String, nullable = True, unique=True)
    certificate_file = Column(String, nullable = True)
    create_at = Column(String, nullable = True)
    update_at = Column(String, nullable = True)
    user_id = Column(String, ForeignKey('users.id'))
    user = relationship('User', back_populates = 'rieltors')

    def __repr__(self):
        return f"<Rieltor {self.id}>"