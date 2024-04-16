from readfile import * 
from vpython import * 
filename ='/home/tensem/solve-dynamic-/src/dynamic_scenarios/data_Resorte.txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)
#variables de entrada en g, para tener en cuenta Un Newton equivale a 102.212g con la gravedad en Bogota 
print("Para tener en cuenta: 'Un Newton equivale aproximadamente a 102.212g ' ") 
m1 = float(input("Ingrese la masa #1 en gramos"))
m2 = float(input("Ingrese la masa #2 en gramos"))
m3 = float(input("Ingrese la masa #3 en gramos"))

techo = box(pos=vec(0,3,0),size=vec(7,0.1,1),color=color.blue) #techo
#Resortes con constante(k) en dn/cm, dinas sobre centimetros 
resorte1=helix(pos=vec(-3,0,0),axis=vec(0,3,0),radius=0.3,constant=502060 ,thickness=0.1,coils=20,color=color.red) 
resorte2=helix(pos=vec(0,0,0),axis=vec(0,3,0),radius=0.3,constant=471714,thickness=0.1,coils=20,color=color.yellow)
resorte3=helix(pos=vec(3,0,0),axis=vec(0,3,0),radius=0.3,constant=101741,thickness=0.1,coils=20,color=color.green)
masa1=box(pos=vec(-3,-0.2,0),size=vec(0.7,0.7,0.7),color=color.red) 
#masas 
masa2=box(pos=vec(0,-0.2,0),size=vec(0.7,0.7,0.7),color=color.yellow)
masa3=box(pos=vec(3,-0.2,0),size=vec(0.7,0.7,0.7),color=color.green)

g=-978.362 #valor de la gravedad en Bogota en cm/s 
v = 0.4 #velocidad constante del movimiento se puede cambiar para mejorar el tiempo de la simulacion
#propiedades de los objetos 
resorte1.vel=vec(0,-v,0)
resorte2.vel=vec(0,-v,0)
resorte3.vel=vec(0,-v,0)
masa1.vel=vec(0,-v,0)
masa2.vel=vec(0,-v,0)
masa3.vel=vec(0,-v,0)
masa1.mass=m1
masa2.mass=m2
masa3.mass=m3

#Fuerzas generadas por las masas (Pesos)  
W1=g*masa1.mass
W2=g*masa2.mass
W3=g*masa3.mass

#distancias generadas por las masas 
d1=W1/resorte1.constant
d2=W2/resorte2.constant
d3=W3/resorte3.constant

#Imprimo la respuesta de la distancia 
print("La distancia de elongacion del resorte #1 es: ",-d1,"cm,",-d1*10,"mm")
print("La distancia de elongacion del resorte #2 es: ",-d2,"cm,",-d2*10,"mm")
print("La distancia de elongacion del resorte #3 es: ",-d3,"cm,",-d3*10,"mm")

t=0
dt =0.0025
dt1_0 =dt*-masa1.vel.y #para cuadrar con la velocidad 
dt1_1 =dt*-masa1.vel.y
dt1_2=dt*-masa1.vel.y
while t<30:
  rate(200)
  t+=dt
  resorte1.pos+=resorte1.vel*dt #cambio la posicion y la propiedad axis para simular el elongamiento de los resortes
  resorte1.axis.y+=dt1_0
  resorte2.pos+=resorte2.vel*dt
  resorte2.axis.y+=dt1_1
  resorte3.pos+=resorte3.vel*dt
  resorte3.axis.y+=dt1_2
  masa1.pos+=masa1.vel*dt #actualizo la posicion de las masas 
  masa2.pos+=masa2.vel*dt
  masa3.pos+=masa3.vel*dt
  if masa1.pos.y <= d1-0.2: #limites del movimiento
    masa1.vel*=0
    resorte1.vel*=0
    dt1_0=0
  if masa2.pos.y <= d2-0.2: #limites del movimiento
    masa2.vel*=0
    resorte2.vel*=0
    dt1_1=0
  if masa3.pos.y <= d3-0.2: #limites del movimiento
    masa3.vel*=0
    resorte3.vel*=0
    dt1_2=0
  if masa1.vel==vec(0,0,0) and masa2.vel==vec(0,0,0) and masa3.vel==vec(0,0,0):
    break