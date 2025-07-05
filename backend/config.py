# backend/config.py

import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DB_URL = os.getenv("DB_URL", "sqlite:///neurospect.db")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 800))
ENV = os.getenv("ENV", "dev")
DEBUG = os.getenv("DEBUG", "True") == "True"

# Sanity check
assert OPENAI_API_KEY, "Missing OPENAI_API_KEY in environment!"