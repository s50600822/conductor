import requests
import time

for x in range(0, 1):
	requests.post('http://localhost:8080/api/workflow/kitchensink', headers={'Content-type': 'application/json'},json={"task2Name": "task_5"})