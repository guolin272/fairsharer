# Portfolio Exercise 6: Fair Sharer

This is my repository for the "Finger Exercise 6" in the Data Science course.

## What this code does
I implemented a function called `fair_sharer`. It looks for the highest value in a list and distributes a part of it to the neighbors on the left and right side.
If the highest value is at the edge, it wraps around.

## Project Structure
* `fairsharer/`: Contains the main python code.
* `tests/`: Contains a unit test to check if the calculation is correct.
* `.github/workflows`: A CI pipeline that runs the tests automatically on Ubuntu, Windows and Mac.
* `pyproject.toml`: Defines the dependencies.

## How to use
To run this on your computer, you need to install the dependencies first:

```bash
pip install ".[dev]"