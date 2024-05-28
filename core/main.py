from core.config_loader import load_config
from core.worker_runner import execute_task
from core.task_manager import assign_tasks, evaluate_responses
from core.boss import initialize_boss_model
import json
import asyncio
from rich.console import Console

console = Console()


async def main():
    config = load_config()

    # Read tasks from the input file
    with open(config["input_file"], 'r') as f:
        tasks = [line.strip() for line in f.readlines()]

    workers = [
        {"name": config["workerl"], "function": execute_task},
        {"name": config["worker2"], "function": execute_task},
        {"name": config["worker3"], "function": execute_task}
    ]

    boss_model = config["boss"]
    output_file = config["output_file"]  # Read the output file from config
    rounds = config.get("rounds", 1)  # Default to 1 round if not specified

    # Initialize the boss model with grading instructions
    initialize_boss_model(boss_model)

    await assign_tasks(workers, tasks, output_file, rounds)

    # Read the responses from the output file
    responses = []
    with open(output_file, 'r') as f:
        for line in f:
            responses.append(json.loads(line))

    evaluate_responses(responses, boss_model, output_file)

if __name__ == "__main__":
    asyncio.run(main())
