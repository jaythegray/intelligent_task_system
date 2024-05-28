import json
import os

def load_config(config_path='config.json'):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file {config_path} not found.")
    
    with open(config_path, 'r') as file:
        config = json.load(file)
    
    validate_config(config)
    return config

def validate_config(config):
    required_keys = ["task_file", "worker_count"]
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required config key: {key}")
