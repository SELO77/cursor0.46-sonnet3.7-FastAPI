from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field


# Chat message format
class ChatMessage(BaseModel):
    role: str
    content: str


# Shared properties
class MessageBase(BaseModel):
    model: str
    input_messages: List[ChatMessage]
    system_prompt_id: Optional[int] = None
    metadata: Optional[Dict[str, Any]] = None


# Properties to receive on item creation
class MessageCreate(MessageBase):
    pass


# Properties shared by models stored in DB
class MessageInDBBase(MessageBase):
    id: int
    request_id: str
    generated_text: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


# Properties to return to client
class Message(MessageInDBBase):
    pass


# Properties properties stored in DB
class MessageInDB(MessageInDBBase):
    pass


# OpenRouter request format
class OpenRouterRequest(BaseModel):
    model: str
    messages: List[ChatMessage]
    max_tokens: Optional[int] = None
    temperature: Optional[float] = 0.7
    top_p: Optional[float] = 0.9
    stream: bool = False


# OpenRouter response format
class OpenRouterResponse(BaseModel):
    id: str
    choices: List[Dict[str, Any]]
    created: int
    model: str
    object: str
    usage: Dict[str, int]
