from readfile import * 
from vpython import * 

from readfile import *
from vpython import *
import os

# Obtener la ruta del directorio actual
dir_actual = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta al archivo .txt
filename = os.path.join(dir_actual, 'data_MURA3(movimientorectilineouniformeaceleradoenlos3ejes).txt')
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)
vx0=data[0]
x0=data[1]
ax=data[2]
ay=data[3]
vy0=data[4]
y0=data[5]
az=data[6]
vz0=data[7]
z0=data[8]

a= vector(ax, -ay, az)  # Acceleration due to gravity (m/s^2)

# Scene setup
scene = canvas(title="Parabolic Motion", width=800, height=600)
scene.autoscale = False

# Ground
ground = box(pos=vector(x0, y0-5, z0), size=vector(20, 0.1, 10), color=color.green)

# Projectile
projectile = sphere(pos=vector(x0, y0, z0), radius=0.3, color=color.red, make_trail=True, trail_type="points", retain=100)

# Initial conditions
projectile.velocity = vector(vx0, vy0, vz0)  # Initial velocity (m/s)
t = 0  # Initial time (s)
dt = 0.01  # Time step (s)

# Main loop
while projectile.pos.y >= 0:
    rate(100)
    
    # Update position
    projectile.pos += projectile.velocity * dt
    
    # Update velocity (considering gravity)
    projectile.velocity += a * dt
    
    # Update time
    t += dt
