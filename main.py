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

def delete_task(task_id):
    cursor.execute("""
    DELETE FROM tasks
    WHERE id = (?)
    """, (task_id,))

def complete_task(task_id):
    cursor.execute("""
    UPDATE tasks
    SET completed = 1
    WHERE id = (?)
""", (task_id))

#menu 
while True:
    
    clear()
    print("==== This is a test branch ====\n")
    print("=== Todo CLI ===\n")
    print("1 - List Tasks")
    print("2 - Add task")
    print("3 - Complete task")
    print("4 - Delete task")
    print("0 - Save and Exit")
    choice = input("\nPlease choose an option: ")

    if choice == "1":
        list_tasks()
        pause()

    elif choice == "2":
        add_task()
        pause()

    elif choice == "4":
        list_tasks()
        selected_task = int(input("Please select a task to delete: "))
                
        delete_task(selected_task)
        print("Task delete successfully")
        pause()
    
    elif choice == "0":
        connection.commit()
        connection.close()
        break
    
    else:
        break

