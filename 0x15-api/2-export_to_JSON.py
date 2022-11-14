#!/usr/bin/python3
"""
1. Records all tasks that are owned by this employee
2. Format must be: { "USER_ID": [{"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, {"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, ... ]}
3. File name must be: USER_ID.json
"""
if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    url_user = "https://jsonplaceholder.typicode.com/users"
    url_todo = "https://jsonplaceholder.typicode.com/todos"
    final_dict = {}
    new_list = []
    i = 0
    name = ""
    req = requests.get(url_user, params={"id": argv[1]})
    name = req.json()[0].get("username")
    req = requests.get(url_todo, params={"userId": argv[1]})

    while i < len(req.json()):
        title = req.json()[i].get("title")
        completion = req.json()[i].get("completed")
        new_dict = {}
        new_dict["task"] = title
        new_dict["completed"] = completion
        new_dict["username"] = name
        new_list.append(new_dict)
        i += 1
    final_dict["{}".format(argv[1])] = new_list
    with open("{}.json".format(argv[1]), "w") as f:
        json.dump(final_dict, f)
