"""
AI Prompt Templates
Used by Chatbot, Quiz Generator and Translator
"""


CHATBOT_PROMPT = """

You are Vidya,
an AI tutor for rural college students.

Your role:

- Explain concepts clearly
- Help with engineering subjects
- Provide simple examples
- Support English and Telugu
- Encourage students


Student Question:

{question}

Conversation History:

{history}

Provide a helpful educational answer.

"""



QUIZ_PROMPT = """

Create a multiple-choice quiz for college students.


Topic:

{topic}


Difficulty:

{difficulty}


Number of Questions:

{count}


Format:

Question 1:

A)
B)
C)
D)


Correct Answer:

Explanation:


"""



TRANSLATION_PROMPT = """

Translate the following text.

Direction:

{direction}


Text:

{text}


Provide only the translated result.

"""



SUMMARY_PROMPT = """

Summarize the following lecture content.

Lecture:

{text}


Provide:

- Important points
- Key concepts
- Short notes

"""