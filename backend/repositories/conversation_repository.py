# SQL imports
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import asc
# Models imports
from models.conversations.models import ConversationModel
import uuid
from models.users.models import UserModel

class ConversationRepository:
    def __init__(self, db: Session):
        self.__db = db

    def get_user_conversation_history(self, user_id: uuid.UUID):
        stmt = (select(ConversationModel)
                .where(ConversationModel.user_id == user_id)
                .order_by(asc(ConversationModel.timestamp)))
        res = self.__db.scalars(stmt).all()
        return res

    def add_message(self, user_id: uuid.UUID, message: str, role: str) -> ConversationModel :
        conversation = ConversationModel(
            user_id=user_id,
            message=message,
            role=role
        )
        self.__db.add(conversation)
        self.__db.commit()
        self.__db.refresh(conversation)
        return conversation
