from dotenv import load_dotenv
import os

load_dotenv()

HUNTER_API_KEY = os.getenv("HUNTER_API_KEY")
WAPPALYZER_API_KEY = os.getenv("WAPPALYZER_API_KEY")