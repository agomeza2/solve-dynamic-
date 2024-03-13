from vpython import * 
from readfile import * 

filename ='data_Plano inclinado polea.txt'
data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)

plano2 = box(pos=vec(0,4.45,0),size=vec(20,1,20),axis=vec(1,-0.2,0),color=color.yellow) #planos amarillos
plano1 = box(pos=vec(-20,5,0),size=vec(20,1,20),axis=vec(1,0.2,0),color=color.yellow)
bloque2=box(pos=vec(0,6,0),size=vec(7.626,2.729,5),axis=vec(1,-0.2,0),color=color.red)#bloque de la derecha 
bloque1=box(pos=vec(-20,6.7,0),size=vec(7.626,2.729,5),axis=vec(1,0.2,0),color=color.blue)#bloque de la izquierda
polea_eje =arrow(pos=vec(-10,4.3,0),axis=vec(0,5,0),color=color.blue) #polea
polea =sphere(pos=vec(-10,8.4,0),radius=0.7,color=color.blue)
cuerda_izq = cylinder(pos=vec(-15.8,7,0),axis=vec(6,1.3,0), radius=0.4,color=color.red)
cuerda_der =cylinder(pos=vec(-10,8.3,0),axis=vec(6,-1.3,0), radius=0.4,color=color.red) 
piso=box(pos=vec(-10,0.553,0), size=vec(40,1,40),color=color.green)#piso

bloque1.mass = 0.4  #masa del bloque azul
bloque2.mass=0.3 #masa del bloque rojo 
bloque1.vel=vec(0,0,0) #velocidades inciales
bloque2.vel=vec(0,0,0)
cuerda_der.vel=vec(0,0,0) 
bloque1.a=vec(0,0,0)#aceleracion inicial
bloque2.a=vec(0,0,0)
uk1 = 0.1 #coeficiente cinetico del bloque azul
uk2 = 0.2 #coeficiente cinetico del bloque rojo 
theta_1=atan(plano1.axis.y/plano1.axis.x) #angulo izquierdo
theta_2=atan(plano2.axis.y/plano2.axis.x) #angulo derecho 
g=-9.77412 #aceleracion de la gravedad en el Campus Universitario  
#aceleracion del sistema 
a=g*((bloque2.mass*(sin(theta_2)*uk2+cos(theta_2))-bloque1.mass*(sin(theta_1)*uk1+cos(theta_1)))/(bloque1.mass-bloque2.mass))
t=0 #tiempo incial  
dt =0.0025 #delta de t 

while t<5:
  rate(200)
  t+=dt
  bloque1.pos+=bloque1.vel*dt #actualizamos posicion
  bloque2.pos+=bloque2.vel*dt
  cuerda_der.axis+=cuerda_der.vel*dt
  bloque1.vel+=bloque1.a*dt #actualizamos velocidad
  bloque2.vel+=bloque2.a*dt
  cuerda_der.vel+=bloque2.a*dt
  bloque1.a=vec(cos(theta_1)*a,sin(theta_1)*a,0) #aceleracion constante
  bloque2.a=vec(cos(theta_2)*a,sin(theta_2)*a,0)
  if not bloque1.pos.x<-14.65: #Evitar que el bloque se salga del plano 
        break