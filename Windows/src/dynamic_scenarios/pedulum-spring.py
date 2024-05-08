from vpython import *
from readfile import * 

filename ='/home/tensem/solve-dynamic-/src/dynamic_scenarios/data_Pénduloresorte.txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)
m=data[0]
tetha=data[1]
k=data[2]

techo = box(pos=vec(0,3,0),size=vec(3.5,0.1,1),color=color.blue) #techo
#Resorte con constante(k) en dn/cm, dinas sobre centimetros 
resorte=helix(pos=vec(0,0,0),axis=vec(0,3,0),radius=0.3,constant=458607.1875 ,thickness=0.1,coils=20,color=color.red)
#masas 
masa=box(pos=vec(0,-0.2,0),size=vec(0.7,0.7,0.7),color=color.yellow)
g =-978.362 #cm/s
#propiedades de los objetos
masa.mass = 600
masa.vel=vec(0,0,0)
resorte.vel=vec(0,0,0)
masa.a=vec(0,0,0)

t=0 
dt = 0.3
while(true):
    rate(200)
    t+=dt
    masa.pos+=masa.vel*dt #actualizamos posicion de la masa 
    resorte.pos+=resorte.vel*dt #para la ilusion del movimiento hacia abajo del resorte
    resorte.axis-=masa.vel*dt #para que el resorte se elonge y se contraiga 
    resorte.vel+=masa.a*dt #para la ilusion del movimiento hacia abajo
    masa.vel+=masa.a*dt #actualizamos la velocidad de la masa 
    masa.a=vec(0,((-masa.pos.y*resorte.constant)/masa.mass)+g,0)#actualizamos la aceleracion del movimiento del bloque