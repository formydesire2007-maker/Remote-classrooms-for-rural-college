from flask import Blueprint, request, jsonify

from services.translator_service import translate_text


translator_bp = Blueprint(
    "translator",
    __name__
)


@translator_bp.route("/", methods=["POST"])
def translator():
    try:
        data = request.get_json(silent=True) or {}

        text = data.get("text", "")
        direction = data.get("direction", "en-te")

        if not text or not str(text).strip():
            return jsonify({"error": "Text is required"}), 400

        translated = translate_text(text, direction)

        if translated and not translated.lower().startswith("translation could not be completed"):
            return jsonify({"translation": translated})

        return jsonify({"error": translated}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500