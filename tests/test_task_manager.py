import pytest
import json
from unittest.mock import patch
from core.task_manager import assign_tasks, evaluate_responses
from core.worker_runner import execute_task


@pytest.fixture
def config(tmpdir):
    config_data = {
        "boss": "llama3",
        "workerl": "moondream",
        "worker2": "tinyllama",
        "worker3": "tinydolphin",
        "task_file": str(tmpdir.join("tasks.txt")),
        "rounds": 2,
        "input_file": str(tmpdir.join("tasks.txt")),
        "output_file": str(tmpdir.join("output.json")),
        "log_file": str(tmpdir.join("log_file")),
        "dev_mode": False,
        "num_threads": 32,
        "memory_limit": 64
    }
    with open(config_data["input_file"], 'w') as f:
        f.write("Task 1\nTask 2\nTask 3\n")
    return config_data


@pytest.fixture
def workers():
    return [
        {"name": "moondream", "function": execute_task},
        {"name": "tinyllama", "function": execute_task},
        {"name": "tinydolphin", "function": execute_task}
    ]


@patch('core.worker_runner.execute_task')
async def test_assign_tasks(mock_execute_task, config, workers, capfd):
    mock_execute_task.side_effect = lambda task, worker_name: f"Mock response to {task} b\n\n\n\ny {worker_name}"

    with open(config["input_file"], 'r') as f:
        tasks = [line.strip() for line in f.readlines()]

    await assign_tasks(workers, tasks, config["output_file"], config["rounds"])

    with open(config["output_file"], 'r') as f:
        output_lines = f.readlines()

    expected = [
        {"model_name": "moondream", "task": "Task 1",
            "response": "Mock response to Task 1 by moondream"},
        {"model_name": "tinyllama", "task": "Task 2",
            "response": "Mock response to Task 2 by tinyllama"},
        {"model_name": "tinydolphin", "task": "Task 3",
            "response": "Mock response to Task 3 by tinydolphin"},
        {"model_name": "moondream", "task": "Task 1",
            "response": "Mock response to Task 1 by moondream"},
        {"model_name": "tinyllama", "task": "Task 2",
            "response": "Mock response to Task 2 by tinyllama"},
        {"model_name": "tinydolphin", "task": "Task 3",
            "response": "Mock response to Task 3 by tinydolphin"}
    ]
    output = [json.loads(line) for line in output_lines]
    assert output == expected

    # Capture and print verbose output
    captured = capfd.readouterr()
    print(captured.out)


@patch('core.boss.review_response')
def test_evaluate_responses(mock_review_response, config, capfd):
    responses = [
        {"model_name": "moondream", "task": "Task 1",
            "response": "Mock response to Task 1 by moondream"},
        {"model_name": "tinyllama", "task": "Task 2",
            "response": "Mock response to Task 2 by tinyllama"},
        {"model_name": "tinydolphin", "task": "Task 3",
            "response": "Mock response to Task 3 by tinydolphin"},
        {"model_name": "moondream", "task": "Task 1",
            "response": "Mock response to Task 1 by moondream"},
        {"model_name": "tinyllama", "task": "Task 2",
            "response": "Mock response to Task 2 by tinyllama"},
        {"model_name": "tinydolphin", "task": "Task 3",
            "response": "Mock response to Task 3 by tinydolphin"}
    ]
    boss_model = config["boss"]

    mock_review_response.side_effect = lambda task, response, model: (
        85, f"Mock evaluation for {task}")

    evaluate_responses(responses, boss_model, config["output_file"])

    with open(config["output_file"], 'r') as f:
        output_lines = f.readlines()

    output = [json.loads(line) for line in output_lines]

    for response in responses:
        assert any(res["task"] == response["task"] and res["model_name"]
                   == response["model_name"] for res in output)

    # Capture and print verbose output
    captured = capfd.readouterr()
    print(captured.out)
