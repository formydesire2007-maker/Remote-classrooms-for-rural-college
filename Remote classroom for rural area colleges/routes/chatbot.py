from flask import Blueprint, request, jsonify

from services.chatbot_service import get_chatbot_response


chatbot_bp = Blueprint(
    "chatbot",
    __name__
)


@chatbot_bp.route("/", methods=["POST"])
def chatbot():

    try:
        data = request.get_json()

        message = data.get("message", "")
        history = data.get("history", [])


        if not message:
            return jsonify({
                "error": "Message is required"
            }), 400


        reply = get_chatbot_response(
            message,
            history
        )


        return jsonify({
            "reply": reply
        })


    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500