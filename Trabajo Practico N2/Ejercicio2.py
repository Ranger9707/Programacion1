#Alumno: Matias Vespa

#2. Que reciba un número entero positivo y una potencia a elevar y que nos devuelva el resultado.

#Definiciones
def calcular_numero(numero, potencia):
    if numero <= 0:
        return "El numero a potenciar debe ser un numero entero positivo."
    else:
        return numero ** potencia


#Logica programa
numero_entero = int(input("Ingrese un número entero positivo como base: "))

potencia = int(input("Ingrese el número con el que desea elevar al anterior: "))

resultado = calcular_numero(numero_entero, potencia)

print(f"El resultado de {numero_entero} elevado a {potencia} es: {resultado}")