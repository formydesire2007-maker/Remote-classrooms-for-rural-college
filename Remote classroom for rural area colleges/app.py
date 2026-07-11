import os
import sqlite3
from pathlib import Path

from flask import Flask, render_template
from flask_cors import CORS
from dotenv import load_dotenv

from models import db
from routes.chatbot import chatbot_bp
from routes.quiz import quiz_bp
from routes.translator import translator_bp
from routes.transcription import transcription_bp
from models.user import User

PROJECT_ROOT = Path(__file__).resolve().parent
load_dotenv(PROJECT_ROOT / ".env")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "remote-classroom-secret")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{(PROJECT_ROOT / 'database' / 'classroom.db').resolve()}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = str(PROJECT_ROOT / "uploads")

# Allow frontend requests
CORS(app)
db.init_app(app)

# Register API routes
app.register_blueprint(chatbot_bp, url_prefix="/api/chatbot")
app.register_blueprint(quiz_bp, url_prefix="/api/quiz")
app.register_blueprint(translator_bp, url_prefix="/api/translate")
app.register_blueprint(transcription_bp, url_prefix="/api/transcription")


def init_database():
    db_dir = PROJECT_ROOT / "database"
    db_dir.mkdir(exist_ok=True)

    with app.app_context():
        db.create_all()

        schema_path = PROJECT_ROOT / "database" / "schema.sql"
        if schema_path.exists():
            db_path = Path(app.config["SQLALCHEMY_DATABASE_URI"].replace("sqlite:///", "", 1))
            conn = sqlite3.connect(str(db_path))
            try:
                with schema_path.open("r", encoding="utf-8") as handle:
                    conn.executescript(handle.read())
                conn.commit()
            finally:
                conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return {
        "status": "running",
        "message": "Remote Classroom Backend is active"
    }


init_database()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

    