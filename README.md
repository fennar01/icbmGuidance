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

## Planned Features
The following enhancements are planned to further increase the educational value and sophistication of the simulation:
- **EnvironmentalModel**: Simulate environmental effects (e.g., wind, gravity variations) in a non-functional way.
- **FaultInjector**: Introduce simulated sensor/actuator failures for scenario-based learning.
- **Advanced Visualizations**: Add 3D trajectory plots, error ellipses, and more.
- **Scenario Selection Interface**: Allow users to select different demonstration scenarios (all non-functional).

Contributions are welcome! See `DEVELOPMENT.md` for safe contribution guidelines.

## New Modules

### EnvironmentalModel
Simulates environmental effects such as wind and gravity variations. These effects are purely illustrative and do not represent real-world physics.

### FaultInjector
Allows toggling simulated sensor and actuator faults for demonstration purposes. Faults are non-harmful and only affect the dummy data used in the simulation.

### ScenarioSelector
Allows users to select between different demonstration scenarios:
- `normal`: No faults
- `sensor_fault`: Simulated sensor faults only
- `actuator_fault`: Simulated actuator faults only
- `both_faults`: Both sensor and actuator faults

To change the scenario, edit the following lines in `simulation.py`:

```python
selector = ScenarioSelector()
scenario = selector.select('sensor_fault')  # Options: 'normal', 'sensor_fault', 'actuator_fault', 'both_faults'
sim = Simulation(**scenario)
sim.run()
```

## Using Faults and Environmental Effects
You can enable or disable sensor and actuator faults by passing arguments to the `Simulation` class in `simulation.py`:

```python
sim = Simulation(sensor_fault=True, actuator_fault=False)
sim.run()
```

Environmental effects are always simulated as small random variations in wind and gravity, and are used in the dummy position update step.

## Upcoming Advanced Visualizations
To further enhance the educational value of this simulation, the following visualization features are planned:
- **3D Trajectory Plots**: Visualize the simulated missile path in three dimensions.
- **Error Ellipses**: Illustrate uncertainty in position or trajectory due to simulated sensor noise or faults.

These features will be added in future updates. Contributions and suggestions are welcome!

### 3D Trajectory Visualization
The simulation now includes a 3D trajectory plot, in addition to the 2D plot. The 3D plot visualizes the simulated missile path in downrange, crossrange, and altitude dimensions. This feature is for educational purposes only and does not represent real-world physics or guidance.

Both 2D and 3D plots are generated at the end of each simulation run to help illustrate the modular structure and theoretical possibilities of missile guidance visualization.

---

## License
MIT License 