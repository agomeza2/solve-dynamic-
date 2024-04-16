from readfile import * 
from vpython import* 
filename ='/home/tensem/solve-dynamic-/src/dynamic_scenarios/data_MURAXAZA(movimiento rectilineo uniforme acelerado en ejes x,z).txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)

floor=box(pos=vec(0,-.02,0), size=vec(2,.02,.4))
ball=sphere(pos=vec(-1,0,0), radius=0.02, color=color.red, make_trail=True)
g=vec(0,-9.8,0)
ball.m=0.1 v0=4.0
theta=60 #degrees ball.p=ball.m*v0*vec(cos(theta*pi/180),sin(theta*pi/180),0)
t=0 dt=0.01

while ball.pos.y>=0: rate(100)
Fnet = ball.p = ball.pos = t=t+dt