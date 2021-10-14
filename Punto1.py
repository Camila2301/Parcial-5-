"""El siguiente codigo calcula e imprime
Simulacion para estimar el valor teorico de la probabilidad enunciado en el teorema de 6 / π ^ 2
Autor: Maria Camila Vargas Giraldo 
Ultima actualización: 10 de octubre / 2021 """

#La siguiente funcion se queda solo con los valores que estan repetidos.
def frecuencia(lista):
    f = []
    unique_list = list(set(lista)) 
    for i in unique_list:
        f.append(lista.count(i))
    return len(f)

#La siguiente funcion toma un numero que sea postivo y mayor a 1 y muestra ademas sus numeros primos teniendo como resultado en su salida un vector..
def descomponer_numero(n):   
    Numero_primo = 2
    Numeros = []
    
    while n>1:
        if n % Numero_primo == 0:# Este condicional sirve para determinar si da como residuo cero.
            n //= Numero_primo  
            Numeros.append(Numero_primo)
            
        else:
            Numero_primo += 1 
            
    return Numeros #devuelve el vector de factores primos con repeticiones   


# calcula la cantidad de enteros libres de cuadrados hasta un n
def libre_cuadrados(n):
    x = 0
    for v in range(2,n+1,1):
        lista_Numeros = descomponer_numero(v)
        
        if  len(lista_Numeros) == frecuencia(lista_Numeros):
            x=x+1
            
        else:
            continue
            
    print('Cantidad de enteros libres:', x)
    print('P(v libre)=', x/n)


for n in range(2,100,1):
    print(libre_cuadrados(n))