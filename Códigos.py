#METODO 1

from machine import Pin as pin
from utime import sleep, sleep_ms
led1=pin(15,pin.OUT)
led2=pin(4,pin.OUT)
led3=pin(5,pin.OUT)
led4=pin(19,pin.OUT)
led5=pin(21,pin.OUT)
led6=pin(3,pin.OUT)
led7=pin(22,pin.OUT)
led8=pin(13,pin.OUT)
led9=pin(14,pin.OUT)

pausa = 0.2

while True:
    led1.value(1)
    sleep(pausa)
    led1.value(0)
    sleep(pausa)
    
    led2.value(1)
    sleep(pausa)
    led2.value(0)
    sleep(pausa)
    
    led3.value(1)
    sleep(pausa)
    led3.value(0)
    sleep(pausa)
         
    led4.value(1)
    sleep(pausa)
    led4.value(0)
    sleep(pausa)
    
    led5.value(1)
    sleep(pausa)
    led5.value(0)
    sleep(pausa)
    
    led6.value(1)
    sleep(pausa)
    led6.value(0)
    sleep(pausa)
    
    led7.value(1)
    sleep(pausa)
    led7.value(0)
    sleep(pausa)
    
    led8.value(1)
    sleep(pausa)
    led8.value(0)
    sleep(pausa)
    
    led9.value(1)
    sleep(pausa)
    led9.value(0)
    sleep(pausa)
    break





#METODO 2

from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausams, sleep_us as pausaAs

leda=pin(15,pin.OUT)
ledb=pin(4,pin.OUT)
ledc=pin(5,pin.OUT)
ledd=pin(19,pin.OUT)
lede=pin(21,pin.OUT)
ledf=pin(3,pin.OUT)
ledg=pin(22,pin.OUT)
ledh=pin(13,pin.OUT)
ledi=pin(14,pin.OUT)

#Hacemos la funcion
def encenderLeds(i,h,g,f,e,d,c,b,a):#Escibimos los parametros en este orden, para que enciendan de derecha a izquierda
    leda.value(a)
    ledb.value(b)
    ledc.value(c)
    ledd.value(d)
    lede.value(e)
    ledf.value(f)
    ledg.value(g)
    ledh.value(h)
    ledi.value(i)
    pausams(200)

while True:
    encenderLeds(0,0,0,0,0,0,0,0,0)
    encenderLeds(0,0,0,0,0,0,0,0,1)
    encenderLeds(0,0,0,0,0,0,0,1,0)
    encenderLeds(0,0,0,0,0,0,1,0,0)
    encenderLeds(0,0,0,0,0,1,0,0,0)
    encenderLeds(0,0,0,0,1,0,0,0,0)
    encenderLeds(0,0,0,1,0,0,0,0,0)
    encenderLeds(0,0,1,0,0,0,0,0,0)
    encenderLeds(0,1,0,0,0,0,0,0,0)
    encenderLeds(1,0,0,0,0,0,0,0,0)






#METODO 3

from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausams, sleep_us as sleepUS

leda=pin(15,pin.OUT)
ledb=pin(4,pin.OUT)
ledc=pin(5,pin.OUT)
ledd=pin(19,pin.OUT)
lede=pin(21,pin.OUT)
ledf=pin(3,pin.OUT)
ledg=pin(22,pin.OUT)
ledh=pin(13,pin.OUT)
ledi=pin(14,pin.OUT)

listaObjetos = [leda,ledb,ledc,ledd,lede,ledf,ledg,ledh,ledi]

#Creamis una funcion hacia la derecha
def derecha():
    for elemento in listaObjetos:
        
        elemento.value(1)
        pausams(50)
        elemento.value(0)
        pausams(50)
        
#Creamos una funcion hacia la izquierda
def izquierda():
        for elemento in reversed (listaObjetos):
            
            elemento.value(1)
            pausams (50)
            elemento.value(0)
            pausams(50)

while True:
    derecha()
    izquierda()


    
    
#METODO 4

from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausams, sleep_us as pausaus

#Creamos la lista que almacenara los puertos a usar
puertos = [15,4,5,19,21,3,22,13,14]
#Creamos una lista vacía que utilizaremos para agregar los datos de la lista "puertos"
todos = []

#Creamos un bucle for para agregar los elementos de la lista "puertos" en la lista "todos"
for i in puertos:
    todos.append (pin(i,pin.OUT)) #El metodo "append" nos permite agregar nuevos elementos a una lista, las cuales vamos agregando con el iterador "i", y el "OUT" nos indica que son datos de salida
print (todos)

#Creamos una funcion para hacer que las luces enciendan hacia la derecha
def secuenciaDerecha():
    for i in todos:
        for j in range(2):
            i.value(not i.value()) #Ponemos el not, para que empiece con un 1, es decir encendiendose, ya que por defecto el valor que iria en el vañlue es "0", y el "not", lo invierte, volviendolo en 1. 
            pausams(130)

#Creamos una funcion para hacer que las luces enciendan hacia la izquierda
def secuenciaIzquierda():
    for i in reversed (todos):    #Ponemos "reversed" para que se ejecute la misma instruccion que en "secuenciaDerecha", pero de manera inversa.
        for j in range(2):
            i.value(not i.value ())
            pausams(130)

#Hacemos un bucle para que se ejecuten las funciones
while True:
    secuenciaDerecha()
    secuenciaIzquierda()
 



#METODO 5

from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us
puerto=[15,2,4,5,18,21,22,23,25,33]
todos=[]
for i in puerto:
    todos.append (pin(i,pin.OUT))
print (todos)
def derecha():
    for i in todos:
        for j in range (2):
            i.value(not i.value())
            pausam(150)
def izquierda():
    for i in reversed(todos):
        for j in range (2):
            i.value(not i.value())
            pausam(150)
while True:
    derecha()
    #izquierda()
