import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent
load_dotenv(PROJECT_ROOT / ".env")


class Config:

    # Flask settings
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "remote-classroom-secret"
    )

    DEBUG = True

    # AI API settings
    AI_PROVIDER = os.getenv(
        "AI_PROVIDER",
        "openai"
    )

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
    CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY", "").strip()
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

    # Database
    DATABASE = os.getenv("DATABASE", str(PROJECT_ROOT / "database" / "classroom.db"))

    # Upload folders
    UPLOAD_FOLDER = str(PROJECT_ROOT / "uploads")
