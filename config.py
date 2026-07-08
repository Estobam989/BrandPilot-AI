
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def get_secret(key, default=None):
    """Read from Streamlit secrets first, then fall back to environment variables."""
    try:
        return st.secrets[key]
    except Exception:
        return os.getenv(key, default)

# AI
GROQ_API_KEY = get_secret("GROQ_API_KEY")
MODEL_NAME = get_secret("MODEL_NAME", "llama-3.3-70b-versatile")
TEMPERATURE = float(get_secret("TEMPERATURE", 0.7))
MAX_TOKENS = int(get_secret("MAX_TOKENS", 4096))

# Database
DATABASE_URL = get_secret("DATABASE_URL", "sqlite:///brandpilot.db")

# Social Media
FACEBOOK_ACCESS_TOKEN = get_secret("FACEBOOK_ACCESS_TOKEN", "")
INSTAGRAM_ACCESS_TOKEN = get_secret("INSTAGRAM_ACCESS_TOKEN", "")
LINKEDIN_ACCESS_TOKEN = get_secret("LINKEDIN_ACCESS_TOKEN", "")
X_ACCESS_TOKEN = get_secret("X_ACCESS_TOKEN", "")

# Hugging Face
HF_TOKEN = get_secret("HF_TOKEN", "")

# App
APP_NAME = "BrandPilot AI"
APP_VERSION = "1.0.0"
DEBUG = str(get_secret("DEBUG", "True")).lower() == "true"
