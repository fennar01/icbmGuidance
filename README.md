# ICBM Guidance System Simulation (Non-Functional)

**DISCLAIMER: This project is a non-functional, educational simulation of an Intercontinental Ballistic Missile (ICBM) guidance system. It is intended solely for demonstration purposes for journalists and researchers. No part of this project is operational or intended for real-world use.**

## Project Overview
This repository simulates the theoretical architecture and logic of an ICBM guidance system using open source tools. All code and documentation are intentionally incomplete and non-operational, with sensitive or dangerous elements omitted or replaced with safe placeholders.

## Features
- Modular architecture for guidance, navigation, and control (GNC)
- Simulated sensor and actuator interfaces
- Visualization of theoretical missile trajectory
- Modern development pipeline (CI/CD, linting, testing)
- Educational documentation

## What This Is **NOT**
- This is **not** a real or functional missile guidance system
- No code here can be used for real-world weaponry
- All sensitive or dangerous details are omitted or replaced

## Intended Audience
- Journalists
- Researchers
- Policy makers
- Educators

## Getting Started
This project is for demonstration only. See the documentation for more details.

## Modular Architecture
This simulation is now organized into Python classes for each subsystem:
- **SensorSuite**: Simulates IMU, GPS, and other sensors with noise.
- **NavigationSystem**: Estimates current state from sensor data (dummy logic).
- **GuidanceSystem**: Computes desired trajectory commands (dummy logic).
- **ControlSystem**: Generates actuator commands (dummy logic).
- **ActuatorSuite**: Simulates actuators (no real hardware).
- **TrajectoryVisualizer**: Plots a simulated, non-representative trajectory.
- **Simulation**: Orchestrates the modular simulation, running each subsystem in sequence.

Each class is heavily commented and non-operational, designed for educational demonstration only.

## How the Modules Interact
1. **SensorSuite** generates noisy sensor data.
2. **NavigationSystem** estimates the missile's state from this data.
3. **GuidanceSystem** computes dummy trajectory commands based on the state and a target.
4. **ControlSystem** generates dummy actuator commands.
5. **ActuatorSuite** receives these commands (no real effect).
6. **Simulation** updates a dummy position and records the trajectory.
7. **TrajectoryVisualizer** displays the simulated path.

## Demo
To run the simulation locally:
```bash
pip install -r requirements.txt
python simulation.py
```
You will see console output for each simulated step and a simple trajectory plot.

## Development Pipeline
See `DEVELOPMENT.md` for full details. Key points:
- Code style: PEP8
- Linting: `flake8` or `pylint`
- Testing: `pytest` (for safe, non-operational logic)
- CI/CD: GitHub Actions recommended

---

## License
MIT License 