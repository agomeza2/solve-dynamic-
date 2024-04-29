from vpython import * 
from readfile import * 

filename ='/home/tensem/solve-dynamic-/src/dynamic_scenarios/data_Colisión lineal elástica.txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)
m1=data[0]
m2=data[1]
d=data[2]
v01=data[3]
v02=data[4]
carroiz = box(pos=vec(-10,0,0),size=vec(2,2,2),color = color.blue)
carrode = box(pos=vec(d+10,0,0),size=vec(2,2,2),color = color.red)
flechaiz = arrow(pos=vec(-10,0,0),axis=vec(3,0,0),color=color.yellow)
piso = box(pos=vec(0,-0.9,0), size=vec(40,0.5,10),color=color.green)

carroiz.vel=vec(v01,0,0) #blocks velocity 
carrode.vel=vec(v02,0,0)
flechaiz.vel=vec(v01,0,0)
carroiz.mass = m1 #blocks mass 
carrode.mass =m2 

t = 0
t2 =0
t3 =0 
dt = 0.0025

while t<15:
    rate(650)
    t += dt
    carroiz.pos=carroiz.pos + carroiz.vel*dt
    flechaiz.pos=flechaiz.pos + flechaiz.vel*dt
    carrode.pos = carrode.pos+carrode.vel*dt
    if not flechaiz.pos.x<8:
        carrode.vel=((2*carroiz.mass)/(carroiz.mass+carrode.mass))*carroiz.vel
        flechade = arrow(pos=vec(10,0,0),axis=vec(3,0,0),color=color.yellow)
        flechade.vel=((2*carroiz.mass)/(carroiz.mass+carrode.mass))*carroiz.vel
        flechade.pos = flechade.pos + flechade.vel*dt
        carroiz.vel=((carroiz.mass-carrode.mass)/(carroiz.mass+carrode.mass))*carroiz.vel
        flechaiz.vel=((carroiz.mass-carrode.mass)/(carroiz.mass+carrode.mass))*flechaiz.vel
        if not carroiz.vel.x>=0:
            flechaiz.axis=flechaiz.axis*-1    
        break
      
while t2<3:
    rate(650)
    t2 += dt
    carroiz.pos = carroiz.pos + carroiz.vel*dt
    flechaiz.pos = flechaiz.pos + flechaiz.vel*dt 
    carrode.pos = carrode.pos + carrode.vel*dt
    flechade.pos = flechade.pos + flechade.vel*dt
    