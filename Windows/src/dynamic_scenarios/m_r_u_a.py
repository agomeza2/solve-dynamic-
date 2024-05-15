from readfile import *
from vpython import *
import os

# Obtener la ruta del directorio actual
dir_actual = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta al archivo .txt
filename = os.path.join(dir_actual, 'data_MURA(movimientorectilineouniformeacelerado).txt')

data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)
v0=data[0]
x0=data[1]
a=data[2]


scene = canvas(title="Rectilinear Uniform Accelerated Motion", width=800, height=200)
scene.autoscale = False

# Ground
ground = box(pos=vector(x0, -1, 0), size=vector(20*x0, 0.1, 10), color=color.green)

# Object
object = box(pos=vector(-x0, 0, 0), size=vector(1, 1, 1), color=color.blue)

# Initial conditions
object.velocity=vec(v0,0,0) # Initial speed (m/s)
object.acceleration = vec(a,0,0)  # Acceleration (m/s^2)
dt = 0.01  # Time step (s)

# Camera setup
scene.camera.pos = vector(0, 5, 15)  # Set camera position
scene.camera.axis = vector(0, -1, -3)  # Set camera orientation

# Main loop
while object.pos.x<=2*x0:
    rate(100)
    
    # Update velocity
    object.velocity+= object.acceleration * dt
    
    # Move object
    object.pos+= object.velocity* dt
