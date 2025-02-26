import uuid
from typing import Any, Dict, List, Optional

import httpx

from app.core.config import settings
from app.schemas.message import ChatMessage, OpenRouterRequest, OpenRouterResponse


class OpenRouterService:
    def __init__(self):
        self.api_key = settings.OPENROUTER_API_KEY
        self.base_url = settings.OPENROUTER_BASE_URL
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "https://ai-text-microservice",  # Optional
            "X-Title": "AI Text Microservice",  # Optional
        }

    async def generate_text(
        self,
        model: str,
        messages: List[ChatMessage],
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        top_p: float = 0.9,
    ) -> Dict[str, Any]:
        """
        Generate text using OpenRouter API
        """
        # Ensure model is valid or use default
        if model not in settings.AVAILABLE_MODELS:
            model = settings.DEFAULT_MODEL

        # Prepare request
        request_data = OpenRouterRequest(
            model=model,
            messages=[msg.dict() for msg in messages],
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            stream=False,
        )

        # Make API call
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=request_data.dict(),
                timeout=60.0,
            )

            if response.status_code != 200:
                raise Exception(f"OpenRouter API error: {response.text}")

            return response.json()

    def extract_generated_text(self, response: Dict[str, Any]) -> str:
        """
        Extract generated text from OpenRouter response
        """
        try:
            # Parse response
            openrouter_response = OpenRouterResponse(**response)

            # Extract text from first choice
            if openrouter_response.choices and len(openrouter_response.choices) > 0:
                return (
                    openrouter_response.choices[0].get("message", {}).get("content", "")
                )

            return ""
        except Exception as e:
            print(f"Error extracting text: {e}")
            return ""

    def generate_request_id(self) -> str:
        """
        Generate a unique request ID
        """
        return str(uuid.uuid4())


# Create a singleton instance
openrouter_service = OpenRouterService()
