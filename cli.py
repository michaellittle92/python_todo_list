from rich.console import Console 
from rich.table import Table
from taskmanger import *

console = Console()

console.print("Hello", "World", style="bold red")

table = Table(title = "Tasks")
table.add_column("Task_id")
table.add_column("Task_name")
table.add_column("Is_complete")

all_tasks = TaskManager.get_all_tasks()

for task in all_tasks: 
    table.add_row(str(task.task_id), task.task_name, str(task.is_complete))

#print(all_tasks[0].task_name)

console.print(table)