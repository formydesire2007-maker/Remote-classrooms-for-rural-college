from flask import Blueprint, request, jsonify

from services.quiz_service import generate_quiz


quiz_bp = Blueprint(
    "quiz",
    __name__
)


@quiz_bp.route("/", methods=["POST"])
def quiz_generator():

    try:

        data = request.get_json()


        topic = data.get(
            "topic",
            ""
        )

        count = data.get(
            "count",
            5
        )

        difficulty = data.get(
            "difficulty",
            "medium"
        )


        if not topic:

            return jsonify({
                "error": "Topic is required"
            }), 400



        result = generate_quiz(
            topic,
            count,
            difficulty
        )


        return jsonify({
            "quiz": result
        })


    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500