from readfile import * 
from vpython import * 
filename ='C:\\Users\\Alex\\solve-dynamic-\\Windows\\src\\dynamic_scenarios\\data_Péndulo.txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)
m=data[0]
theta=data[1]

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)
L = 3.0   # Length of the pendulum rod (m)
theta0 = theta  # Initial angle (radians)
theta_dot0 = 0.0  # Initial angular velocity (radians/s)

# Scene setup
scene = canvas(title="Pendulum Simulation", width=800, height=600)
scene.autoscale = False

# Ground
ground = box(pos=vector(0, -L-1, 0), size=vector(20, 0.1, 1), color=color.green)

# Pendulum rod
rod = cylinder(pos=vector(0, 0, 0), axis=vector(L * sin(theta0), -L * cos(theta0), 0), radius=0.1, color=color.gray(0.5))

# Pendulum bob
bob = sphere(pos=rod.axis, radius=0.2, color=color.blue)

# Time setup
t = 0
dt = 0.01

# Main loop
while t<10:
    rate(100)

    # Angular acceleration (from the equation of motion for a pendulum)
    theta_double_dot = -g / L * sin(theta0)
    
    # Update angular velocity and angle using Euler's method
    theta_dot0 += theta_double_dot * dt
    theta0 += theta_dot0 * dt
    
    # Update position of the pendulum bob and rod
    bob.pos = vector(L * sin(theta0), -L * cos(theta0), 0)
    rod.axis = bob.pos

    # Update time
    t += dt