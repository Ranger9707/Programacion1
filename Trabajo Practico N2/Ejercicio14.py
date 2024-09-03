#Alumno: Matias Vespa

"""14. Que pida un año y que escriba si es bisiesto o no. Les recordamos que los años bisiestos son
múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Algunos
ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900
no es bisiesto."""

#Definiciones

def anio_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print(f"El año {anio} es año bisiesto.")
    else: 
        print(f"El año {anio} no es bisiesto")
    
#Logica programa

anio_usuario = int(input("Ingrese el año que quiera revisar: "))

anio_bisiesto(anio_usuario)
