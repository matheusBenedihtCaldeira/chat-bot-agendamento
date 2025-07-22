# SQLAlchemy imports
from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from .. import table_registry
# Utils imports
from datetime import datetime
import uuid
from typing import Optional


@table_registry.mapped_as_dataclass
class ConversationModel:
    __tablename__ = "tb_conversations"

    message: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False)
    timestamp: Mapped[datetime] = mapped_column(
        server_default=func.now(), init=False
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("tb_users.id"),
        nullable=False
    )
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default_factory=uuid.uuid4
    )

    user: Mapped[Optional["UserModel"]] = relationship("UserModel", back_populates="conversations", init=False)
