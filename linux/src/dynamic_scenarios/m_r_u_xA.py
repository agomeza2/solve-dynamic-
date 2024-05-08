from readfile import * 
from vpython import * 
filename ='/home/tensem/solve-dynamic-/src/dynamic_scenarios/data_MURAXA(movimiento rectilineo uniforme acelerado en el eje x).txt'
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

floor=box(pos=vec(x0,y0-.02,z0), size=vec(2,.02,.4))
ball=sphere(pos=vec(-1,y0,z0), radius=0.02, color=color.red, make_trail=True)
a=vec(ax,0,0)
v=vec(vx0,vy0,vz0) 
ball.v=v
ball.a=a
tetha=30*pi/180
phi=60*pi/180
t=0 
dt=0.25

while t<50: 
    rate(200)
    t+=dt 
    ball.pos+=ball.v*dt
    ball.v+=ball.a*dt
    ball.a+=vec(cos(tetha)*sin(phi)*ax,sin(tetha)*sin(phi)*ay,cos(phi)*az)
