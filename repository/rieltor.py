from sqlalchemy.orm import Session
from db.models import Rieltor
from schemas.rieltor import RieltorShow, RieltorCreate
import datetime, uuid
from db.hashing import Hasher


def list_rieltors(db : Session):
    orders = db.query(Rieltor).all()
    return orders


def create_rieltor(rieltor: RieltorCreate, db: Session, user_id = str):
    create_date = str(datetime.datetime.now())
    rieltor_id   = str(uuid.uuid1())
    rieltor_object = Rieltor(
        id                       = rieltor_id,
        create_at                = create_date,
        update_at                = create_date,
        user_id                  = user_id,
        first_name               = rieltor.first_name,
        last_name                = rieltor.last_name,
        patronym                 = rieltor.patronym,
        birth_date               = rieltor.birth_date,
        pasport                  = rieltor.pasport,
        phone_number             = rieltor.phone_number,
        email                    = rieltor.email,
        address                  = rieltor.address,
        work_experience          = rieltor.work_experience,
        image                    = rieltor.image,
        power_of_attorney_date   = rieltor.power_of_attorney_date,
        power_of_attorney_number = rieltor.power_of_attorney_number,
        power_of_attorney_term   = rieltor.power_of_attorney_term,
        certificate_date         = rieltor.certificate_date,
        certificate_number       = rieltor.certificate_number,
        certificate_file         = rieltor.certificate_file,
        username                 = rieltor.username,
        password                 = Hasher.get_password_hash(rieltor.password)
    )
    db.add(rieltor_object)
    db.commit()
    db.refresh(rieltor_object)
    return rieltor_object



def retreive_rieltor(id:str, db:Session):
    rieltor = db.query(Rieltor).filter(Rieltor.id == id).first()
    return rieltor


def update_rieltor(rieltor_id:str, rieltor: RieltorCreate, db: Session):
    rieltor_update = db.query(Rieltor).filter(Rieltor.id == rieltor_id)
    rieltor_update.update(rieltor.__dict__)
    db.commit()
    return 1


def delete_rieltor(id:str,db: Session):
    rieltor_delete = db.query(Rieltor).filter(Rieltor.id == id)
    rieltor_delete.delete(synchronize_session=False)
    db.commit()
    return 1