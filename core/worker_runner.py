from rich.console import Console

console = Console()


def execute_task(task, worker_name):
    console.print(f"[blue]{worker_name} executing task: {task}[/blue]")
    # Simulate task execution logic
    response = f"Response to {task} by {worker_name}"
    return response
