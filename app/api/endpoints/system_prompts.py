from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.system_prompt import SystemPrompt
from app.schemas.system_prompt import SystemPrompt as SystemPromptSchema
from app.schemas.system_prompt import SystemPromptCreate, SystemPromptUpdate

router = APIRouter()


@router.get("/", response_model=List[SystemPromptSchema])
def read_system_prompts(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve system prompts.
    """
    system_prompts = db.query(SystemPrompt).offset(skip).limit(limit).all()
    return system_prompts


@router.post("/", response_model=SystemPromptSchema)
def create_system_prompt(
    *,
    db: Session = Depends(get_db),
    system_prompt_in: SystemPromptCreate,
) -> Any:
    """
    Create new system prompt.
    """
    system_prompt = SystemPrompt(
        name=system_prompt_in.name,
        content=system_prompt_in.content,
        description=system_prompt_in.description,
        is_active=system_prompt_in.is_active,
    )
    db.add(system_prompt)
    db.commit()
    db.refresh(system_prompt)
    return system_prompt


@router.get("/{id}", response_model=SystemPromptSchema)
def read_system_prompt(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """
    Get system prompt by ID.
    """
    system_prompt = db.query(SystemPrompt).filter(SystemPrompt.id == id).first()
    if not system_prompt:
        raise HTTPException(status_code=404, detail="System prompt not found")
    return system_prompt


@router.put("/{id}", response_model=SystemPromptSchema)
def update_system_prompt(
    *,
    db: Session = Depends(get_db),
    id: int,
    system_prompt_in: SystemPromptUpdate,
) -> Any:
    """
    Update a system prompt.
    """
    system_prompt = db.query(SystemPrompt).filter(SystemPrompt.id == id).first()
    if not system_prompt:
        raise HTTPException(status_code=404, detail="System prompt not found")

    update_data = system_prompt_in.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(system_prompt, field, value)

    db.add(system_prompt)
    db.commit()
    db.refresh(system_prompt)
    return system_prompt


@router.delete("/{id}", response_model=SystemPromptSchema)
def delete_system_prompt(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """
    Delete a system prompt.
    """
    system_prompt = db.query(SystemPrompt).filter(SystemPrompt.id == id).first()
    if not system_prompt:
        raise HTTPException(status_code=404, detail="System prompt not found")

    db.delete(system_prompt)
    db.commit()
    return system_prompt
