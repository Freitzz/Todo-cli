import json
import os

tasks = []
with open(r"tasks.json", "r") as file:
    tasks = json.load(file)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress ENTER to continue")

def list_tasks (task_list):
    clear()
    print("=== Tasks List ===\n")

    if len(tasks) == 0:
        print("There are no tasks")
    else:
        for task in task_list:
            print(f"{task_list.index(task) + 1} - {task}")
    

def add_task():
    clear()
    print("=== Add Task ===\n")
    task = input("Please write your task: ")
    tasks.append(task)

    with open(r"tasks.json", "w") as file:
        json.dump(tasks, file)
    
    print(f"\n'{task}', added succefuly!")

def delete_task():
    if len(tasks) == 0:
        print("\nThere are no tasks to delete.")
    
    else:
        list_tasks(tasks)
        print("0 - Exit")
        while True:
            try:
                delete_selection = int(input("\nPlese select a task: "))
            except ValueError:
                print("Please choose a valid task number!")
            
            else:
            
                if delete_selection < 0 or delete_selection > len(tasks):
                    print("Please choose a valid task number!")
                    continue
                else:
                    
                    if delete_selection == 0:
                        print("\nNo tasks deleted!")
                        break
                    else:
                        deleted_task = tasks.pop(delete_selection - 1)
                        with open(r"tasks.json","w") as file:
                            json.dump(tasks, file)

                        print(f"\nSuccefuly deleted = '{deleted_task}'!")
                        break

#menu 
while True:
    
    clear()
    print("=== Todo CLI ===\n")
    print("1 - List Tasks")
    print("2 - Add task")
    print("3 - Delete task")
    print("0 - Exit")
    choice = input("\nPlease choose an option: ")

    if choice == "1":
        list_tasks(tasks)
        pause()

    elif choice == "2":
        add_task()
        pause()

    elif choice == "3":
        delete_task()
        pause()
    
    else:
        break

