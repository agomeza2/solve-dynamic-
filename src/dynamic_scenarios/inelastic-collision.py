from readfile import * 

import os

# Obtener la ruta del directorio actual
dir_actual = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta al archivo .txt
filename = os.path.join(dir_actual, 'data_Colisiónlinealinelástica.txt')

data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)
m1=data[0]
m2=data[1]
d=data[2]
v01=data[3]

from vpython import *
scene.title = "Colisión Inelástica entre Dos Ladrillos"
scene.width = 800
scene.height = 600

# Parámetros iniciales
L = 2.0  # Longitud del ladrillo
W = 2.0  # Ancho del ladrillo
H = 2.0  # Altura del ladrillo

# Ladrillo en movimiento
background =box(pos=vector(d,-1,0),size=vector(d+40,0.3,10),color=color.green)
brick1 = box(pos=vector(-5, 0, 0), size=vector(L, H, W), color=color.red)
brick1.velocity = vector(2, 0, 0)  # Velocidad inicial del ladrillo 1
brick1.mass = 2.0  # Masa del ladrillo 1

# Ladrillo en reposo
brick2 = box(pos=vector(0, 0, 0), size=vector(L, H, W), color=color.blue)
brick2.velocity = vector(0, 0, 0)  # Velocidad inicial del ladrillo 2
brick2.mass = 3.0  # Masa del ladrillo 2

# Tiempo y delta de tiempo
t = 0
dt = 0.01

while t < 10:
    rate(100)
    
    # Movimiento de los ladrillos
    brick1.pos += brick1.velocity * dt
    brick2.pos += brick2.velocity * dt
    
    # Detección de colisión
    if brick1.pos.x + L/2 >= brick2.pos.x - L/2:
        # Ajustar posiciones para que los ladrillos queden pegados
        overlap = (brick1.pos.x + L/2) - (brick2.pos.x - L/2)
        brick1.pos.x -= overlap / 2
        brick2.pos.x += overlap / 2
        
        # Calcular velocidad final
        total_mass = brick1.mass + brick2.mass
        brick1.velocity = (brick1.mass * brick1.velocity + brick2.mass * brick2.velocity) / total_mass
        brick2.velocity = brick1.velocity
        
        # La colisión ocurre una vez, luego los ladrillos se mueven juntos
        break
    
    t += dt

# Continuar movimiento después de la colisión
while t < 20:
    rate(100)
    
    # Movimiento conjunto de los ladrillos después de la colisión
    brick1.pos += brick1.velocity * dt
    brick2.pos += brick2.velocity * dt
    
    t += dt