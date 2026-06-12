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

priority_map = {
    1: "Low",
    2: "Medium",
    3: "High"
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress ENTER to continue")

def list_tasks ():
    cursor.execute("SELECT * FROM tasks;")
    task_list = cursor.fetchall()

    for task in task_list:
        if task[3] == 0:
            print(f"Id: {task[0]} - '{task[1]}' - {priority_map[task[2]]} priority - Not completed.")
        elif task[3] == 1:
            print(f"Id: {task[0]} - '{task[1]}' - {priority_map[task[2]]} priority - Completed.")


def list_uncompleted_tasks():
    cursor.execute("""SELECT * FROM tasks
                   WHERE completed = 0;                   
                   """)
    task_list = cursor.fetchall()

    for task in task_list:
        print(f"Id: {task[0]} - '{task[1]}' - {priority_map[task[2]]} priority - Not completed.")

def add_task():
    clear()
    print("=== Add Task ===\n")
    task = input("Please write your task: ")
    task_priority = 1
    while True:
        try:
            task_priority = int(input("Please insert task priority:\n(1, 2 or 3)\n"))
        except ValueError:
            clear()
            print("Please insert a valid integer!")
        else:
            if task_priority < 1 or task_priority > 3:
                clear()
                print("Please insert between 1, 2 or 3!")
            else:
                break

    task_completed = 0

    cursor.execute("""
    INSERT INTO tasks(task, priority, completed)
    VALUES (?,?,?)
    """, (task, task_priority, task_completed))
    
    print(f"\n'{task}', added succefuly with {priority_map[task_priority]} priority!")

def delete_task(task_id):
    cursor.execute("""
    DELETE FROM tasks
    WHERE id = (?)
    """, (task_id,))

#returns true of false
def complete_task(task_id):
    cursor.execute("""
    UPDATE tasks
    SET completed = 1
    WHERE id = (?);
    """, (task_id,))

def task_exists(task_id):
    cursor.execute("""
                    SELECT * FROM tasks
                    WHERE id = (?);
                    """, (task_id,))
    task = cursor.fetchall()               
    if task == []:
        return False
    else:
        return True

#menu 
while True:
    
    clear()
    print("==== This is a test branch ====\n")
    print("=== Todo CLI ===\n")
    print("1 - List all tasks")
    print("2 - Add task")
    print("3 - Complete task")
    print("4 - Delete task")
    print("0 - Save and Exit")
    choice = input("\nPlease choose an option: ")

    #list all tasks
    if choice == "1":
        clear()
        print("=== Tasks list ===\n")
        list_tasks()
        pause()

    #Add task
    elif choice == "2":
        add_task()
        pause()

    #complete task
    elif choice == "3":
        clear()
        print("=== Complete task ===\n")
        list_uncompleted_tasks()
        while True:
            try:
                selected_task = int(input("\nPlease select a task id to mark as completed (Enter 0 to exit.): "))
            except ValueError:
                print("\nPlese insert a valid id! - intyeger")
            else:
                if selected_task == 0:
                    break

                elif task_exists(selected_task):
                    delete_task(selected_task)
                    print("\nTask marked as completed successfully")
                    break                  
                else:
                    print("\nPlease insert a valid id!")
        complete_task(selected_task)
        pause()

    #delete task
    elif choice == "4":
        clear()
        print("=== Delete task ===\n")
        list_tasks()
        
        while True:
            try:
                selected_task = int(input("\nPlease select a task id to delete (Enter 0 to exit): "))
            except ValueError:
                print("\nPlese insert a valid id!")
            else:
                if selected_task == 0:
                    break

                elif task_exists(selected_task):
                    delete_task(selected_task)
                    print("\nTask delete successfully")
                    break                  
                else:
                    print("\nPlease insert a valid id!")                
        pause()
    
    #exit
    elif choice == "0":
        connection.commit()
        connection.close()
        break
    
    else:
        break

