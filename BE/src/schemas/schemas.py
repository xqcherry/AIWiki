from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class DocusModel(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="文档标题")
    content: str = Field(default="", description="Markdown 内容")

class DocusCreate(DocusModel):
    pass

class DocusUpdate(DocusModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    content: Optional[str] = None

class DocusResponse(DocusModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True