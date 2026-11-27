# Test Station Planner

A learning project that will turn test requirements into a draft test station plan.
Right now it contains an Instrument class and its first tests.

## Setup

1. Clone the repository and open the folder.
2. Create and activate a virtual environment:

    python -m venv .venv
    .venv/Scripts/Activate.ps1

3. Install the dependencies:

    pip install -r requirements.txt

## Run the tests

With the virtual environment active, run this from the project root:

    pytest

Expected result: 2 passed.

## Project layout

- src/instrument.py: the Instrument class (range and accuracy checks)
- tests/test_instrument.py: tests for the Instrument classpip freeze > requirements.txt