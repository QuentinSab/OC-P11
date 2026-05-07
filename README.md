# OC-P12

This project is a web application built with Flask that allows clubs to register for competitions and book places.

## Requirements

- Python 3.x
- pip
- Firefox (for functional tests)

## Setup

### 1. Clone the repository

Open your terminal and clone the project repository using the following command:

    git clone https://github.com/QuentinSab/OC-P11

Change into the project directory:

    cd OC-P11

### 2. Create a virtual environment

To create a virtual environment with venv:

    python -m venv env

### 3. Activate the virtual environment

To activate the virtual environment, use:

On Windows:

    env\Scripts\activate

On macOS/Linux:

    source env/bin/activate

### 4. Install dependencies

With the virtual environment activated, install the required packages listed in requirements.txt using the following command:

    pip install -r requirements.txt

## Usage

### 1. Running the application

To start the server, activate the virtual environment then use:

    $env:FLASK_APP = "server.py"
    flask run

Then open your browser at:

    http://127.0.0.1:5000

### 2. Using the program

You can log in using the emails in "clubs.json".

## Testing

### 1. Running the test

To launch the test, use the following commands:

    $env:PYTHONPATH="."
    pytest

You can verify the test coverage with:

    coverage run -m pytest

And one of the commands below:

    coverage report
    coverage html

### 2. Using Locust

With the server running, open another terminal, activate the virtual environment then use:

    locust

Open your browser at:

    http://localhost:8089

And set the host:

    http://127.0.0.1:5000

## Documentation

Flask : https://flask.palletsprojects.com/en/stable/
Pytest : https://docs.pytest.org/en/stable/
Selenium : https://selenium-python.readthedocs.io/
Locust : https://docs.locust.io/en/stable/