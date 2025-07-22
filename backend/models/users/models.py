# SQLAlchemy imports
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from .. import table_registry
# Utils imports
from datetime import datetime
import uuid
from ..conversations.models import ConversationModel
from ..schedule.models import ScheduleModel

@table_registry.mapped_as_dataclass
class UserModel:
    __tablename__ = "tb_users"

    whatsapp_number: Mapped[str] = mapped_column(unique=True, nullable=False)
    profile_name: Mapped[str] = mapped_column(
        nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), init=False
    )
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default_factory=uuid.uuid4
    )
    conversations = relationship("ConversationModel", back_populates="user")
    schedules = relationship("ScheduleModel", back_populates="user")
