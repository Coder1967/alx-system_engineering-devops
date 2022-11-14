#!/usr/bin/python3
"""
1. Records all tasks that are owned by this employee
2. Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
3. File name must be: USER_ID.csv
"""
if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    i = 0
    params = {"id": argv[1]}
    req = requests.get("https://jsonplaceholder.typicode.com/users",
                       params=params)
    name = req.json()[0].get("username")
    req = requests.get("https://jsonplaceholder.typicode.com/todos",
                       params={"userId": argv[1]})

    with open('{}.csv'.format(argv[1]), 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        while i < len(req.json()):
            title = req.json()[i].get("title")
            status = req.json()[i].get("completed")
            writer.writerow([argv[1], name, status, title])
            i += 1
