from vpython import *
from readfile import * 

filename ='/home/tensem/solve-dynamic-/src/dynamic_scenarios/data_Pénduloresorte.txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)
m=data[0]
tetha=data[1]
k0=data[2]

if tetha>=90:
    tetha = 45 

g = 9.81  # Acceleration due to gravity (m/s^2)
L = 3.0   # Length of the pendulum rod (m)
k = k0 # Spring constant (N/m)
theta0 = tetha  # Initial angle (radians)
theta_dot0 = 0.0  # Initial angular velocity (radians/s)

# Scene setup
scene = canvas(title="Pendulum with Spring Compression", width=800, height=600)
scene.autoscale = False

# Ground
ground = box(pos=vector(0, -L-1, 0), size=vector(20, 0.1, 1), color=color.green)

# Pendulum bob
bob = sphere(pos=vector(L * sin(theta0), -L * cos(theta0), 0), radius=0.2, color=color.blue)

# Spring
spring = helix(pos=vector(0, 0, 0), radius=0.1, color=color.gray(0.5))

# Time setup
t = 0
dt = 0.01

# Main loop
while t<5:
    rate(100)

    # Calculate displacement and spring force
    displacement = mag(bob.pos) - L
    spring_force = -k * displacement * norm(bob.pos)
    
    # Total force
    total_force = vector(0, -g, 0) + spring_force
    
    # Angular acceleration (from the equation of motion for a pendulum)
    theta_double_dot = cross(bob.pos, total_force).z / (mag(bob.pos) ** 2 * L)
    
    # Update angular velocity and angle using Euler's method
    theta_dot0 += theta_double_dot * dt
    theta0 += theta_dot0 * dt
    
    # Update position of the pendulum bob and spring
    bob.pos = vector(L * sin(theta0), -L * cos(theta0), 0)
    spring.axis = bob.pos
    
    # Update spring length based on compression or decompression
    spring_length = L + displacement
    spring.length = spring_length
    
    # Update time
    t += dt
