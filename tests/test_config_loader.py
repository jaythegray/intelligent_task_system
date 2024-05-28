import pytest
from core.config_loader import load_config, validate_config

def test_load_config():
    config = load_config('config.json')
    assert isinstance(config, dict)

def test_validate_config():
    config = {
        "task_file": "tasks.txt",
        "worker_count": 3
    }
    validate_config(config)
    assert True
