from core.task_manager import assign_tasks, evaluate_responses


def test_assign_tasks():
    workers = {
        "workerl": lambda task, worker_name: f"Response to {task} by {worker_name}",
        "worker2": lambda task, worker_name: f"Response to {task} by {worker_name}",
        "worker3": lambda task, worker_name: f"Response to {task} by {worker_name}"
    }
    tasks = ["Task 1", "Task 2", "Task 3"]
    results = assign_tasks(workers, tasks)
    expected = [
        ("Task 1", "Response to Task 1 by workerl"),
        ("Task 2", "Response to Task 2 by worker2"),
        ("Task 3", "Response to Task 3 by worker3")
    ]
    assert results == expected


def test_evaluate_responses():
    responses = [
        ("Task 1", "Response to Task 1 by workerl"),
        ("Task 2", "Response to Task 2 by worker2"),
        ("Task 3", "Response to Task 3 by worker3")
    ]
    evaluate_responses(responses)
    assert True  # Just check that the function runs without error
