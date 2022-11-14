#!/usr/bin/python3
"""
1. Records all tasks from all employees
2. File name must be: todo_all_employees.json
"""
if __name__ == "__main__":
    import json
    import requests
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as f:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, f)
