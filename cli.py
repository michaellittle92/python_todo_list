from task import Task
from taskmanger import *

item = Task(0, "class test", False)
item.create_new_task()

print(item)

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
           all_tasks = TaskManager.get_all_tasks()
           for task in all_tasks:
               print(task)
        elif user_input == 2: 
            CreateItem()
        elif user_input == 3: 
            #CompleteItem()
            pass
        elif user_input == 4:
           # ModifyItem()
           pass
        elif user_input == 5:
          #  DeleteItem()
          pass
        elif user_input == 6:
           exit = True
           print("exiting program...")
        else: 
            print("An error has occoured. Please Try again\n")

def CreateItem():
    user_input = input("Enter new task item: ")
    item = Task(0, user_input, False).create_new_task()
print("Todo List.")
menu()

