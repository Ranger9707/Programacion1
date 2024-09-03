#Alumno: Matias Vespa

#6. Que pida al usuario una palabra y la muestre por pantalla 10 veces.

#Definiciones
def repeticion_nombre(palabra):
    for i in range(10):
        print(palabra)

#Logica programa
pedido_palabra = (input("Por favor ingrese una palabra: "))
palabra_dada = repeticion_nombre(pedido_palabra)
