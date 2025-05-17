import sqlite3

class Task:
    def __init__(self, task_id, task_name, is_complete):
        self.task_id = task_id
        self.task_name = task_name
        self.is_complete = is_complete
    
    def __str__(self):
        status = "[ ]"
        if self.is_complete == True:
            status = "[x]"
        return f"{status} {self.task_id}. {self.task_name}"
    
    def create_new_task(self):
        sqliteConnection = sqlite3.connect("todo.db")
        cursor = sqliteConnection.cursor()
        insert_query = """INSERT INTO Tasks (task_name, is_complete)
        VALUES (?, 0)
        ;"""
        cursor.execute(insert_query, (self.task_name,))
        sqliteConnection.commit()
        self.task_id = cursor.lastrowid
        cursor.close()
        sqliteConnection.close()

    def update_name(self, new_name):
        sqliteConnection = sqlite3.connect("todo.db")
        cursor = sqliteConnection.cursor()
        update_name_query = """
        Update Tasks 
        SET task_name = ?
        WHERE task_id = ?;
        """
        cursor.execute(update_name_query,(new_name, self.task_id))
        sqliteConnection.commit()
        cursor.close()
        sqliteConnection.close()
    
    def mark_complete(self):
        sqliteConnection = sqlite3.connect("todo.db")
        cursor = sqliteConnection.cursor()
        mark_complete_query = """
        Update Tasks 
        Set is_complete = 1
        WHERE task_id = ?
        """
        cursor.execute(mark_complete_query, (self.task_id,))
        sqliteConnection.commit()
        cursor.close()
        sqliteConnection.close()
    
    def delete_task(self):
        sqliteConnection = sqlite3.connect("todo.db")
        cursor = sqliteConnection.cursor()
        delete_query = """
        DELETE FROM Tasks 
        WHERE task_id = ?
        """
        cursor.execute(delete_query,(self.task_id,))
        sqliteConnection.commit()
        cursor.close()
        sqliteConnection.close()
