from vpython import * 
from readfile import * 

filename ='/home/tensem/solve-dynamic-/src/dynamic_scenarios/data_Planoinclinado.txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)
m=data[0]
tetha=data[1]

if (tetha>45):
    tetha = 45 

floor=box(pos=vec(0,0,0), size=vec(25,2,2), color=color.red)
cuerpo=box(pos=vec(10,2,2), size=vec(2,2.69,1), color=color.green)

dist_cuerpox=(cuerpo.size.x)/2
dist_floorx=(floor.size.x)/2

dist_cuerpoy=(cuerpo.size.y)/2
dist_floory=(floor.size.y)/2

dist_cuerpoz=(cuerpo.size.z)/2
dist_floorz=(floor.size.z)/2

flechaguia=arrow(pos=vec(dist_floorx,dist_floory,dist_floorz), shaftwidth=0.1, axis=vec(-12.5,0,0), color=color.green)
flechaguia2=arrow(pos=vec(dist_floorx,dist_floory,dist_floorz), shaftwidth=0.1, axis=vec(-12.5,0,0), color=color.green)

theta=tetha

floor.rotate(angle=theta*pi/180,axis=vec(0,0,(floor.size.z)/2), origin=vector((floor.size.x)/2,(floor.size.y)/2,1))
cuerpo.rotate(angle=theta*pi/180,axis=vec(0,0,(floor.size.z)/2), origin=vector((floor.size.x)/2,(floor.size.y)/2,1))
flechaguia.rotate(angle=theta*pi/180,axis=vec(0,0,(floor.size.z)/2), origin=vector((floor.size.x)/2,(floor.size.y)/2,1))
    
ang = flechaguia2.axis.diff_angle(flechaguia.axis)



g=-9.8
cuerpo.m=m
t=0
cuerpo.a=vec(0,0,0)
cuerpo.vel=vec(0,0,0)
2
dt=0.0025
tfi=3
while t<tfi:
    rate(200)
    t+=dt
    cuerpo.pos+=cuerpo.vel*dt 
    cuerpo.vel+=cuerpo.a*dt 
    cuerpo.a=vec(cos(ang)*g,sin(ang)*g,0)
    