#Alumno Matias Vespa
#Escriba un programa que indique si un texto es palíndromo, es decir, se escribe igual al
#derecho que al revés. Por ejemplo: rayar, kayak, somos

texto = (input ("Ingrese el texto que desea imprimir al revés:"))
#Pedimos el texto

texto_reves = (texto[::-1])
#Hacemos la reversa

print(f"Tu texto al revés es: {texto_reves}")

if texto_reves == texto_reves[::-1]:
    print("El texto es palíndromo")
else: 
    print ("El texto no es palíndromo")
#Se usa un if - else para verificar si las palabras son palindromos o no y asi notificar al usuario