#Alumno Matias Vespa
#Pida al usuario que ingrese un texto para luego imprimirlo al revés. Ej: HOLA -> ALOH.
texto = (input ("Ingrese el texto que desea imprimir al revés:"))
#Pedimos el texto

texto_reves = (texto[::-1])
#Hacemos la reversa

print(f"Tu text al revés es: {texto_reves}")