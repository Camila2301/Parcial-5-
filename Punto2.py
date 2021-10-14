"""El siguiente codigo calcula e imprime
el problema 89 del taller 4
Autor: Maria Camila Vargas Giraldo 
Ultima actualización: 10 de octubre / 2021 """


#Utilizo libreria random para usar las funciones de los numeros aleatorios.
import random 
divisores={} #Numeros divisores
p={} #Numero perfecto
np={} #Numero no perfecto

def esp(x):#creamos la funcion que comprueba si x es un numero perfecto
    suma=0
    for i in range(1,x):
        if x % i == 0:
            suma+=i #si la division da modulo 0 a la variable suma se le suma i 
            divisores[i]=i
    return suma == x #si la suma es igual a x el retorno dara True sino dara False

n=int(input("ingrese el rango max de la muestra ")) #aqui solicitamos el numero de mayor del rango a numeros a escoger
x=random.randint(1,n) #se escoge el numero al azar entre 1 y n 
print("el numero al azar escogido fue",x)
    
if esp(x)==True: #condicional para imprimir 
    print(x," es un numero p")
    print("sus divisores son :")
    listaDeDivisores = divisores.values() #en una variable sacamos los valores del diccionario divisores
    listaDeDivisores = list(listaDeDivisores) #convertimos la variable en una lista
    print(listaDeDivisores)
else: 
    print(x, "no es un numero p")
    print("sus divisores son :")
    listaDeDivisores = divisores.values()
    listaDeDivisores = list(listaDeDivisores)
    print(listaDeDivisores)

for i in range(1,x+1): #con este for contamos la cantidad de numeros perfectos desde 1 hasta x+1
    if esp(i)==True:
        p[i]=i
    else:
        np[i]=i
#Contamos con una funcion len que nos ayuda a enocontrar la cantidad de numeros perfectos.                      
cont=len(p) 
print("hay entre el 1 y ",x," esta cantidad de p :",cont)
print("hay entre el 1 y ",x," esta cantidad de np :",len(np))
listap=p.values()
listap=list(listap)
print("esta es la lista de p :")
print(listap)
print("el porcentaje de numeros perfectos desde 1 hasta ",x," es ",cont/x,"%")


print("se realiza el calculo para saber si ",x," es un numero teorema")
suma=sum(listaDeDivisores)+x
h=len(listaDeDivisores)+1 #Cuantos espacios esta ocupando esta lista dependiendo de los datos
calculo=(x*h)/suma 
print("el resultado es ",calculo) 
if (x*h)%suma==0: #con este condicional si la variable calculo da residuo 0 significa que el numero x es de ore
    print(x," es un numero de teorema")
else:
    print(x," no es un numero de teorema")
