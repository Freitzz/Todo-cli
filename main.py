import json
import os

tasks = []
with open(r"tasks.json", "r") as file:
    tasks = json.load(file)

def list_tasks (task_list):
    for task in task_list:
        print(f"{task_list.index(task) + 1} - {task}")

while True:

    print("=== Todo CLI ===\n")
    print("1 - List Tasks")
    print("2 - Add task")
    print("3 - Delete task")
    print("0 - Exit")
    choice = input("\nPlease choose an option: ")

    if choice == "1":
        list_tasks(tasks)
    
    else:
        break

