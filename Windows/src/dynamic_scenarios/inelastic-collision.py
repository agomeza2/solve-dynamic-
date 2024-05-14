from readfile import * 

filename ='C:\\Users\\Alex\\solve-dynamic-\\Windows\\src\\dynamic_scenarios\\data_Colisiónlinealinelástica.txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)
m1=data[0]
m2=data[1]
d=data[2]
v01=data[3]
v02=data[4]

from vpython import *

v1_initial = vector(v01, 0, 0)  # Initial velocity of the first brick (m/s)
v2_initial = vector(0, 0, 0)  # Initial velocity of the second brick (m/s)

# Scene setup
scene = canvas(title="Inelastic Collision", width=800, height=400)
scene.autoscale = False

# Bricks
brick1 = box(pos=vector(d-5, 0, 0), size=vector(1, 1, 1), color=color.blue, velocity=v1_initial)
brick2 = box(pos=vector(d+5, 0, 0), size=vector(1.5, 1.5, 1.5), color=color.red, velocity=v2_initial)

# Ground
ground = box(pos=vector(d, -1, 0), size=vector(20*d, 0.1, d*10), color=color.green)

# Time setup
dt = 0.01

# Main loop
while brick1.pos.x<=2*d:
    rate(100)
    
    # Update positions
    brick1.pos += brick1.velocity * dt
    brick2.pos += brick2.velocity * dt
    
    # Check for collision
    if brick1.pos.x + brick1.size.x / 2 >= brick2.pos.x - brick2.size.x / 2:
        # Calculate final velocity of the combined system
        v_final = (m1 * brick1.velocity + m2 * brick2.velocity) / (m1 + m2)
        
        # Update velocities (inelastic collision)
        brick1.velocity = v_final
        brick2.velocity = v_final