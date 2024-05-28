from rich.console import Console
import json
import asyncio
from core.boss import review_response

console = Console()


async def assign_task(worker, task):
    console.print(f"Assigning task to {worker['name']}: {task}")
    response = await worker['function'](task, worker['name'])
    return {
        "model_name": worker['name'],
        "task": task,
        "response": response
    }


async def assign_tasks(workers, tasks, output_file, rounds):
    tasks_to_run = []
    task_index = 0

    for _ in range(rounds):
        for worker in workers:
            if task_index < len(tasks):
                task = tasks[task_index]
                task_index += 1
                tasks_to_run.append(assign_task(worker, task))

    results = await asyncio.gather(*tasks_to_run)

    with open(output_file, 'a') as f:
        for result in results:
            f.write(json.dumps(result) + "\n")


def evaluate_responses(responses, boss_model, output_file):
    updated_responses = []
    for response in responses:
        task = response["task"]
        response_text = response["response"]
        console.print(f"Evaluating response for task: {task}")
        score, reason = review_response(task, response_text, boss_model)
        response["score"] = score
        response["reason"] = reason
        updated_responses.append(response)

    with open(output_file, 'a') as f:  # Open in append mode
        for response in updated_responses:
            f.write(json.dumps(response) + "\n")

    return updated_responses
