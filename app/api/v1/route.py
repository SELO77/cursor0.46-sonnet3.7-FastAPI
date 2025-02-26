from fastapi import APIRouter

from app.api.v1.health.route import router as health_router
from app.api.v1.messages.route import router as messages_router
from app.api.v1.system_prompts.route import router as system_prompts_router

api_router = APIRouter()

api_router.include_router(messages_router, prefix="/messages", tags=["messages"])
api_router.include_router(
    system_prompts_router, prefix="/system-prompts", tags=["system-prompts"]
)
api_router.include_router(health_router, prefix="/health", tags=["health"])
