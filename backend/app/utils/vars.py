from dotenv import load_dotenv
import os

load_dotenv()

DB_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
DB_USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME")
DB_NAME = os.getenv("MONGO_INITDB_DATABASE")

HUNTER_API_KEY = os.getenv("HUNTER_API_KEY")