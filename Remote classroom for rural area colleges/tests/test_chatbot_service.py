from services import chatbot_service


def test_fallback_explanation_is_conversational_for_any_topic(monkeypatch):
    monkeypatch.setattr(chatbot_service, "ask_ai", lambda prompt: "AI Error: no key")

    response = chatbot_service.get_chatbot_response("tell me about python", [])

    assert "python" in response.lower()
    assert "programming" in response.lower() or "beginner" in response.lower()
    assert "example" in response.lower()
    assert "ask again" not in response.lower()
