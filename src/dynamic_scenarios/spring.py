from readfile import * 
from vpython import * 

import os

# Obtener la ruta del directorio actual
dir_actual = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta al archivo .txt
filename = os.path.join(dir_actual, 'data_Resorte.txt')

data_array = read_file(filename)
data_array1 = filter_numbers(data_array)
data = float_array(data_array1)
m=data[0]
k_s=data[1]
x0=data[2]

L0=.1 #the natural length of the spring
k=k_s #spring constant

#the holder is the top plate for the spring
holder= box(pos=vec(-.1,.1,0), size=vec(.1,.005,.1))

#the ball and the spring should be obvious
#note that the ball has a trail
ball=sphere(pos=vec(-.1,-L0+.1,0), radius=0.02, color=color.red, make_trail=True)
spring=helix(pos=holder.pos, axis=ball.pos-holder.pos, radius=.02, coils=10)

ball.m=m #mass of the ball in kg
ball.p=ball.m*vec(0,0,0) #starting momentum mass times velocity

dr=vec(0,x0,0) #this is the displacement of the spring
ball.pos=ball.pos+dr

g=vec(0,-9.8,0) #gravitational field
t=0
dt=0.01 #size of the time step

#putting the loop as "while True" means it runs forever
#you could change this to while t< 10: or something
while t<3: 
    rate(100) #this says 100 calculations per second
    
    #L is the length of the spring, from the holder to the ball
    L=ball.pos-holder.pos
    
    #remember that mag(R) gives the magnitude of vector R
    #remember that norm(R) gives the unit vector for R
    Fs=-k*(mag(L)-L0)*norm(L) #this is Hooke's law
    
    #this calculates the net force
    F=Fs+ball.m*g
    
    #update the momentum
    ball.p=ball.p+F*dt
    
    #update the position of the ball
    ball.pos= ball.pos +ball.p*dt/ball.m
    #this next line updates the spring
    spring.axis=ball.pos-holder.pos
    