import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")


AI_PROVIDER = os.getenv(
    "AI_PROVIDER",
    "openai"
)


def ask_ai(prompt):

    try:

        if AI_PROVIDER == "openai":
            return openai_response(prompt)

        elif AI_PROVIDER == "claude":
            return claude_response(prompt)

        elif AI_PROVIDER == "gemini":
            return gemini_response(prompt)

        else:
            return "AI provider not configured."

    except Exception as e:
        return f"AI Error: {str(e)}"


def _get_openai_key():
    key = os.getenv("OPENAI_API_KEY", "").strip()
    if not key:
        raise ValueError("OPENAI_API_KEY is not set. Please add your real OpenAI key to .env.")

    invalid_placeholders = [
        "your_openai_api_key_here",
        "your_actual_openai_api_key_here",
        "sk-proj-your",
        "sk-your",
        "sk-pub-",
        "sk-priv-",
        "placeholder",
    ]

    if any(token in key.lower() for token in invalid_placeholders):
        raise ValueError(
            "OPENAI_API_KEY is using a placeholder-style value. "
            "Replace it with a real key from https://platform.openai.com/account/api-keys."
        )

    return key


def openai_response(prompt):
    import openai

    api_key = _get_openai_key()

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are Vidya, an AI tutor for rural college students."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=1000,
            temperature=0.7
        )
        choice = response.choices[0]
        if hasattr(choice, "message"):
            return choice.message.content
        return getattr(choice, "text", "")
    except Exception:
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are Vidya, an AI tutor for rural college students."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=1000,
            temperature=0.7
        )
        choice = response.choices[0]
        if hasattr(choice, "message"):
            return choice.message["content"]
        return getattr(choice, "text", "")



def claude_response(prompt):

    import anthropic


    client = anthropic.Anthropic(
        api_key=os.getenv(
            "CLAUDE_API_KEY"
        )
    )


    response = client.messages.create(

        model="claude-3-5-sonnet-20241022",

        max_tokens=1000,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    return response.content[0].text



def gemini_response(prompt):

    import google.generativeai as genai


    genai.configure(
        api_key=os.getenv(
            "GEMINI_API_KEY"
        )
    )


    model = genai.GenerativeModel(
        "gemini-pro"
    )


    response = model.generate_content(
        prompt
    )


    return response.text