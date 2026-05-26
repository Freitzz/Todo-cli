import sqlite3
import os

BASE_DIR = os.path.dirname(__file__)
TASK_DB = os.path.join(BASE_DIR, "todo.db")

connection = sqlite3.connect(TASK_DB)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               task TEXT,
               priority INTEGER,
               completed INTEGER
               )
""")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress ENTER to continue")

def list_tasks ():
    clear()
    cursor.execute("SELECT * FROM tasks;")
    task_list = cursor.fetchall()

    print(task_list)

def add_task():
    clear()
    print("=== Add Task ===\n")
    task = input("Please write your task: ")
    task_priority = input("Please insert task priority: ")
    task_completed = 0

    cursor.execute("""
    INSERT INTO tasks(task, priority, completed)
    VALUES (?,?,?)
    """, (task, task_priority, task_completed))
    
    print(f"\n'{task}', added succefuly with {task_priority} priority!")

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
                        with open(TASK_FILE,"w") as file:
                            json.dump(tasks, file)

                        print(f"\nSuccefuly deleted = '{deleted_task}'!")
                        break

#menu 
while True:
    
    clear()
    print("==== This is a test branch ====\n")
    print("=== Todo CLI ===\n")
    print("1 - List Tasks")
    print("2 - Add task")
    print("3 - Delete task")
    print("0 - Exit")
    choice = input("\nPlease choose an option: ")

    if choice == "1":
        list_tasks()
        pause()

    elif choice == "2":
        add_task()
        pause()

    elif choice == "3":
        delete_task()
        pause()
    
    else:
        break

connection.commit()
connection.close()
