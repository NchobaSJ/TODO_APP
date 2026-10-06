import uuid
from pydantic import BaseModel, Field, field_validator

from app.schemas.category import CategoryRead


# ---------- Base ----------
class TaskBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str = Field(default="", max_length=2000)
    completed: bool = False

    @field_validator("title")
    @classmethod
    def title_not_blank(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Task title cannot be blank.")
        return v


# ---------- Create ----------
class TaskCreate(TaskBase):
    category_id: uuid.UUID | None = None


# ---------- Update ----------
class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=2000)
    completed: bool | None = None
    category_id: uuid.UUID | None = None

    @field_validator("title")
    @classmethod
    def title_not_blank(cls, v: str | None) -> str | None:
        if v is None:
            return v
        v = v.strip()
        if not v:
            raise ValueError("Task title cannot be blank.")
        return v


# ---------- Read ----------
class TaskRead(TaskBase):
    id: uuid.UUID
    user_id: uuid.UUID
    category: CategoryRead | None = None  # Optional relationship field

    model_config = {"from_attributes": True}