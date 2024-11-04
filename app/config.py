import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

class Settings:
    REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
    REPLICATE_API_URL = "https://api.replicate.com/v1/predictions"

settings = Settings()
print(settings.REPLICATE_API_TOKEN)
