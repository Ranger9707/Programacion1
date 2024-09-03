# 2. Pedir al usuario que ingrese 5 números para luego almacenarlos en una lista y ordenarlos.
# Imprimir por pantalla el resultado

lista_usuario = []
i = 0
while i < 5:
    numero_usuario = float(input("Ingrese el número {}: ".format(i + 1)))
    numero_existente = numero_usuario in lista_usuario
    if numero_existente == True:
        print("El numero que ingresaste ya existe")
    else:
        lista_usuario.append(float(numero_usuario))
        i = i + 1

lista_usuario.sort()

print(f"Números ordenados: {lista_usuario}")