#!/bin/bash

# Function to check if virtual environment is active
check_venv() {
    if [[ -z "$VIRTUAL_ENV" ]]; then
        echo "Virtual environment is not activated. Please activate the virtual environment and rerun the script."
        exit 1
    fi
}

# Create virtual environment
python3 -m venv ../venv

# Activate virtual environment
source ../venv/bin/activate

# Check if virtual environment is active
check_venv

# Install dependencies
pip install -r ../requirements.txt

# Install pre-commit hooks for flake8 and autopep8
pip install pre-commit
pre-commit install

# Configure pre-commit hooks
cat <<EOT >> ../.pre-commit-config.yaml
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
EOT

# Run pre-commit install again to configure hooks
pre-commit install

echo "Setup completed successfully."
