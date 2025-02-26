from fastapi import FastAPI

from app.api.v1.route import api_router
from app.core.config import settings
from app.core.exceptions import add_exception_handlers
from app.db.base import create_tables
from app.middleware.cors import setup_cors

# 데이터베이스 테이블 생성
# create_tables()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# CORS 미들웨어 설정
setup_cors(app)

# 예외 핸들러 추가
add_exception_handlers(app)

# API 라우터 포함
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
def root():
    """
    Root endpoint for health check
    """
    return {
        "status": "ok",
        "message": "AI Text Microservice API is running",
        "version": "1.0.0",
    }
