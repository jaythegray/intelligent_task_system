from rich.console import Console

console = Console()


def assign_tasks(workers, tasks):
    results = []
    for worker_name, task in zip(workers.keys(), tasks):
        console.print(f"[green]Assigning task to {worker_name}: {task}[/green]")
        response = workers[worker_name](task, worker_name)
        results.append((task, response))
    return results


def evaluate_responses(responses):
    for task, response in responses:
        console.print(f"[red]Evaluating response for task: {task}[/red]")
        # Evaluation logic
        score = len(response)  # Placeholder score logic
        console.print(f"[yellow]Score: {score}[/yellow]")
