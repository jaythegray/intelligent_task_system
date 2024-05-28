from core.config_loader import load_config
from core.worker_runner import execute_task
from core.task_manager import assign_tasks, evaluate_responses


def main():
    config = load_config()
    tasks = ["Task 1", "Task 2", "Task 3"]  # Placeholder for actual task loading logic
    workers = {
        "workerl": execute_task,
        "worker2": execute_task,
        "worker3": execute_task
    }

    for _ in range(config["rounds"]):
        responses = assign_tasks(workers, tasks)
        evaluate_responses(responses)


if __name__ == "__main__":
    main()
