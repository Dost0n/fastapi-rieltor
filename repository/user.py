from sqlalchemy.orm.session import Session
from db.models import User
from schemas.user import UserCreate
import datetime, uuid
from db.hashing import Hasher


def list_users(db : Session):
    users = db.query(User).all()
    return users


def create_user(user: UserCreate, db: Session):
    user_date = str(datetime.datetime.now())
    user_id   = str(uuid.uuid1())
    try:
        user_staff = user.is_staff
        user_status = user.status
    except:
        user_staff = False
        user_status = False
    user_object = User(
        id         = user_id,
        username   = user.username,
        password   = Hasher.get_password_hash(user.password),
        email      = user.email,
        first_name = user.first_name,
        last_name  = user.last_name,
        create_at  = user_date,
        update_at  = user_date,
        is_staff   = user_staff,
        status     = user_status,
    )
    db.add(user_object)
    db.commit()
    db.refresh(user_object)
    return user_object