# Development Guide for AI Agents

## Project Structure

* `src/`: The source code for this project.
* `tests/`: The test scripts for unit testing.

## Setup

First, run the following commands to set up the development environment:

* `uv sync`: Install dependencies and build the package.
* `uv run task setup`: Setup the project. Here's what will actually happen:
  * Install Git hooks with Lefthook.

## Coding Conventions

* Follow PEP 8.

## Check and Fix Code

Run the following commands to perform various checks and fixes in one go.

* `uv run task check`: Check the whole code.
* `uv run task fix`: Check and fix the whole code.

To run individually:

* `uv run ec`: editorconfig-checker
* `uv run typos`: Typos
* `uv run ruff check`: Ruff (Check)
* `uv run ruff format`: Ruff (Format)
* `uv run ty check`: ty

## Git Operations

### Commit Messages

* Follow Conventional Commits.
* Use the imperative mood in the *description* part.
* Lowercase the first letter of the *type*, *scope*, and *description* parts.

### Pull Requests

* Pull request titles should also follow the above commit message conventions.
