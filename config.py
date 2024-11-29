import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    TOKEN_KEY = os.environ.get("TOKEN_KEY")
    MONGODB_URI = os.environ.get("MONGODB_URI")
  
    DBNAME = os.environ.get("DB_NAME")

