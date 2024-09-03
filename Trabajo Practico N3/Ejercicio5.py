# 5. Escriba un programa Python que solicite al usuario el ingreso de números enteros. Cuando el usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos. 
# Cada uno de los números ingresados por el usuario deberá ser almacenado en una lista. A continuación, realice las siguientes tareas:
#   A. Determinar el máximo.
#   B. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
#   C. Determinar el mínimo.
#   D. Calcular la multiplicación de todos los números de la lista.
#   E. Contar los valores pares e impares.
#   F. Remover los elementos repetidos.

numeros_enteros = []

def entrada_numeros():
    
    while True:
        solicite_numeros  = input("Ingrese numeros enteros o escriba 'fin para terminar': ")
        
        if solicite_numeros == "fin":
            break
        
        else:
            numero = int(solicite_numeros)
            numeros_enteros.append(numero)
            
    print(f"Numeros ingresados: {numeros_enteros}\n")
    
entrada_numeros()

numeros_sin_repetir = []
for numero in numeros_enteros:
    if numero not in numeros_sin_repetir:
        numeros_sin_repetir.append(numero)

numeros_sin_repetir.sort(reverse=True)
numeros_enteros.sort(reverse=True)

#Elimino los numeros repetidos al principio para poder usarlo en otros puntos, creo dos listas diferentes para usarlas en cada caso pedido
#lo hice al principio para no romper las consignas de los otros puntos y dar datos erroneos en el caso de los numeros pares o las multiplicaciones.
#Tambien ordene ambas listas de mayor a menor, si bien no es pedido es util para poder sacar el segundo maximo en las listas y tambien se ven de forma ordenada.

#A
maximo = max(numeros_enteros)
print(f"El numero máximo es: {maximo}\n")

#B
print(f"El segundo numero maximo es: {numeros_sin_repetir[1]}\n")

#C
minimo = min(numeros_enteros)
print(f"El numero minimo es: {minimo}\n")

#D
producto = 1
for numero in numeros_enteros:
    producto *= numero
print (f"La multiplicación de todos los números de la lista es: {producto}\n")

#E
pares = 0
impares = 0
for numero in numeros_enteros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Cantidad de números pares: {pares}\n")
print(f"Cantidad de números impares: {impares}\n")

#F
print(f"Lista sin numeros repetidos: {numeros_sin_repetir}")