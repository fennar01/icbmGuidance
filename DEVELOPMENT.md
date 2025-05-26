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

## Running the Simulation
To run the simulation locally:
```bash
pip install -r requirements.txt
python simulation.py
```
This will execute the non-functional simulation and display a simple trajectory plot.

## Repository
Find the latest code and documentation at: https://github.com/fennar01/icbmGuidance

## Safe Contribution Guidelines
- Always check that your changes do not introduce any real-world operational logic.
- If in doubt, open an issue or discussion before submitting a pull request.

## Extending the Simulation
This project now uses a modular, class-based architecture. To add new features or subsystems:
- Create a new class for your subsystem (e.g., FaultInjector, EnvironmentalModel).
- Ensure all logic is non-functional and safe for public demonstration.
- Add clear docstrings and comments explaining the educational purpose.
- Update the Simulation orchestrator to include your new module if needed.

## Example Extensions
- Add simulated sensor failures or noise models.
- Add a (non-functional) environmental effects module (e.g., wind, gravity variations).
- Add more detailed trajectory visualizations (3D plots, error ellipses, etc.).

All contributions must maintain the non-functional, educational intent of the project. 