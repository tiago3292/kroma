from google import genai
from app.core.config import settings

client = genai.Client(api_key=settings.gemini_api_key)

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Explain how AI works in a few words",
)

assert response.text