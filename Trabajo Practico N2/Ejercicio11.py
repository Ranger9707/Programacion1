#Alumno: Matias Vespa

"""11. Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se
encuentran en dicha frase."""

#Definiciones
def contador_vocales(frase_dada):
    frase_dada = frase_dada.lower()

    contador = 0

    for caracter in frase_dada:
        if caracter in "aeiouáéíóú":
            contador += 1
    print (f"La cantidad de vocales que se encuentran en tu frase son:{contador}")

#Logica programa
frase_del_usuario = input("Por favor ingresa la frase que quieras: ")
contador_vocales(frase_del_usuario)