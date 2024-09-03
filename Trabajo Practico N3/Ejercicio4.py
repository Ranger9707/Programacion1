# 4. Dada la siguiente lista: países = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”], realizar lo siguiente:
#  A. Imprimir la cantidad de elementos que tiene la lista.
#  B. Imprimir el primer y último elemento.
#  C. Imprimir el resto.
#  D. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.
#  E. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de la lista. Quitar el elemento correspondiente de esa posición.
#  F. Imprimir la lista en orden inverso.
#  G. Vaciar la lista.


#Decidi no agregar mucho comentario a este punto, todo lo que hay que hacer es bastante estandar en lo que respecta a listas
#lo unico que quizas es un poco fuera de lo comun es la forma de quitar los paises de la lista, pero sigue siendo bastante basico.

lista_paises = ["Argentina", "Brasil", "Bolivia", "Paraguay", "Venezuela"]
lista_paises_minusculas = [pais.lower() for pais in lista_paises]
print(f"Lista de paises: {lista_paises}\n")


#A
cantidad_paises = len(lista_paises)
print(f"Cantidad de elementos en la lista: {cantidad_paises}\n")

#B
primero_paises = lista_paises[0]
ultimo_paises = lista_paises[-1]
print(f"Primer elemento de la lista: {primero_paises}\n")
print(f"Último elemento de la lista: {ultimo_paises}\n")

#C
resto_paises = lista_paises[1:-1]
print(f"Resto de elementos de la lista: {resto_paises}\n")

#D
pais_seleccionado = input("Ingresa un país: ").lower()
if pais_seleccionado in lista_paises_minusculas:
    indice = lista_paises_minusculas.index(pais_seleccionado)
    print(f"El país '{lista_paises[indice]}' se encuentra en la lista en la posición {indice+1}.\n")
else:
    print(f"El país '{pais_seleccionado}' no se encuentra en la lista.\n")

#E   
num = int(input(f"Ingresa un número entre 1 y {cantidad_paises} para eliminar el elemento de la lista en esa posición: "))
if 1 <= num <= cantidad_paises:
    elemento_eliminado = lista_paises.pop(num - 1)
    print(f"Se ha eliminado el elemento: {elemento_eliminado}\n")
else:
    print("Número ingresado no corresponde a ningun valor en la lista.\n")

#F    
paises_invertidos = list(reversed(lista_paises))
print(f"Lista de paises en la lista en orden inverso: {paises_invertidos}\n")

#G
lista_paises.clear()
print(f"Lista vaciada: {lista_paises}")