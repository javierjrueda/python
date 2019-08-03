import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/javierjrueda/python")
todos = json.loads(response.text)

todos == response.json()

type(todos)

