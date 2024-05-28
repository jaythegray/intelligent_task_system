from core.config_loader import load_config, validate_config


def test_load_config():
    config = load_config('config.json')
    assert isinstance(config, dict)


def test_validate_config():
    config = {
        "boss": "llama2-uncensored",
        "workerl": "moondream",
        "worker2": "tinyllama",
        "worker3": "tinydolphin",
        "task_file": "files/tasks/task_category1.txt",
        "rounds": 2,
        "log_file": "logs/log_file",
        "dev_mode": False
    }
    validate_config(config)
    assert True
