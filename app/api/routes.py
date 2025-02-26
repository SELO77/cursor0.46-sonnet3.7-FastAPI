from fastapi import APIRouter

from app.api.endpoints import messages, system_prompts

api_router = APIRouter()

api_router.include_router(messages.router, prefix="/messages", tags=["messages"])
api_router.include_router(
    system_prompts.router, prefix="/system-prompts", tags=["system-prompts"]
)
