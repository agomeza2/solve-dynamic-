from readfile import * 
from vpython import* 
filename ='C:\\Users\\Alex\\solve-dynamic-\\Windows\\src\\dynamic_scenarios\\data_MURAXAZA(movimientorectilineouniformeaceleradoenejesx,z).txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)
vx0=data[0]
x0=data[1]
ax=data[2]
vy0=data[3]
y0=data[4]
vz0=data[5]
z0=data[6]
az=data[7]

a= vector(ax, 0, az)  # Acceleration due to gravity (m/s^2)

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
