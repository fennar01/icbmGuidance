"""
ICBM Guidance System Simulation (Non-Functional, Modular)

This script simulates the theoretical structure of an ICBM guidance system for educational purposes only.
All sensitive or dangerous details are omitted or replaced with safe placeholders.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- Simulated Sensor Suite ---
class SensorSuite:
    """Simulates IMU, GPS, and other sensors with noise (non-functional)."""
    def __init__(self):
        self.noise_std = 0.1  # Simulated sensor noise

    def read(self):
        # Dummy position, velocity, attitude with noise
        position = np.array([0, 0, 0]) + np.random.normal(0, self.noise_std, 3)
        velocity = np.array([0, 0, 0]) + np.random.normal(0, self.noise_std, 3)
        attitude = np.array([0, 0, 0]) + np.random.normal(0, self.noise_std, 3)
        return {
            'position': position,
            'velocity': velocity,
            'attitude': attitude
        }

# --- Simulated Navigation System ---
class NavigationSystem:
    """Estimates current state from sensor data (non-functional)."""
    def estimate_state(self, sensor_data):
        # In reality, would use Kalman filter, etc.
        # Here, just pass through the noisy data
        return sensor_data

# --- Simulated Guidance System ---
class GuidanceSystem:
    """Computes desired trajectory commands (non-functional)."""
    def compute_guidance(self, nav_state, target):
        # In reality, would solve optimal control problems
        # Here, return dummy commands
        return {
            'desired_heading': 0,
            'desired_pitch': 0,
            'desired_velocity': 0
        }

# --- Simulated Control System ---
class ControlSystem:
    """Generates actuator commands from guidance (non-functional)."""
    def compute_actuators(self, guidance_cmd, nav_state):
        # In reality, would use PID, LQR, etc.
        # Here, return dummy actuator commands
        return {
            'thrust': 0,
            'fin_angles': [0, 0, 0, 0]
        }

# --- Simulated Actuator Suite ---
class ActuatorSuite:
    """Simulates actuators (non-functional)."""
    def actuate(self, actuator_cmd):
        # In reality, would send commands to hardware
        # Here, do nothing
        pass

# --- Trajectory Visualizer ---
class TrajectoryVisualizer:
    """Plots a simulated, non-representative trajectory."""
    def plot(self, trajectory):
        x = trajectory['x']
        y = trajectory['y']
        plt.plot(x, y)
        plt.title('Simulated ICBM Trajectory (Non-Functional)')
        plt.xlabel('Distance (km)')
        plt.ylabel('Altitude (km)')
        plt.show()

# --- Simulated Environmental Model ---
class EnvironmentalModel:
    """Simulates environmental effects (wind, gravity variations) in a non-functional way."""
    def __init__(self):
        self.wind = np.array([0.0, 0.0, 0.0])  # Dummy wind vector
        self.gravity = 9.81  # Dummy gravity (m/s^2)

    def get_environment(self, step):
        # Return dummy, non-physical environmental effects
        wind = self.wind + np.random.normal(0, 0.01, 3)  # Small random wind
        gravity = self.gravity + np.random.normal(0, 0.01)
        return {'wind': wind, 'gravity': gravity}

# --- Simulated Fault Injector ---
class FaultInjector:
    """Allows toggling simulated sensor/actuator faults for demonstration (non-functional)."""
    def __init__(self, sensor_fault=False, actuator_fault=False):
        self.sensor_fault = sensor_fault
        self.actuator_fault = actuator_fault

    def inject_sensor_fault(self, sensor_data):
        if self.sensor_fault:
            # Corrupt sensor data (dummy, non-harmful)
            return {k: v + np.random.normal(10, 5, v.shape) for k, v in sensor_data.items()}
        return sensor_data

    def inject_actuator_fault(self, actuator_cmd):
        if self.actuator_fault:
            # Corrupt actuator command (dummy, non-harmful)
            return {k: (np.array(v) + 999) if isinstance(v, (list, np.ndarray)) else v for k, v in actuator_cmd.items()}
        return actuator_cmd

# --- Main Simulation Orchestrator ---
class Simulation:
    """Orchestrates the modular simulation (non-functional, now with environment and faults)."""
    def __init__(self, sensor_fault=False, actuator_fault=False):
        self.sensors = SensorSuite()
        self.navigation = NavigationSystem()
        self.guidance = GuidanceSystem()
        self.control = ControlSystem()
        self.actuators = ActuatorSuite()
        self.environment = EnvironmentalModel()
        self.faults = FaultInjector(sensor_fault, actuator_fault)
        self.visualizer = TrajectoryVisualizer()
        self.trajectory = {'x': [], 'y': []}
        self.target = np.array([100, 0, 0])  # Dummy target

    def run(self, steps=20):
        print("ICBM Guidance System Simulation (Non-Functional, Modular)")
        print("This is an educational demonstration. No real guidance or control is performed.")
        state = {'position': np.array([0, 0, 0])}
        for step in range(steps):
            env = self.environment.get_environment(step)
            sensor_data = self.sensors.read()
            sensor_data = self.faults.inject_sensor_fault(sensor_data)
            nav_state = self.navigation.estimate_state(sensor_data)
            guidance_cmd = self.guidance.compute_guidance(nav_state, self.target)
            actuator_cmd = self.control.compute_actuators(guidance_cmd, nav_state)
            actuator_cmd = self.faults.inject_actuator_fault(actuator_cmd)
            self.actuators.actuate(actuator_cmd)
            # Simulate position update (dummy, non-physical, includes wind)
            state['position'] = state['position'] + np.random.normal(1, 0.2, 3) + env['wind']
            self.trajectory['x'].append(state['position'][0])
            self.trajectory['y'].append(state['position'][2])
            print(f"Step {step}: Simulated modular GNC cycle (no real actions)")
        self.visualizer.plot(self.trajectory)

# --- Scenario Selector ---
class ScenarioSelector:
    """Allows selection of demonstration scenarios (non-functional, educational)."""
    def __init__(self):
        self.scenarios = {
            'normal': {'sensor_fault': False, 'actuator_fault': False},
            'sensor_fault': {'sensor_fault': True, 'actuator_fault': False},
            'actuator_fault': {'sensor_fault': False, 'actuator_fault': True},
            'both_faults': {'sensor_fault': True, 'actuator_fault': True},
        }

    def select(self, scenario_name):
        return self.scenarios.get(scenario_name, self.scenarios['normal'])

if __name__ == "__main__":
    # Example: scenario selection
    selector = ScenarioSelector()
    # Change the scenario name below to try different demonstration modes
    scenario = selector.select('sensor_fault')  # Options: 'normal', 'sensor_fault', 'actuator_fault', 'both_faults'
    sim = Simulation(**scenario)
    sim.run() 