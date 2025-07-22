# SQL imports
from pandas.core.config_init import styler_mathjax
from sqlalchemy.orm import Session
from sqlalchemy import select
# Models imports
from models.users.models import UserModel

class UserRepository:
    def __init__(self, db: Session):
        self.__db = db

    def index_users(self):
        stmt = select(UserModel)
        res = self.__db.scalars(stmt).all()
        return res

    def get_user_by_number(self, number:str):
        stmt = select(UserModel).where(UserModel.whatsapp_number == number)
        return self.__db.scalars(stmt).first()

    def add_user(self, number: str, profile_name: str) -> UserModel:
        user = UserModel(
            profile_name=profile_name,
            whatsapp_number=number
        )
        self.__db.add(user)
        self.__db.commit()
        self.__db.refresh(user)
        return user
