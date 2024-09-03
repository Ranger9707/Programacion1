#Alumno: Matias Vespa

"""12. Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro
mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día
ingresado no es ninguno de esos, imprimir otro mensaje."""

#Definiciones

def dia_de_la_semana(dia):

    dia = dia.lower()

    if dia == "lunes":
        print ("Hoy es lunes! Feliz inicio de la semana")
    elif dia == "viernes":
        print ("Por fin llegamos al viernes, Feliz fin de semana!")
    elif dia == "sabado" or dia == "sábado" or dia == "domingo":
        print("Qué haces acá? Anda a disfrutar el finde.")
    elif dia == "martes" or dia == "miercoles" or dia == "jueves":
        print("Estamos atravesando por la semana, ya falta poco para el finde.")
    else:
        print("Lo que ingresaste no es ningún día de la semana.")

#Logica programa
dia_usuario = input("Ingresa el día de la semana que quieras: ")
dia_de_la_semana(dia_usuario)