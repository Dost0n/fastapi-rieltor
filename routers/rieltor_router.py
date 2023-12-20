from fastapi import APIRouter
from routers.login_router import get_current_user_from_token
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from db.models import User, Rieltor
from typing import List
from db.session import get_db
from schemas.rieltor import RieltorCreate, RieltorShow
from schemas.user import UserCreate, UserShow
from repository.rieltor import list_rieltors,create_rieltor, retreive_rieltor, update_rieltor, delete_rieltor
from repository.user import create_user


router = APIRouter()


""" ## Get Rieltor List """
@router.get("/all", response_model=List[RieltorShow])
def rieltor_list(db:Session = Depends(get_db), user:User = Depends(get_current_user_from_token)):
    user_id = user.id
    current_user = db.query(User).filter(User.id == user_id).first()
    if current_user.is_staff:
        rieltors = list_rieltors(db=db)
        return rieltors
    raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
            detail = "This user is not superuser")


""" ## Rieltor Create """
@router.post("/create", status_code = status.HTTP_201_CREATED, response_model=RieltorShow)
def rieltor_create(rieltor:RieltorCreate, db:Session = Depends(get_db), user:User = Depends(get_current_user_from_token)):
    db_username = db.query(User).filter(User.username == rieltor.username).first()
    if db_username is not None:
        return HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
            detail = "This username already exist")
    db_email = db.query(User).filter(User.email == rieltor.email).first()
    if db_email is not None:
        return HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
            detail = "This email address already exist")
    db_pasport = db.query(Rieltor).filter(Rieltor.pasport == rieltor.pasport).first()
    if db_pasport is not None:
        return HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
            detail = "This passport already exist")
    db_phone_number = db.query(Rieltor).filter(Rieltor.phone_number == rieltor.phone_number).first()
    if db_phone_number is not None:
        return HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
            detail = "This phone number already exist")
    db_sertificate_number = db.query(Rieltor).filter(Rieltor.certificate_number == rieltor.certificate_number).first()
    if db_sertificate_number is not None:
        return HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
            detail = "This certificate number already exist")

    rieltor_user = create_user(user = rieltor, db = db)
    rieltor = create_rieltor(rieltor = rieltor, db = db, user_id = user.id)
    return rieltor


""" ## Get Rieltor by id """
@router.get("/get/{id}", response_model=RieltorShow)
def rieltor_retrieve(id:str, db:Session = Depends(get_db), user:User = Depends(get_current_user_from_token)):
    user_id = user.id
    current_user = db.query(User).filter(User.id == user_id).first()
    if current_user.is_staff:
        rieltor = retreive_rieltor(id=id,db=db)
        if not rieltor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Rieltor with this id {id} does not exist")
        return rieltor
    raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
            detail = "This user is not superuser")
    

""" ## Rieltor Update """
@router.put("/update/{id}")
def rieltor_update(rieltor:RieltorCreate, id:str, db:Session = Depends(get_db), user:User = Depends(get_current_user_from_token)):
    user_id = user.id
    current_user = db.query(User).filter(User.id == user_id).first()
    if current_user.is_staff:
        existing_rieltor = retreive_rieltor(id=id,db=db)
        if not existing_rieltor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Order with this id {id} does not exist")
        rieltor = update_rieltor(rieltor_id = existing_rieltor.id, rieltor = rieltor, db = db)
        return {"msg":"Successfully updated data."}
    raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
            detail = "This user is not superuser")
    

""" ## Rieltor Delete """
@router.delete("/delete/{id}")
def rieltor_delete(id:str, db:Session = Depends(get_db), user:User = Depends(get_current_user_from_token)):
    user_id = user.id
    current_user = db.query(User).filter(User.id == user_id).first()
    if current_user.is_staff:
        existing_rieltor = retreive_rieltor(id=id,db=db)
        if not existing_rieltor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Rieltor with this id {id} does not exist")
        rieltor = delete_rieltor(id = id, db = db)
        return {"msg":"Successfully delete data."}
    raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
            detail = "This user is not superuser")