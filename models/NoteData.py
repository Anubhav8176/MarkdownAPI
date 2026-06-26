from datetime import datetime, timezone
from uuid import UUID, uuid4

from sqlalchemy import String, Text, DateTime

from database.database import Base
from sqlalchemy.orm import Mapped, mapped_column


# We need to add Mapped to let sqlalchemy do its alchemy
class MarkdownNote(Base):
    __tablename__ = "markdown_note"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4
    )
    file_name: Mapped[str] = mapped_column(name="file_name", type_=String(255))
    content: Mapped[str] = mapped_column(name="content", type_=Text, default="No content found!!")
    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        name="uploaded_at",
        default=lambda : datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        name="updated_at",
        default=lambda : datetime.now(timezone.utc),
        onupdate=lambda : datetime.now(timezone.utc)
    )