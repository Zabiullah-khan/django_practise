import requests
import json

url='http://127.0.0.1:8000/student/student/1/'

fetchs= requests.get(url=url)
get_json = fetchs.json()
print(get_json)
