from fastapi import APIRouter

router = APIRouter()


@router.get("/", summary="Health check", description="Check if the API is running")
async def health_check():
    """
    Health check endpoint.

    Returns:
        dict: A dictionary with status information
    """
    return {"status": "healthy"}
