#Alumno: Matias Vespa

#4. Que dada la base y altura de un triángulo nos calcule su área.

#Definiciones
def area_triangulo(base, altura):
    return (0.5 * base * altura)

#Logica programa
base_dada = float(input("Ingrese la base del triangulo: "))
altura_dada = float(input("Ingrese la altura del triangulo: "))

area = area_triangulo(base_dada, altura_dada)

print(f"El area del triangulo es {area}")