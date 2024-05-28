from rich.console import Console

console = Console()

def execute_task(task):
    console.print(f"[blue]Worker executing task: {task}[/blue]")
    # Task execution logic
    response = f"Response to {task}"
    return response
