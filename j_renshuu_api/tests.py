from requests import get, post, put, delete


SERVER = 'http://localhost:8000/'

response = get(SERVER + 'categories/')
print(response.json())

response = get(SERVER + 'words/')
print(response.json())