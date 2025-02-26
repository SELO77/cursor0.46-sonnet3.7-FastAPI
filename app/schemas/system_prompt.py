from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class SystemPromptBase(BaseModel):
    name: str
    content: str
    description: Optional[str] = None
    is_active: bool = True


# Properties to receive on item creation
class SystemPromptCreate(SystemPromptBase):
    pass


# Properties to receive on item update
class SystemPromptUpdate(SystemPromptBase):
    name: Optional[str] = None
    content: Optional[str] = None
    is_active: Optional[bool] = None


# Properties shared by models stored in DB
class SystemPromptInDBBase(SystemPromptBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Properties to return to client
class SystemPrompt(SystemPromptInDBBase):
    pass


# Properties properties stored in DB
class SystemPromptInDB(SystemPromptInDBBase):
    pass
