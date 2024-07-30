#!/usr/bin/python3

""" Building upon task 0, this script exports the data to JSON format """

import json
import requests
import sys


def get_employee_info_and_tasks(employee_id):
    """ Exports the data into JSON format """

    api_url = 'https://jsonplaceholder.typicode.com/'

    user_url = '{}users/{}'.format(api_url, employee_id)
    todos_url = '{}todos?userId={}'.format(api_url, employee_id)

    user_response = requests.get(user_url)
    user_data = user_response.json()

    username = user_data.get('username')

    todos_response = requests.get(todos_url)
    tasks_data = todos_response.json()

    tasks_list = []
    for task in tasks_data:
        dict_task = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        }
        tasks_list.append(dict_task)

    employee_tasks = {str(employee_id): tasks_list}

    filename = '{}.json'.format(employee_id)
    with open(filename, mode='w') as json_file:
        json.dump(employee_tasks, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    get_employee_info_and_tasks(employee_id)
