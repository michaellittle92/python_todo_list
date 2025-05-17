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

    #@staticmethod
    # def get_task_by_id(task_id):
        # Connect to DB
        # SELECT WHERE task_id = ?
        # Return Task object

   # @staticmethod
    #def initialize_db():
        # Run CREATE TABLE IF NOT EXISTS

