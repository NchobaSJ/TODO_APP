import uuid
from pydantic import BaseModel, Field, field_validator

from app.schemas.user import UserRead


# ---------- Base: shared fields ----------
class CategoryBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)

    @field_validator("name")
    @classmethod
    def name_not_blank(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Category name cannot be blank.")
        return v


# ---------- Create: what client sends on POST ----------
class CategoryCreate(CategoryBase):
    pass


# ---------- Update: what client sends on PATCH (all optional) ----------
class CategoryUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)

    @field_validator("name")
    @classmethod
    def name_not_blank(cls, v: str | None) -> str | None:
        if v is None:
            return v
        v = v.strip()
        if not v:
            raise ValueError("Category name cannot be blank.")
        return v


# ---------- Read: what server returns ----------
class CategoryRead(CategoryBase):
    id: uuid.UUID
    user_id: uuid.UUID
    owner: UserRead
    

    # ← This is the "ModelSerializer" magic: read from ORM objects
    model_config = {"from_attributes": True}