from vpython import* 
from readfile import * 

filename ='data_MURA.txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)

# creamos la cuerda con cilindros 
cuerda_h = cylinder(pos=vec(-5.5,0,0),axis=vec(8.5,0,0), radius=0.1,color=color.yellow)
cuerda_v =cylinder(pos=vec(-5.5,0,0),axis=vec(0,-5,0),radius=0.1,color=color.yellow)
#creamos la polea con una esfera y una flecha 
polea =sphere(pos=vec(-5.5,0,0),radius=0.2,color=color.blue)
eje_polea=arrow(pos=vec(-5,-0.8,0),axis=vec(-0.5,0.85,0),color=color.blue)
#creamos la superficie (mesa)
mesa = box(pos=vec(0,-0.8,0), size=vec(10,0.1,10),color=color.green)
#creamos los bloques (arriba-azul,abajo-rojo) 
b_arriba = box(pos=vec(3,0,0),size=vec(1.5,1.5,1.5),color = color.blue)
b_abajo= box(pos=vec(-5.5,-5,0),size=vec(1,1,1),color = color.red)
    
#masas y velocidades iniciales
b_arriba.mass=5 #bloque azul con 5 veces mas masa
b_abajo.mass=1
b_arriba.vel=vec(0,0,0)
b_abajo.vel=vec(0,0,0)
cuerda_h.vel=vec(0,0,0)
cuerda_v.vel=vec(0,0,0)

g=-9.77412 #valor de la gravedad en Bogota en el Observatorio de la Ciudad universitaria
uk=0.1 #coeficiente de friccion cinetico 
t=0 #tiempo 
dt=0.0025 #delta de t 
#aceleracion del movimiento segun el analisis del DCL
a=g*((b_abajo.mass-b_arriba.mass*uk)/(b_arriba.mass-b_abajo.mass)) 

if a>0: #para evitar problemas con la direccion del movimiento
  b_abajo.a=vec(0,-a,0)
  b_arriba.a=vec(-a,0,0)
else:
  b_abajo.a=vec(0,a,0)
  b_arriba.a=vec(a,0,0)
  
while t<5:
    rate(300)
    b_abajo.pos+=b_abajo.vel*dt #actualizo posicion del bloque rojo 
    b_abajo.vel+=b_abajo.a*dt #actualizo velocidad del bloque rojo
    b_arriba.pos+=b_arriba.vel*dt #actualizo posicion del bloque azul 
    b_arriba.vel+=b_arriba.a*dt #actualizo velocidad del bloque azul
    cuerda_h.axis.x+=cuerda_h.vel.x*dt #realizo el mismo procedimiento con la cuerda
    cuerda_v.axis.y+=cuerda_v.vel.y*dt
    if a>0:   #para evitar problemas con la direccion del movimiento
      cuerda_h.vel.x-=a*dt
      cuerda_v.vel.y-=a*dt
    else:
      cuerda_h.vel.x+=a*dt
      cuerda_v.vel.y+=a*dt
      
    t+=dt
    if not b_arriba.pos.x>-4.15: #condicion para cuando el bloque azul se estrella con la polea
        break