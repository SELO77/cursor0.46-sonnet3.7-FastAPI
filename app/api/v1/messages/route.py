from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.v1.messages.schema import Message, MessageCreate
from app.api.v1.messages.service import MessageService
from app.dependencies.database import get_db

router = APIRouter()


@router.post(
    "/",
    response_model=Message,
    summary="Create a new message",
    description="Generate text using OpenRouter API and store the message.",
)
async def create_message(
    message_in: MessageCreate,
    db: Session = Depends(get_db),
    message_service: MessageService = Depends(),
) -> Any:
    """
    Create a new message:

    - **model**: The model to use for text generation
    - **input_messages**: List of input messages
    - **system_prompt_id**: Optional system prompt ID
    - **metadata**: Optional metadata
    """
    return await message_service.create_message(db, message_in)
