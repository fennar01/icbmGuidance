# Rocket Guidance System Simulation (Non-Functional)

**DISCLAIMER: This project is a non-functional, educational simulation of a rocket guidance system. It is intended solely for demonstration purposes for journalists and researchers. No part of this project is operational or intended for real-world use.**

## Project Overview
This repository simulates the theoretical architecture and logic of a rocket guidance system using open source tools. All code and documentation are intentionally incomplete and non-operational, with sensitive or dangerous elements omitted or replaced with safe placeholders.

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
- `high_wind`: Simulates strong wind conditions to illustrate environmental challenges.
- `gravity_anomaly`: Simulates a gravity anomaly to show how unusual environmental effects might impact guidance.
- `gps_outage`: Simulates a GPS outage (degraded navigation) to demonstrate the effect of sensor loss.

To change the scenario, edit the following lines in `simulation.py`:

```python
selector = ScenarioSelector()
scenario = selector.select('sensor_fault')  # Options: 'normal', 'sensor_fault', 'actuator_fault', 'both_faults', 'high_wind', 'gravity_anomaly', 'gps_outage'
sim = Simulation(**scenario)
sim.run()
```

## Adding New Scenarios

To contribute a new demonstration scenario, add an entry to the `scenarios` dictionary in the `ScenarioSelector` class in `simulation.py`. Each scenario can specify sensor/actuator faults, environmental mode, and navigation degradation. For example:

```python
'custom_scenario': {
    'sensor_fault': True,
    'actuator_fault': False,
    'env_mode': 'high_wind',
    'nav_degraded': True
}
```

All new scenarios must be clearly non-functional and serve an educational purpose.

## Using the Command-Line Scenario Selection

The simulation now supports interactive scenario selection via the command line. When you run `simulation.py`, you will be prompted to select a demonstration scenario from the available options. For example:

```
Select a demonstration scenario:
1. normal
2. sensor_fault
3. actuator_fault
4. both_faults
5. high_wind
6. gravity_anomaly
7. gps_outage
Enter the number of your choice: 
```

The simulation will then run with the selected scenario, making it easy to demonstrate different educational cases interactively.