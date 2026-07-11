from services.ai_client import ask_ai


def generate_quiz(topic, count, difficulty):
    prompt = f"""
Create a {difficulty} level quiz.

Topic:
{topic}

Number of questions:
{count}

Format:

Question:
A)
B)
C)
D)

Correct Answer:
Explanation:
"""

    try:
        quiz = ask_ai(prompt)
        cleaned = str(quiz).strip()
        if cleaned and not cleaned.lower().startswith("ai error"):
            return cleaned
    except Exception:
        pass

    count_value = max(1, int(count)) if str(count).isdigit() else 5
    questions = []
    for i in range(1, count_value + 1):
        questions.append(
            f"{i}. What is an important concept related to {topic}?\nA. Definition\nB. Example\nC. Summary\nD. Practice\nCorrect Answer: A\nExplanation: Review the main idea of {topic}."
        )
    return "\n\n".join(questions)