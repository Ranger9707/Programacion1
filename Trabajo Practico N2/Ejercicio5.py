#Alumno: Matias Vespa

#5. Que dado tres números ingresados por el usuario nos devuelva el promedio.

#Definiciones
def promedio_numeros(numero_uno, numero_dos, numero_tres):
    return (numero_uno + numero_dos + numero_tres) / 3

def numero(cantidad):
    return float(input(f"Ingrese el {cantidad} número: "))

#Logica programa
primer = numero("primer")
segundo = numero("segundo")
tercero = numero("tercero")

promedio = promedio_numeros(primer,segundo,tercero)

print (f"El promedio de los números {primer}, {segundo} y {tercero} es {promedio}")