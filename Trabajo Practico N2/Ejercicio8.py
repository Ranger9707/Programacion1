#Alumno: Matias Vespa

#8. Pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

#Definiciones
def comprobador_de_mayoria_de_edad(edad):
    if edad >= 18:
        print("Usuario es mayor de edad.")
    else:
        print("Usuario aun no es mayor de edad.")

#Logica programa
edad_dada = int(input("Ingrese su edad: "))

comprobador_de_mayoria_de_edad(edad_dada)