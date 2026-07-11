"""
Remote Classroom for Rural Colleges
Application Constants
"""


# Application Information

PROJECT_NAME = "Remote Classroom for Rural Colleges"

PROJECT_VERSION = "1.0.0"


# Supported Languages

ENGLISH = "en-IN"

TELUGU = "te-IN"



# AI Settings

DEFAULT_AI_MODEL = "gpt-4o-mini"

MAX_HISTORY_LENGTH = 20



# Quiz Settings

DEFAULT_QUIZ_COUNT = 5

QUIZ_LEVELS = [

    "easy",
    "medium",
    "hard"

]



# Upload Settings

ALLOWED_AUDIO_FORMATS = [

    "wav",
    "mp3",
    "ogg"

]


UPLOAD_FOLDER = "uploads"



# API Messages

ERROR_MESSAGE = {

    "missing_input":
        "Required input is missing",

    "server_error":
        "Something went wrong. Please try again",

    "success":
        "Operation completed successfully"

}