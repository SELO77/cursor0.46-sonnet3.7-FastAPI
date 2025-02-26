from typing import Any, Dict, List

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.message import Message
from app.models.system_prompt import SystemPrompt
from app.schemas.message import ChatMessage
from app.schemas.message import Message as MessageSchema
from app.schemas.message import MessageCreate
from app.services.openrouter import openrouter_service

router = APIRouter()


@router.post("/", response_model=MessageSchema)
async def create_message(
    *,
    db: Session = Depends(get_db),
    message_in: MessageCreate,
) -> Any:
    """
    Generate text using OpenRouter API.
    """
    # Generate a unique request ID
    request_id = openrouter_service.generate_request_id()

    # Get system prompt if provided
    system_prompt = None
    if message_in.system_prompt_id:
        system_prompt = (
            db.query(SystemPrompt)
            .filter(
                SystemPrompt.id == message_in.system_prompt_id,
                SystemPrompt.is_active == True,
            )
            .first()
        )

        if not system_prompt:
            raise HTTPException(
                status_code=404,
                detail=f"System prompt with ID {message_in.system_prompt_id} not found or inactive",
            )

    # Prepare messages for OpenRouter
    openrouter_messages = []

    # Add system prompt if available
    if system_prompt:
        openrouter_messages.append(
            ChatMessage(role="system", content=system_prompt.content)
        )

    # Add user messages
    openrouter_messages.extend(message_in.input_messages)

    # Create message record in DB
    message = Message(
        request_id=request_id,
        model=message_in.model,
        input_messages=message_in.input_messages,
        system_prompt_id=message_in.system_prompt_id,
        metadata=message_in.metadata,
    )
    db.add(message)
    db.commit()

    try:
        # Call OpenRouter API
        response = await openrouter_service.generate_text(
            model=message_in.model,
            messages=openrouter_messages,
        )

        # Extract generated text
        generated_text = openrouter_service.extract_generated_text(response)

        # Update message with generated text
        message.generated_text = generated_text
        db.add(message)
        db.commit()
        db.refresh(message)

        return message
    except Exception as e:
        # Handle errors
        db.refresh(message)
        raise HTTPException(
            status_code=500,
            detail=f"Error generating text: {str(e)}",
        )
