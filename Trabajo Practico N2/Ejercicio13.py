#Alumno: Matias Vespa

"""13. Que resuelva el siguiente problema: los alumnos de un curso se han dividido en dos grupos
A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un
nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el
resto. Escribir un programa que pregunte al usuario su nombre y sexo y muestre por pantalla
el grupo que le corresponde."""

#Definiciones

def division_grupos(nombre,genero):
    n = nombre[0].lower()
    genero = genero.lower()

    if (nombre < "m" and genero == "f") or (nombre > "n" and genero == "m"):
        grupo = "grupo A"
    else:
        grupo = "grupo B"
    
    print(f"Segun tu nombre y tu genero, pertences al {grupo}")

#Logica programa

nombre_dado = input("Por favor ingresa tu nombre: ")
genero_dado = input("Por favor ingresa tu genero (M/F): ")

division_grupos(nombre_dado, genero_dado)
    