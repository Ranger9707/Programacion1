#Alumno Matias Vespa
#Escriba un programa que permita al usuario ingresar la base y altura de un triángulo para
#luego imprimir por pantalla la superficie total.

base_triangulo = int (input ("Ingrese la base: "))
altura_triangulo = int (input ("Ingrese la altura: "))
#Ingreso de datos

superficie_triangulo = (base_triangulo * altura_triangulo) / 2
#Calculo de la superficie

print (f"La superficie del triangulo es: {superficie_triangulo}")