from core.worker_runner import execute_task


def test_execute_task():
    task = "Sample task"
    worker_name = "moondream"
    response = execute_task(task, worker_name)
    assert response == f"Response to {task} by {worker_name}"
