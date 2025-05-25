from task import Task
import sqlite3

class TaskManager:

    @staticmethod
    def get_all_tasks():
        tasks = []
        # Connect to DB
        sqliteConnection = sqlite3.connect("todo.db")
        cursor = sqliteConnection.cursor()
        # SELECT * FROM Tasks
        select_all_query = '''
        SELECT * FROM Tasks
        '''
        cursor.execute(select_all_query)
        # For each row, create a Task instance
        for task in cursor:
           tasks.append(Task(task[0], task[1], task[2]))
        return tasks
    
    def get_all_complete_tasks():
        tasks = []
        # Connect to DB
        sqliteConnection = sqlite3.connect("todo.db")
        cursor = sqliteConnection.cursor()
        # SELECT * FROM Tasks
        select_all_query = '''
        SELECT * FROM Tasks
        WHERE is_complete != 1
        '''
        cursor.execute(select_all_query)
        # For each row, create a Task instance
        for task in cursor:
           tasks.append(Task(task[0], task[1], task[2]))
        return tasks
    
def InitializeDatabase():
    sqliteConnection = sqlite3.connect("todo.db")
    cursor = sqliteConnection.cursor()

    table = """CREATE TABLE IF NOT EXISTS Tasks (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT NOT NULL,
    is_complete INTEGER NOT NULL
    );"""
    cursor.execute(table)


