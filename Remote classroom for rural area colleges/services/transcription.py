import speech_recognition as sr


def transcribe_audio(audio_file, language):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio, language=language)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except Exception as e:
        return f"Transcription unavailable: {str(e)}"
