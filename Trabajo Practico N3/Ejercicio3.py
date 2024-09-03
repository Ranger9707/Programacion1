# 3. Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], permitir al usuario ingresar 3 frutas más para agregarlas al final de lista. 
# Luego, mostrar por pantalla la lista completa y debajo la misma lista pero sólo con las frutas que añadió el usuario.

lista_frutas_programa = ["banana", "manzana", "pera"]

fruta_nueva_1 = input("Ingresa la primera fruta: ")
fruta_nueva_2 = input("Ingresa la segunda fruta: ")
fruta_nueva_3 = input("Ingresa la tercera fruta: ")

#Se que podria haber hecho un input que pidiera las 3 frutas de una y luego separarlas con una coma para podes hacer la lista de forma mas sencilla, pero me parecio mucho mas limpio y mas estetico ir pidiendo de a uno
#aunque es cierto que deja poco espacio para poder expandir este programa si se requieren agregar mas frutas

lista_frutas_usuario = [fruta_nueva_1, fruta_nueva_2, fruta_nueva_3]

lista_frutas_programa.extend(lista_frutas_usuario)

print(f"Lista completa de frutas: {lista_frutas_programa}")

print(f"Lista de frutas añadidas por el usuario: {lista_frutas_usuario}")