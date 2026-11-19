from datetime import datetime
from enum import Enum
from pydantic import BaseModel

class Status(str, Enum):
    DRAFT = "rascunho"
    SCHEDULED = "agendado"
    PUBLISHED = "publicado"
    FAILED = "falhou"

class PostBase(BaseModel):
    topic: str
    caption: str

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: str
    image_path: str | None = None
    scheduled_at: datetime | None = None
    status: Status | None = Status.DRAFT
    created_at: datetime
    author_id: int

    model_config = {"from_attributes": True}

class PostUpdate(BaseModel):
    topic: str | None = None
    caption: str | None = None