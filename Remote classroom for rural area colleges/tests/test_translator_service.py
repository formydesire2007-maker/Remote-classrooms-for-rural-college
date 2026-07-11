import pytest

from services import translator_service


@pytest.mark.parametrize(
    ("text", "direction", "expected"),
    [
        ("hello priya", "en-te", "నమస్తే ప్రియా"),
        ("how are you", "en-te", "మీరు ఎలా ఉన్నారు"),
        ("students are studying in the library", "en-te", "విద్యార్థులు లైబ్రరీలో చదువుతున్నారు"),
        ("the weather is very hot today", "en-te", "ఈరోజు వాతావరణం చాలా వేడిగా ఉంది"),
        ("please submit your assignment before Friday", "en-te", "దయచేసి మీ అసైన్మెంట్‌ను శుక్రవారానికి ముందు సమర్పించండి"),
        ("my name is raju and i am from hyderabad", "en-te", "నా పేరు రాజు మరియు నేను హైదరాబాదుకు చెందినవాణి"),
        ("we will have a science exam next week", "en-te", "మేము próxima వారం సైన్స్ పరీక్షకు సిద్ధమవుతాము"),
        ("the teacher explained the lesson clearly", "en-te", "అధ్యాపకుడు పాఠాన్ని స్పష్టంగా వివరించారు"),
        ("this is a long paragraph for testing translation quality and natural Telugu", "en-te", "ఇది అనువాద నాణ్యత మరియు సహజమైన తెలుగు కోసం పరీక్షించడానికి ఒక దీర్ఘ పేరా"),
        ("I love learning computer science and artificial intelligence", "en-te", "నేను కంప్యూటర్ సైన్స్ మరియు కృత్రిమ మేధస్సు నేర్చుకోవడం ఇష్టపడతాను"),
    ],
)
def test_translates_multiple_english_sentences_to_telugu(monkeypatch, text, direction, expected):
    monkeypatch.setattr(translator_service, "ask_ai", lambda prompt: expected)

    response = translator_service.translate_text(text, direction)

    assert response == expected


def test_returns_meaningful_error_when_translation_fails(monkeypatch):
    def broken_ai(prompt):
        raise RuntimeError("simulated api failure")

    monkeypatch.setattr(translator_service, "ask_ai", broken_ai)

    response = translator_service.translate_text("hello", "en-te")

    assert response and response.lower() != "hello"
