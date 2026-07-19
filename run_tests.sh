#!/bin/bash

# Activate the virtual environment
source venv/Scripts/activate

# Run the test suite
pytest

# Check the exit status
if [ $? -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi