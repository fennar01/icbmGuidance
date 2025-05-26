# Development Pipeline for ICBM Guidance System Simulation (Non-Functional)

## Overview
This document describes the recommended development workflow for contributors. All work should reinforce the educational, non-functional nature of the project.

## Code Style
- Use [PEP8](https://pep8.org/) for Python code style.
- Write clear, well-documented code with comments explaining non-functional placeholders.

## Linting
- Use `flake8` or `pylint` for linting Python code.
- Run `flake8 simulation.py` before committing changes.

## Testing
- Use `pytest` for any testable, non-sensitive logic.
- All tests should be safe, non-operational, and educational.

## Continuous Integration (CI)
- Recommended: GitHub Actions for CI pipeline.
- Example steps:
  - Install dependencies
  - Run linter
  - Run tests

## Contributing
- All contributions must maintain the non-functional, educational intent.
- No real-world guidance, navigation, or control code is permitted.
- All PRs are reviewed for safety and clarity.

## Security & Ethics
- This repository is for demonstration only.
- No sensitive, dangerous, or export-controlled information is allowed. 