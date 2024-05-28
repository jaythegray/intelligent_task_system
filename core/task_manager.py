from rich.console import Console

console = Console()

def assign_tasks(workers, tasks):
    results = []
    for worker, task in zip(workers, tasks):
        console.print(f"[green]Assigning task to worker: {task}[/green]")
        response = worker(task)
        results.append((task, response))
    return results

def evaluate_responses(responses):
    for task, response in responses:
        console.print(f"[red]Evaluating response for task: {task}[/red]")
        # Evaluation logic
        score = len(response)  # Placeholder score logic
        console.print(f"[yellow]Score: {score}[/yellow]")
