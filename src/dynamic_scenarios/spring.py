from readfile import * 
from vpython import * 
filename ='/home/tensem/solve-dynamic-/src/dynamic_scenarios/data_Resorte.txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)
m=data[0]
k=data[1]
x0=data[2]

pared1=box(pos=vec(-16.9,3.5,0),size=vec(0.3,7,19.2),color=color.blue)
pared1=box(pos=vec(16.9,3.5,0),size=vec(0.3,7,19.2),color=color.red)
piso=box(pos=vec(0,0,0),size=vec(33.8,0.5,19.2),color=color.gray(0.5))
resorte_izq=helix(pos=vec(-16.8,1.75,0),axis=vec(25.11,0,0),radius=0.8,constant=55000 ,thickness=0.1,coils=20,color=color.blue)
resorte_der=helix(pos=vec(16.9,1.75,0),axis=vec(-8.69,0,0),radius=0.8,constant=57000 ,thickness=0.1,coils=20,color=color.red)
masa=box(pos=vec(8.21,1.75,0),size=vec(3.5,3.5,3.5),color=color.yellow)

g=-978.362
uk=0.3 
#propiedades de los objetos
masa.mass=289.4
masa.vel=vec(0,0,0)
masa.a=vec(0,0,0)

t=0 
dt=0.00025

while t<3:
  rate(200)
  t+=dt
  masa.pos+=masa.vel*dt
  resorte_izq.axis+=masa.vel*dt
  resorte_der.axis+=masa.vel*dt
  masa.vel+=masa.a*dt
  masa.a=vec(((-(resorte_izq.constant+resorte_der.constant)/masa.mass)*masa.pos.x)+uk*g,0,0)