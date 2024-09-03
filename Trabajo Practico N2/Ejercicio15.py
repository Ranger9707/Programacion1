#Alumno: Matias Vespa

"""15. Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe
validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter,
informarle que no se puede procesar el dato."""

#Definiciones

def es_vocal(letra):
    vocales = 'aeiou'
    if letra.lower() in vocales:
        print(f"La letra {letra} es vocal.")
    else:
        print(f"La letra {letra} no es vocal.")

#Logica programa
        
intentos = 0
max_intentos = 3
        
while intentos < max_intentos:
    letra_usuario = input("Por favor ingrese solo una letra para verificar si es vocal o no: ")

    if len(letra_usuario) == 1:
        es_vocal(letra_usuario)
        break
    else:
        print("Ingreso mas de una letra, por favor solo ingrese solo una letra.")
        intentos += 1
else:
    print("Supero el limite de intentos fallidos. El programa se detendrá. Por favor reinicie el programa.")