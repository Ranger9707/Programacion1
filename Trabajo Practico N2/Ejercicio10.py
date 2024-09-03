#Alumno: Matias Vespa

"""10. Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:
a. Todos los números impares desde 1 hasta ese número separados por comas.
b. La cuenta atrás desde ese número hasta cero separados por comas.
c. Que indique si es primo o no.
d. Por último, su factorial."""

#Definiciones

def numeros_impares(numero):
    for i in range(1, int(numero+1)):
        if i % 2 != 0:
            if i == numero:
                print(i, end=" ")
            else:
                print(i, end=", ")

def cuenta_atras(numero):
    for i in range(numero, -1, -1):
        if i == 0:
            print(i)
        else:
            print(i, end=", ")

def es_primo(numero):
    if numero < 2:
        print("El número no es primo.")
        return False
    for i in range(2, numero):
        if (numero % i) == 0:
            print("El número no es primo.")
            return False
    print("El número es primo.")
    return True
        
def factorial(numero):
    if numero == 0:
        print("El factorial de 0 es 1.")
        return 1
    else:
        fact = 1
        while numero > 1:
            fact *= numero
            numero -= 1
        print(f"El factorial de {numero} es {fact}.")
        return fact

#Logica programa

numero_ingresado = int(input("Por favor, ingresa un número entero positivo: "))
print ("\n")

print ("a. Todos los números impares desde 1 hasta ese número separados por comas.:\n")
numeros_impares(numero_ingresado)
print ("\n")

print ("b. La cuenta atrás desde ese número hasta cero separados por comas.:\n")
cuenta_atras(numero_ingresado)
print ("\n")

print("c. Que indique si es primo o no.\n")
es_primo(numero_ingresado)
print ("\n")

print("d. Por último, su factorial.:\n")
factorial(numero_ingresado)
print ("\n")