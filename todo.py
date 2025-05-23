import sqlite3
from task import Task

def InitializeDatabase():
    sqliteConnection = sqlite3.connect("todo.db")
    cursor = sqliteConnection.cursor()

    table = """CREATE TABLE IF NOT EXISTS Tasks (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
            ReadAllItems()
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

