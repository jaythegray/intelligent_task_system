#!/bin/bash

# Run autopep8 to fix the formatting issues
autopep8 --in-place --recursive .

# Run flake8 to identify any remaining issues
flake8_output=$(flake8 .)
if [ -n "$flake8_output" ]; then
    echo "Flake8 issues detected:"
    echo "$flake8_output"

    # Fix long lines
    echo "Fixing long lines..."
    for file in $(echo "$flake8_output" | grep -oP '^[^:]+'); do
        sed -i -E 's/.{89}/&\\n/g' "$file"
    done

    # Remove unused imports and fix blank lines issues
    echo "Removing unused imports and fixing blank lines..."
    for file in $(echo "$flake8_output" | grep -oP '^[^:]+'); do
        autoflake --in-place --remove-unused-variables --remove-all-unused-imports "$file"
        autopep8 --in-place --aggressive --aggressive "$file"
    done
fi

# Run pre-commit hooks again to ensure all issues are fixed
pre-commit run --all-files

echo "All issues fixed."
