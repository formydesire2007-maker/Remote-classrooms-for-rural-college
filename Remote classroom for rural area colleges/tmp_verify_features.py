import requests

base = 'http://127.0.0.1:5000'
print('health', requests.get(base + '/health').status_code)
print('chat', requests.post(base + '/api/chatbot/', json={'message': 'Explain photosynthesis', 'history': []}).json())
print('quiz', requests.post(base + '/api/quiz/', json={'topic': 'Photosynthesis', 'count': 2, 'difficulty': 'easy'}).json())
