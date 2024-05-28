import asyncio


async def execute_task(task, worker_name):
    # Simulate task execution with a placeholder response
    await asyncio.sleep(1)  # Simulate some delay
    return f"Response to {task} by {worker_name}"
