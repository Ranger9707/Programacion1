#Alumno: Matias Vespa

#1. Que al pasarle una cadena <nombre> nos muestre por pantalla el saludo ¡Hola <nombre>!.

#Definiciones
def saludo_con_nombre(nombre):
    print(f"¡Hola {nombre}!")

#Logica programa
nombre_usuario = input("Por favor ingrese su nombre:")

saludo_con_nombre(nombre_usuario)