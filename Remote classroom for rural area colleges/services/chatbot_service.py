from services.ai_client import ask_ai


def get_chatbot_response(message, history):
    prompt = f"""
You are Vidya, an AI tutor helping rural college students.

Conversation history:
{history}

Student question:
{message}

Explain clearly with simple examples.
Support English and Telugu if needed.
"""

    try:
        response = ask_ai(prompt)
        cleaned = str(response).strip()
        if cleaned and not cleaned.lower().startswith("ai error"):
            return cleaned
    except Exception:
        pass

    lower_message = (message or "").strip().lower()

    if not lower_message:
        return "I can help with academic questions. Please ask me something like 'explain photosynthesis' or 'tell me about Python'."

    if "formula" in lower_message or "solve" in lower_message or "calculate" in lower_message:
        return "I can help with step-by-step explanations. For now, here is a simple guide: identify the given values, choose the correct formula, substitute carefully, and simplify the result."

    if any(word in lower_message for word in ["telugu", "తెలుగు", "language", "grammar", "exam"]):
        return "I can explain concepts in simple English and Telugu. For example, 'What is photosynthesis?' can be answered as: Photosynthesis is the process by which plants make food using sunlight, water, and carbon dioxide."

    if "python" in lower_message:
        return "Python is a beginner-friendly programming language used for web development, automation, data science, AI, and scripting. A simple example is: print('Hello') which displays text on the screen."

    if "database" in lower_message or "sql" in lower_message:
        return "A database stores and organizes data. SQL is used to create, read, update, and delete records. For example, SELECT * FROM students shows all student records."

    if "html" in lower_message or "css" in lower_message or "javascript" in lower_message:
        return "HTML gives structure to a web page, CSS styles it, and JavaScript makes it interactive. Together, they build modern websites."

    if "flask" in lower_message:
        return "Flask is a lightweight Python web framework used to build web applications and APIs. It is simple to learn and popular for small and medium projects."

    topic = (message or "").strip()
    if any(word in lower_message for word in ["what", "why", "how", "explain", "define", "tell me about", "who", "can you", "do you know", "describe"]):
        return f"{topic} is an important topic. In simple terms, it means understanding the main idea, the key features, and one practical example so it becomes easier to learn."

    if len(topic.split()) <= 3:
        return f"{topic.capitalize()} is a useful topic to learn. I can explain it in simple steps, give a clear example, and help you understand it better."

    return f"Here is a helpful explanation for '{topic}': it becomes easier to understand when you learn the main idea, key points, and one simple example."