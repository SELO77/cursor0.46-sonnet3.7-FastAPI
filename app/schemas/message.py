from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    role: str
    content: str


class OpenRouterRequest(BaseModel):
    model: str
    messages: List[Dict[str, str]]
    max_tokens: Optional[int] = None
    temperature: float = 0.7
    top_p: float = 0.9
    stream: bool = False


class OpenRouterResponseChoice(BaseModel):
    message: Dict[str, str]
    index: int
    finish_reason: Optional[str] = None


class OpenRouterResponseUsage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class OpenRouterResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: List[Union[Dict[str, Any], OpenRouterResponseChoice]]
    usage: Optional[Union[Dict[str, int], OpenRouterResponseUsage]] = None
