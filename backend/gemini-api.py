from google import genai
from app.core.config import settings

client = genai.Client(api_key=settings.gemini_api_key)

response = client.models.generate_content(
    model="models/gemini-3.6-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)