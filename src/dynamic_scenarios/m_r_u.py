from readfile import *
from vpython import *
import os

# Obtener la ruta del directorio actual
dir_actual = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta al archivo .txt
filename = os.path.join(dir_actual, 'data_MUR(movimientorectilineouniforme).txt')
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)
v0=data[0]
x=data[1]

scene = canvas(title="Rectilinear Uniform Motion", width=800, height=200)
scene.autoscale = False

scene.camera.pos = vector(0, 5, 15)  # Set camera position
scene.camera.axis = vector(0, -1, -3)  # Set camera orientation

# Ground
ground = box(pos=vector(x, -1, 0), size=vector(20*x, 0.1, 1), color=color.green)

# Object
object = box(pos=vector(-x, 0, 0), size=vector(1, 1, 1), color=color.blue)

# Initial conditions
speed = v0  # Constant speed (m/s)
dt = 0.01  # Time step (s)
t=0
tf=x/speed 

# Main loop
while t<tf:
    rate(100)
    t+=dt
    # Move object
    object.pos.x += speed * dt