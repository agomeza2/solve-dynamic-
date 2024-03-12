from vpython import * 
#creamos los objetos 
plano = box(pos=vec(0,4.45,0),size=vec(20,1,20),axis=vec(1,0,0),color=color.yellow)
bloque=box(pos=vec(5,7.5,0),size=vec(7.626,2.729,5),axis=vec(1,0,0),color=color.red)
piso=box(pos=vec(0,0.553,0), size=vec(35,1,35),color=color.green)

#propiedades del bloque 
bloque.mass=5
bloque.vel=vec(0,0,0)
bloque.a=vec(0,0,0)
theta =0 #angulo inicial del plano y del bloque

a=0 
t=0
t1=0
dt=0.0025 #delta de t y t1
g=-9.77412 #valor de la gravedad en el Observatorio de la Ciudad Universitaria
uk=0.1 #coeficiente cinetico
us=0.30573 #coeficiente estatico

while t<5: #primer movimiento inclinacion del plano, bloque estacionario 
    rate(500)
    t+=dt
    plano.axis.y+=dt #inclinamos el plano amarillo 
    tange = tan(plano.axis.y/plano.axis.x) #tangente del angulo theta
    if tange<1:
      bloque.axis.y=tange*bloque.axis.x #inclinamos el objeto 
    if tange>us: #condicion donde el objeto empieza su movimiento
        break #finaliza la inclinacion del plano 

theta=atan(plano.axis.y/plano.axis.x) #angulo de inclinacion
a =g*(sin(theta)-uk*cos(theta)) #aceleracion

while t1<10: #segundo movimiento el bloque en movimiento 
    rate(500)
    t1+=dt
    bloque.pos+=bloque.vel*dt #actualizamos posicion
    bloque.vel+=bloque.a*dt #actualizamos velocidad
    bloque.a=vec(cos(theta)*a,sin(theta)*a,0) #aceleracion constante repartida por sus componentes 
    if not bloque.pos.x>-6.45: #Evitar que el bloque se salga del plano 
        break