from flask import Blueprint, request, jsonify

from services.transcription import transcribe_audio


transcription_bp = Blueprint(
    "transcription",
    __name__
)


@transcription_bp.route("/", methods=["POST"])
def transcription():

    try:

        if "audio" not in request.files:

            return jsonify({
                "error": "Audio file required"
            }), 400



        audio_file = request.files["audio"]


        language = request.form.get(
            "language",
            "en-IN"
        )


        result = transcribe_audio(
            audio_file,
            language
        )


        return jsonify({
            "transcript": result
        })


    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500