import json
import logging
import requests

from services.ai_client import ask_ai


logger = logging.getLogger(__name__)


def _extract_translation(response):
    if response is None:
        return ""

    if isinstance(response, (dict, list)):
        try:
            return str(json.dumps(response))
        except Exception:
            return str(response)

    text = str(response).strip()
    if not text:
        return ""

    if text.startswith("```"):
        text = text.strip("`").strip()

    if "translation" in text.lower() and ":" in text:
        parts = text.split(":", 1)
        text = parts[1].strip()

    if text.startswith("\"") and text.endswith("\""):
        text = text[1:-1]
    if text.startswith("'") and text.endswith("'"):
        text = text[1:-1]

    return text.strip()


def _get_translation_prompt(text, direction):
    if direction == "en-te":
        return (
            "You are a professional English to Telugu translator. "
            "Translate any English text into clear, natural, grammatically correct Telugu. "
            "Preserve names, numbers, and proper nouns unless they have a standard Telugu form. "
            "Return only the Telugu translation with no explanation or additional text.\n\n"
            f"Text: {text}"
        )

    return (
        "You are a professional English to Telugu translator. "
        "Translate any English text into clear, natural, grammatically correct Telugu. "
        "Preserve names, numbers, and proper nouns unless they have a standard Telugu form. "
        "Return only the Telugu translation with no explanation or additional text.\n\n"
        f"Text: {text}"
    )


def translate_text(text, direction):
    cleaned_text = " ".join(str(text or "").split())
    if not cleaned_text:
        return "Please provide some text to translate."

    prompt = _get_translation_prompt(cleaned_text, direction)

    try:
        result = ask_ai(prompt)
        translated = _extract_translation(result)
        if translated and not translated.lower().startswith("ai error"):
            return translated
    except Exception as exc:
        logger.exception("Translator AI request failed: %s", exc)

    try:
        response = requests.get(
            "https://api.mymemory.translated.net/get",
            params={
                "q": cleaned_text,
                "langpair": "en|te" if direction == "en-te" else "te|en",
            },
            timeout=20,
        )
        response.raise_for_status()
        payload = response.json()
        translated = payload.get("responseData", {}).get("translatedText")
        if translated:
            return translated
    except Exception as exc:
        logger.exception("Translator fallback API request failed: %s", exc)

    return "Translation could not be completed because the AI service is unavailable right now. Please try again shortly."
