from typing import List, Optional

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.api.v1.system_prompts.model import SystemPrompt
from app.api.v1.system_prompts.schema import SystemPromptCreate, SystemPromptUpdate
from app.core.exceptions import AppException


class SystemPromptService:
    def get_system_prompts(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> List[SystemPrompt]:
        """
        Get all system prompts.
        """
        return db.query(SystemPrompt).offset(skip).limit(limit).all()

    def get_system_prompt(self, db: Session, system_prompt_id: int) -> SystemPrompt:
        """
        Get a specific system prompt by ID.
        """
        system_prompt = (
            db.query(SystemPrompt).filter(SystemPrompt.id == system_prompt_id).first()
        )
        if not system_prompt:
            raise AppException(
                status_code=404,
                detail=f"System prompt with ID {system_prompt_id} not found",
                code="system_prompt_not_found",
            )
        return system_prompt

    def create_system_prompt(
        self, db: Session, system_prompt_in: SystemPromptCreate
    ) -> SystemPrompt:
        """
        Create a new system prompt.
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

    def update_system_prompt(
        self, db: Session, system_prompt_id: int, system_prompt_in: SystemPromptUpdate
    ) -> SystemPrompt:
        """
        Update a system prompt.
        """
        system_prompt = self.get_system_prompt(db, system_prompt_id)

        update_data = system_prompt_in.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(system_prompt, field, value)

        db.add(system_prompt)
        db.commit()
        db.refresh(system_prompt)
        return system_prompt

    def delete_system_prompt(self, db: Session, system_prompt_id: int) -> SystemPrompt:
        """
        Delete a system prompt.
        """
        system_prompt = self.get_system_prompt(db, system_prompt_id)
        db.delete(system_prompt)
        db.commit()
        return system_prompt
