import uuid
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from app.core.database import Base

if TYPE_CHECKING:
    # Only imported for type checkers, NOT at runtime → no circular import
    from app.models.task import Task
    from app.models.category import Category


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"

    first_name: Mapped[str] = mapped_column(default="", nullable=False)
    last_name: Mapped[str] = mapped_column(default="", nullable=False)

    tasks: Mapped[list["Task"]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )
    categories: Mapped[list["Category"]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )