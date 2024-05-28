## README.md



## .gitignore

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environment
venv/
ENV/
env/
env.bak/
venv.bak/

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
pytestdebug.log

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# dotenv
.env
.env.*

# Sphinx documentation
docs/_build/

# Pyre type checker
.pyre/

# Custom logs
logs/

# IntelliJ IDEA files
.idea/

# Project configuration file
config.json


## requirements.txt

anyio==4.4.0
asyncio==3.4.3
autopep8==2.1.1
certifi==2024.2.2
cfgv==3.4.0
distlib==0.3.8
exceptiongroup==1.2.1
filelock==3.14.0
flake8==7.0.0
h11==0.14.0
httpcore==1.0.5
httpx==0.27.0
identify==2.5.36
idna==3.7
iniconfig==2.0.0
markdown-it-py==3.0.0
mccabe==0.7.0
mdurl==0.1.2
nodeenv==1.8.0
ollama==0.2.0
packaging==24.0
platformdirs==4.2.2
pluggy==1.5.0
pre-commit==3.7.1
pycodestyle==2.11.1
pyflakes==3.2.0
Pygments==2.18.0
pytest==8.2.1
pytest-asyncio==0.23.7
PyYAML==6.0.1
rich==13.7.1
sniffio==1.3.1
tomli==2.0.1
typing_extensions==4.12.0
virtualenv==20.26.2


## setup.cfg

[pep8]
max-line-length = 88
exclude = venv,*.egg,build,dist
[tool:pytest]
testpaths = tests
python_paths = .


## .flake8

[flake8]
max-line-length = 89
exclude = venv,*.egg,build,dist


## .pre-commit-config.yaml

repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.4.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
-   repo: https://github.com/pycqa/flake8
    rev: 3.9.2
    hooks:
    -   id: flake8
-   repo: https://github.com/pre-commit/mirrors-autopep8
    rev: v1.5.7
    hooks:
    -   id: autopep8


## pytest.ini

[pytest]
minversion = 6.0
addopts = -ra -q
testpaths =
    tests


## run.py

import sys
import os
import asyncio
from core.main import main

# Add the core directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'core')))

# Import the main function and run it
if __name__ == "__main__":
    asyncio.run(main())


## config.json

{
    "boss": "llama3",
    "workerl": "moondream",
    "worker2": "tinyllama",
    "worker3": "tinydolphin",
    "task_file": "files/tasks/grammar_correction.txt",
    "rounds": 1,
    "input_file": "files/tasks/grammar_correction.txt",
    "output_file": "files/output.json",
    "log_file": "logs/log_file",
    "dev_mode": false,
    "num_threads": 32,
    "memory_limit": 64
}


## grammar_correction.txt

1. Correct the grammar in the following sentence: She don't like apples.
2. Correct the grammar in the following sentence: The cat was chasing it’s tail.
3. Correct the grammar in the following sentence: Me and her went to the store.
4. Correct the grammar in the following sentence: They has been waiting for a long time.
5. Correct the grammar in the following sentence: He runned to the park.
6. Correct the punctuation in the following sentence: Lets go to the park she said
7. Correct the punctuation in the following sentence: Wow what a beautiful view
8. Correct the punctuation in the following sentence: Can you believe it
9. Correct the punctuation in the following sentence: The quick brown fox jumps over the lazy dog
10. Correct the punctuation in the following sentence: I cant wait to see you
11. Fix the verb tense in the following sentence: Yesterday, she walk to the store.
12. Fix the verb tense in the following sentence: He is go to the gym every day.
13. Fix the verb tense in the following sentence: They have finish their homework.
14. Fix the verb tense in the following sentence: She was play basketball when I saw her.
15. Fix the verb tense in the following sentence: He has went to the party.
16. Improve the sentence structure: Because I was hungry, so I ate.
17. Improve the sentence structure: She is a good singer she sings beautifully.
18. Improve the sentence structure: I like pizza, it's tasty.
19. Improve the sentence structure: When it raining, I stay inside.
20. Improve the sentence structure: The movie was good, I enjoyed it.


## math_problems.txt

# Math Problems

Solve the following problems:
1. What is 5 + 7?
2. Subtract 9 from 15.
3. Multiply 6 by 8.
4. Divide 40 by 5.
5. What is the square root of 81?

Solve the following word problems:
6. If you have 3 apples and you get 2 more, how many apples do you have in total?
7. A train travels 60 miles per hour. How far will it travel in 3 hours?
8. If a book costs $15 and you buy 4 books, how much will you spend?
9. You have 24 candies and want to share them equally among 6 friends. How many candies does each friend get?
10. If a rectangle has a length of 8 cm and a width of 5 cm, what is its area?

Solve the following advanced problems:
11. What is the derivative of x^2 + 3x + 2?
12. Integrate the function 3x^2.
13. Solve for x: 2x + 3 = 7.
14. What is the value of pi to the first five decimal places?
15. Calculate the factorial of 5.

Solve the following geometry problems:
16. What is the perimeter of a triangle with sides 3 cm, 4 cm, and 5 cm?
17. Find the volume of a cube with a side length of 4 cm.
18. What is the circumference of a circle with a radius of 7 cm?
19. Calculate the area of a triangle with a base of 5 cm and a height of 12 cm.
20. Find the surface area of a sphere with a radius of 6 cm.


## __init__.py



## conftest.py

import sys
import os

# Add the root directory of the project to the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


## test_task_manager.py

import pytest
import json
import asyncio
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
    mock_execute_task.side_effect = lambda task, worker_name: f"Mock response to {task} by {worker_name}"

    with open(config["input_file"], 'r') as f:
        tasks = [line.strip() for line in f.readlines()]

    await assign_tasks(workers, tasks, config["output_file"], config["rounds"])

    with open(config["output_file"], 'r') as f:
        output_lines = f.readlines()

    expected = [
        {"model_name": "moondream", "task": "Task 1", "response": "Mock response to Task 1 by moondream"},
        {"model_name": "tinyllama", "task": "Task 2", "response": "Mock response to Task 2 by tinyllama"},
        {"model_name": "tinydolphin", "task": "Task 3", "response": "Mock response to Task 3 by tinydolphin"},
        {"model_name": "moondream", "task": "Task 1", "response": "Mock response to Task 1 by moondream"},
        {"model_name": "tinyllama", "task": "Task 2", "response": "Mock response to Task 2 by tinyllama"},
        {"model_name": "tinydolphin", "task": "Task 3", "response": "Mock response to Task 3 by tinydolphin"}
    ]
    output = [json.loads(line) for line in output_lines]
    assert output == expected

    # Capture and print verbose output
    captured = capfd.readouterr()
    print(captured.out)

@patch('core.boss.review_response')
def test_evaluate_responses(mock_review_response, config, capfd):
    responses = [
        {"model_name": "moondream", "task": "Task 1", "response": "Mock response to Task 1 by moondream"},
        {"model_name": "tinyllama", "task": "Task 2", "response": "Mock response to Task 2 by tinyllama"},
        {"model_name": "tinydolphin", "task": "Task 3", "response": "Mock response to Task 3 by tinydolphin"},
        {"model_name": "moondream", "task": "Task 1", "response": "Mock response to Task 1 by moondream"},
        {"model_name": "tinyllama", "task": "Task 2", "response": "Mock response to Task 2 by tinyllama"},
        {"model_name": "tinydolphin", "task": "Task 3", "response": "Mock response to Task 3 by tinydolphin"}
    ]
    boss_model = config["boss"]

    mock_review_response.side_effect = lambda task, response, model: (85, f"Mock evaluation for {task}")

    evaluate_responses(responses, boss_model, config["output_file"])

    with open(config["output_file"], 'r') as f:
        output_lines = f.readlines()

    output = [json.loads(line) for line in output_lines]

    for response in responses:
        assert any(res["task"] == response["task"] and res["model_name"] == response["model_name"] for res in output)

    # Capture and print verbose output
    captured = capfd.readouterr()
    print(captured.out)


## test_logger.py



## test_config_loader.py

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


## test_worker_runner.py

from core.worker_runner import execute_task


def test_execute_task():
    task = "Sample task"
    worker_name = "moondream"
    response = execute_task(task, worker_name)
    assert response == f"Response to {task} by {worker_name}"


## __init__.py



## boss.py

from rich.console import Console
import subprocess
import re

console = Console()


def initialize_boss_model(boss_model):
    grading_instructions = """
    Please follow these grading criteria when evaluating the responses:
    - A (90 - 99): Excellent responses that are well-structured, clear, detailed, address all parts of the task, provide specific examples or supporting evidence, and are persuasive and convincing.
    - B (80 - 89): Good responses that are clear and concise, address most parts of the task, provide some examples or evidence, but may lack some detail or persuasiveness.
    - C (70 - 79): Average responses that address the task but may lack clarity, detail, or specific examples. These responses are generally acceptable but have room for improvement.
    - D (60 - 69): Below average responses that are partially correct but lack significant detail, clarity, or fail to address important parts of the task.
    - F (00 - 59): Poor responses that fail to address the task adequately, are unclear, lack structure, or contain significant errors.
    """
    # Construct the command for the Ollama CLI
    command = ['ollama', 'run', boss_model, grading_instructions]

    try:
        # Run the command and capture the output
        subprocess.run(command, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error initializing boss model: {e}[/red]")


def review_response(task, response, boss_model):
    # Construct the command for the Ollama CLI
    command = [
        'ollama', 'run', boss_model,
        f"Task: {task}\nResponse: {response}\nEvaluate the response and provide a score between 1 and 99 and a reason for the score."
    ]

    try:
        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout.strip()

        # Extract the score using regex
        score_match = re.search(r'\bScore:\s*(\d+)', output)
        raw_score = int(score_match.group(1)) if score_match else 0

        # Extract the reason by finding the section after "Reason:" or "Reason for score:"
        reason_match = re.search(r'Reason:(.*)', output, re.DOTALL)
        reason = reason_match.group(1).strip() if reason_match else "No reason provided"

        # Ensure score is between 1 and 99
        if raw_score < 1:
            raw_score = 1
        elif raw_score > 99:
            raw_score = 99

        # Define grading parameters
        if 90 <= raw_score <= 99:
            grade = 'A'
        elif 80 <= raw_score <= 89:
            grade = 'B'
        elif 70 <= raw_score <= 79:
            grade = 'C'
        elif 60 <= raw_score <= 69:
            grade = 'D'
        else:
            grade = 'F'

        score = raw_score
        reason = f"Grade: {grade}. {reason}"

    except (subprocess.CalledProcessError, ValueError, re.error) as e:
        console.print(f"[red]Error processing response: {e}[/red]")
        score = 0
        reason = "Error in evaluation"

    return score, reason


## config_loader.py

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
    required_keys = [
        "boss", "workerl", "worker2", "worker3",
        "task_file", "rounds", "log_file", "dev_mode"
    ]
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing required config key: {key}")


## worker_runner.py

import asyncio


async def execute_task(task, worker_name):
    # Simulate task execution with a placeholder response
    await asyncio.sleep(1)  # Simulate some delay
    return f"Response to {task} by {worker_name}"


## task_manager.py

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
        worker_name = response["model_name"]
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


## logger.py

import logging
from rich.logging import RichHandler

logging.basicConfig(level="INFO", handlers=[RichHandler()])
logger = logging.getLogger("rich")


## main.py

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
