#Alumno: Matias Vespa

#17. Que muestre todos los números primos entre 0 y 100 e imprima cuántos números primos hay.

#Definiciones

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if (numero % i) == 0:
            return False
    return True

#Logica programa

cantidad_numeros_primos = 0
for num in range(101):
    if es_primo(num):
        cantidad_numeros_primos +=1
        print(num,end=" ")

print(f"\nLos numeros primeros encontrados fueron: {cantidad_numeros_primos}")