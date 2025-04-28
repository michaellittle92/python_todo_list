import sqlite3

def CreateItem():
    print("Add Task item")
    item = input("Enter task item.")
    
    sqliteConnection = sqlite3.connect("todo.db")
    cursor = sqliteConnection.cursor()

    insert_query = """INSERT INTO Tasks (task_name, is_complete)
    VALUES (?, 0)
    ;"""
    cursor.execute(insert_query, (item,))
    sqliteConnection.commit()
    cursor.close()
    sqliteConnection.close()


    print(f"{item} has been successfully added to the tasks list.")

def ReadItems():
    for item in tasks:
        print(RowBuilder(item["task"], item["status"]))

def RowBuilder(task, status):
    if status == False:
        status = ("[ ]")
    else:
        status = ("[x]")
    return(f"{task}    {status}")

def CompleteItem():
    print("TODO: Compete item stored in tasks")
    ReadItems()
    user_input = int(input("select the row number of the item you want to marks as complete: ")) -1
    tasks[user_input]["status"] = True
    print(f"{tasks[user_input]["task"]} has been marked as complete")

def ModifyItem():
    ReadItems()
    user_input = int(input("select the row number of the item you want to edit: ")) -1
    old_task_text = tasks[user_input]["task"]
    new_task_text = input("new task text: ")
    tasks[user_input]["task"] = new_task_text
    print(f"{old_task_text} has now been updated to {new_task_text}")
    
def DeleteItem():
    ReadItems()
    user_input = int(input("select the row number of the item you want to delete: ")) -1
    deleted_task = tasks.pop(user_input)

    print(f"the task: {deleted_task["task"]}. has been deleted. ")

def InitializeDatabase():
    sqliteConnection = sqlite3.connect("todo.db")
    cursor = sqliteConnection.cursor()

    table = """CREATE TABLE IF NOT EXISTS Tasks (
    task_name TEXT NOT NULL,
    is_complete INTEGER NOT NULL
    );"""
    cursor.execute(table)

def menu(): 
    exit = False
    while exit == False:
        print("menu.")
        print("1. Show all current items")
        print("2. Add an item.")
        print("3. Complete an item")
        print("4. Modify an item")
        print("5. Delete an item")
        print("6. Exit")
        user_input = int(input("Enter the coresponding number to make your selection."))
        if user_input == 1:
            ReadItems()
        elif user_input == 2: 
            CreateItem()
        elif user_input == 3: 
            CompleteItem()
        elif user_input == 4:
            ModifyItem()
        elif user_input == 5:
            DeleteItem()
        elif user_input == 6:
           exit = True
           print("exiting program...")
        else: 
            print("An error has occoured. Please Try again\n")

print("Todo List.")
InitializeDatabase()
menu()

