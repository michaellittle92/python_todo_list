from rich.console import Console 
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt
from rich.panel import Panel
from rich.align import Align

import requests
import os
import sys
os.system('clear')

console = Console()

def render_table(get_completed_tasks):
    os.system('clear')
    table = Table(
        title="Task List",
        header_style="bold white",
        border_style="dim",
        expand=True
    )
    if get_completed_tasks == True:
        all_tasks = api_get_all_tasks()
    else:
        all_tasks = api_get_incomplete_tasks()
    

    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Task", style="magenta")
    table.add_column("Status", justify="center")

    for task in all_tasks:
        status = Text("[x]", style="green") if task["is_complete"] else Text("[ ]", style="red")
        table.add_row(str(task["task_id"]), task["task_name"], status)

    console.print(table)

def show_menu():
    menu_text ="""
[1] View All Tasks 
[2] Add New Task
[3] Mark Task as Complete
[4] Exit
"""
    panel = Panel(
        Align.left(menu_text),
        subtitle="Use number keys to choose an action"
    )
    console.print(panel)
    choice = Prompt.ask("[bold white]Enter choice[/bold white]")
    return choice.strip()

def api_get_all_tasks():
    try:
        response = requests.get("http://127.0.0.1:8000/get-all-tasks")
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print("tasks not found")
        else:
            print(e)
    except requests.exceptions.ConnectionError:
            print("[red]Could not connect to the API. Is the server running?[/red]")
    return response.json()

def api_get_incomplete_tasks():
    try:
        response = requests.get("http://127.0.0.1:8000/get-all-incomplete-tasks")
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print("tasks not found")
        else:
            print(e)
    except requests.exceptions.ConnectionError:
            print("[red]Could not connect to the API. Is the server running?[/red]")
    return response.json()

def api_add_task():
    choice = Prompt.ask("[bold white]Enter new task name: ").strip()
    try:
        response = requests.post(f"http://127.0.0.1:8000/add_task?task_name={choice}")
        response.raise_for_status()
        data = response.json
        console.print(f"[green]Task added! {choice}[/green]")
    except requests.exceptions.RequestException as e:
        console.print(f"[red]Failed to add task:[/red] {e}")
    render_table(False)

def api_mark_task_complete():
    render_table(False)
    choice = Prompt.ask("[bold white]Enter task id of the task you have completed: ").strip()
    response = requests.patch(f"http://127.0.0.1:8000/complete_task?task_id={choice}")
    data = response.json()
    console.print(f"[bold]{data.get("message")}")
    render_table(False)

def main():
    render_table(False)
    while True:
        choice = show_menu()
        if choice == "1":
            render_table(True)
        if choice == "2": 
            api_add_task()
        if choice =="3":
            api_mark_task_complete()
        if choice =="4":
            os.system("clear")
            console.print("[bold]Exiting....")
            sys.exit()
main()