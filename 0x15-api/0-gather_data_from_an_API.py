#!/usr/bin/python3
"""
A python script that returns information about an employee's TODO list
progress using the REST API and the employee's ID
"""

import requests
from sys import argv


def display_progress():
    """ Display TODO list progress """

    users = requests.get("http://jsonplaceholder.typicode.com/users")

    for user in users.json():
        if user.get('id') == int(argv[1]):
            employee_name = (user.get('name'))
            break

    total_tasks = 0
    done_tasks = 0
    todo_data = []

    todos = requests.get("http://jsonplaceholder.typicode.com/todos")

    for todo in todos.json():
        if todo.get('userId') == int(argv[1]):
            total_tasks += 1
            if todo.get('completed') is True:
                done_tasks += 1
                todo_data.append(todo.get('title'))

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done_tasks, total_tasks))

    for task in todo_data:
        print("\t {}".format(task))


if __name__ == "__main__":
    display_progress()
