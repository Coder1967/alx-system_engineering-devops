#!/usr/bin/python3
"""
1. Records all tasks from all employees
2. File name must be: todo_all_employees.json
"""
if __name__ == "__main__":
    import json
    import requests

    url_user = "https://jsonplaceholder.typicode.com/users"
    url_todo = "https://jsonplaceholder.typicode.com/todos"
    final_dict = {}
    new_list = []
    i = 1
    name = ""
    req = requests.get(url_user)
    users = len(req.json()) + 1

    while i <= users:
        j = 0
        new_list = []
        req = requests.get(url_todo, params={"userId": i})
        todos = len(req.json())
        while j < todos:
            req = requests.get(url_todo, params={"userId": i})
            title = req.json()[i].get("title")
            completion = req.json()[i].get("completed")
            req = requests.get(url_user, params={"id": i})
            name = req.json()[0].get("username")
            new_dict = {}
            new_dict["username"] = name
            new_dict["task"] = title
            new_dict["completed"] = completion
            new_list.append(new_dict)
            j += 1
        final_dict["{}".format(i)] = new_list
        i += 1

    with open("todo_all_employees.json", "w") as f:
        json.dump(final_dict, f)
