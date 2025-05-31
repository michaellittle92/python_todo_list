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
        SELECT task_id, task_name, is_complete FROM Tasks
        '''
        cursor.execute(select_all_query)
        # For each row, create a Task instance
        for task in cursor:
           tasks.append(Task(task[0], task[1], task[2]))
        return tasks
    
    def get_all_incomplete_tasks():
        tasks = []
        # Connect to DB
        sqliteConnection = sqlite3.connect("todo.db")
        cursor = sqliteConnection.cursor()
        # SELECT * FROM Tasks
        select_all_query = '''
        SELECT  task_id, task_name, is_complete FROM Tasks
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

    task_table = """CREATE TABLE IF NOT EXISTS Tasks (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT NOT NULL,
    task_order_index INTEGER,
    project_id INTEGER, 
    task_creation_timestamp TIMESTAMP,
    task_completion_timestamp,
    is_complete INTEGER NOT NULL
    );"""
    
    project_table = """CREATE TABLE IF NOT EXISTS Projects(
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT NOT NULL,
    project_description TEXT

    );
    """
    cursor.execute(project_table)
    cursor.execute(task_table)


