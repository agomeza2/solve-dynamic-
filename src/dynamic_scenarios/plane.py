from vpython import * 
from readfile import * 

filename ='data_MURA.txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)

floor=box(pos=vec(0,0,0), size=vec(25,2,2), color=color.red)
floor2=box(pos=vec(0,0,0), size=vec(25,2,2), color=color.blue)
cuerpo=box(pos=vec(0,0,0), size=vec(7.60,2.69,1), color=color.green)

dist_cuerpox=(cuerpo.size.x)/2
dist_floorx=(floor.size.x)/2
dist_floor2x=(floor2.size.x)/2

dist_cuerpoy=(cuerpo.size.y)/2
dist_floory=(floor.size.y)/2
dist_floor2y=(floor2.size.y)/2

dist_cuerpoz=(cuerpo.size.z)/2
dist_floorz=(floor.size.z)/2
dist_floor2z=(floor2.size.z)/2


cuerpo.pos.y=dist_cuerpoy+dist_floory
cuerpo.pos.x=-(dist_cuerpox+dist_floorx)/2

flechaguia=arrow(pos=vec(dist_floorx,dist_floory,dist_floorz), shaftwidth=0.1, axis=vec(-12.5,0,0), color=color.green)
flechaguia2=arrow(pos=vec(dist_floorx,dist_floory,dist_floorz), shaftwidth=0.1, axis=vec(-12.5,0,0), color=color.green)

theta=13.86

floor.rotate(angle=theta*pi/180,axis=vec(0,0,-(floor.size.z)/2), origin=vector((floor.size.x)/2,(floor.size.y)/2,1))
cuerpo.rotate(angle=theta*pi/180,axis=vec(0,0,-(floor.size.z)/2), origin=vector((floor.size.x)/2,(floor.size.y)/2,1))
flechaguia.rotate(angle=theta*pi/180,axis=vec(0,0,-(floor.size.z)/2), origin=vector((floor.size.x)/2,(floor.size.y)/2,1))
    
U=tan(ang)
ang = flechaguia2.axis.diff_angle(flechaguia.axis)



g=9.8
cuerpo.m=0.781
t=0
U=tan(ang)

N=cuerpo.m*g*cos(theta)
a=((g*sin(theta))-(g*cos(theta)*U))
Fr= N*U
Fc=cuerpo.m*g*sin(ang)
label( pos=vec(0,-2,1),text='grados de inclinación='+ang*180/pi+'')
label( pos=vec(0,-3,1),text='Coeficiente de fricción estática='+U+'')
label( pos=vec(0,-4,1),text='Fuerza de fricción='+Fr+'')
label( pos=vec(0,-5,1),text='Fuerza experimentada cuerpo='+Fc+'')

ay=g*sin(ang)
ax=g*cos(ang)*U

dt=0.001
tfi=10
while t<tfi:
    rate(10)
    t=t+dt
    cuerpo.pos.x=cuerpo.pos.x+1/2*(ax*dt^2)
    
    cuerpo.pos.y=cuerpo.pos.y+((1/2*cos(ay*dt^2))/0.743494423792)
    print(ax)