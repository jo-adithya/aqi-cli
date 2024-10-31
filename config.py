from dotenv import load_dotenv
import os

load_dotenv()

WAQI_API_URL = os.getenv("WAQI_API_URL") or "https://api.waqi.info"
WAQI_API_TOKEN = os.getenv("WAQI_API_TOKEN")
