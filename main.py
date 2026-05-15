import json
import os

tasks = []
with open(r"tasks.json", "r") as file:
    tasks = json.load(file)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def list_tasks (task_list):
    for task in task_list:
        print(f"{task_list.index(task) + 1} - {task}")

def add_task():
    task = input("Please write your task: ")
    tasks.append(task)

    with open(r"tasks.json", "w") as file:
        json.dump(tasks, file)
    
    input("Task added succefuly! Press enter to continue")

def delete_task():
    list_tasks(tasks)
    delete_selection = int(input("Plese select a task: "))
    deleted_task = tasks.pop(delete_selection - 1)
    with open(r"tasks.json","w") as file:
        json.dump(tasks, file)

    print(f"Succefuly deleted = '{deleted_task}'!")
    input("Press ENTER to continue")

while True:

    print("=== Todo CLI ===\n")
    print("1 - List Tasks")
    print("2 - Add task")
    print("3 - Delete task")
    print("0 - Exit")
    choice = input("\nPlease choose an option: ")

    if choice == "1":
        list_tasks(tasks)

    elif choice == "2":
        add_task()

    elif choice == "3":
        delete_task()
    
    else:
        break

