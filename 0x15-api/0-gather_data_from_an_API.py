#!/usr/bin/python3
"""
script must display on the standard
output the employee TODO list progress in the exact format:
Employee EMPLOYEE_NAME is done with
tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
"""
import requests
from sys import argv

i = 0
name = ""
total = 0
complete = 0

req = requests.get("https://jsonplaceholder.typicode.com/users",
                   params={"id": argv[1]})
name = req.json()[0]["name"]
req = requests.get("https://jsonplaceholder.typicode.com/todos",
                   params={"userId": argv[1], "completed": "true"})
complete = len(req.json())
req = requests.get("https://jsonplaceholder.typicode.com/todos",
                   params={"userId": argv[1]})
total = len(req.json())
print("Employee {} is done with tasks({:d}/{:d}):".format(
        name, complete, total))
while i < len(req.json()):
    print("\t {}".format(req.json()[i]["title"]))
    i += 1
