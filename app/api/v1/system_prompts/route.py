from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session

from app.api.v1.system_prompts.schema import (
    SystemPrompt,
    SystemPromptCreate,
    SystemPromptUpdate,
)
from app.api.v1.system_prompts.service import SystemPromptService
from app.dependencies.database import get_db

router = APIRouter()


@router.get(
    "/",
    response_model=List[SystemPrompt],
    summary="Get all system prompts",
    description="Retrieve all system prompts.",
)
def get_system_prompts(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    system_prompt_service: SystemPromptService = Depends(),
) -> Any:
    """
    Get all system prompts.

    - **skip**: Number of records to skip
    - **limit**: Maximum number of records to return
    """
    return system_prompt_service.get_system_prompts(db, skip=skip, limit=limit)


@router.get(
    "/{system_prompt_id}",
    response_model=SystemPrompt,
    summary="Get a specific system prompt",
    description="Retrieve a specific system prompt by ID.",
)
def get_system_prompt(
    system_prompt_id: int = Path(..., title="The ID of the system prompt to get"),
    db: Session = Depends(get_db),
    system_prompt_service: SystemPromptService = Depends(),
) -> Any:
    """
    Get a specific system prompt by ID.

    - **system_prompt_id**: ID of the system prompt
    """
    return system_prompt_service.get_system_prompt(
        db, system_prompt_id=system_prompt_id
    )


@router.post(
    "/",
    response_model=SystemPrompt,
    summary="Create a new system prompt",
    description="Create a new system prompt.",
)
def create_system_prompt(
    system_prompt_in: SystemPromptCreate,
    db: Session = Depends(get_db),
    system_prompt_service: SystemPromptService = Depends(),
) -> Any:
    """
    Create a new system prompt.

    - **name**: Name of the system prompt
    - **content**: Content of the system prompt
    - **description**: Optional description
    - **is_active**: Whether the system prompt is active
    """
    return system_prompt_service.create_system_prompt(
        db, system_prompt_in=system_prompt_in
    )


@router.put(
    "/{system_prompt_id}",
    response_model=SystemPrompt,
    summary="Update a system prompt",
    description="Update a system prompt.",
)
def update_system_prompt(
    *,
    system_prompt_id: int = Path(..., title="The ID of the system prompt to update"),
    system_prompt_in: SystemPromptUpdate,
    db: Session = Depends(get_db),
    system_prompt_service: SystemPromptService = Depends(),
) -> Any:
    """
    Update a system prompt.

    - **system_prompt_id**: ID of the system prompt
    - **name**: Name of the system prompt
    - **content**: Content of the system prompt
    - **description**: Optional description
    - **is_active**: Whether the system prompt is active
    """
    return system_prompt_service.update_system_prompt(
        db, system_prompt_id=system_prompt_id, system_prompt_in=system_prompt_in
    )


@router.delete(
    "/{system_prompt_id}",
    response_model=SystemPrompt,
    summary="Delete a system prompt",
    description="Delete a system prompt.",
)
def delete_system_prompt(
    system_prompt_id: int = Path(..., title="The ID of the system prompt to delete"),
    db: Session = Depends(get_db),
    system_prompt_service: SystemPromptService = Depends(),
) -> Any:
    """
    Delete a system prompt.

    - **system_prompt_id**: ID of the system prompt
    """
    return system_prompt_service.delete_system_prompt(
        db, system_prompt_id=system_prompt_id
    )
