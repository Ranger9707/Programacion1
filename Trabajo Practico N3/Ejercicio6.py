# 6. Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir de una lista vacía:
#   A. Agregar un elemento al final.
#   B. Agregar un elemento al principio.
#   C. Quitar un elemento al final.
#   D. Quitar un elemento al principio.


#Cree un menu dentro de todo rudimentario que mientras el while sea true continua en un bucle hasta que el usuario decida terminar de jugar con la lista
def menu():
    print(
        """
    Menu:
        A. Agregar un elemento al final
        B. Agregar un elemento al principio
        C. Quitar un elemento al final
        D. Quitar un elemento al principio
        E. Salir
        """
    )

def modificar_lista():
    lista = []
    
    while True:
        menu()
        opcion = input("Elija una opción presionando la tecla correspondiente: ").upper()
        #utilizo el .upper para que no afecte en que modo ingrese la letra pedida (mayuscula o minuscula)
        
        if opcion == 'A':
            elemento = input("Ingrese el elemento para agregar al final de la lista: ")
            lista.append(elemento)
            print(f"Lista actualizada: {lista}")
        
        elif opcion == 'B':
            elemento = input("Ingrese el elemento a agregar al principio de la lista: ")
            lista.insert(0, elemento)
            print(f"Lista actualizada: {lista}")
        
        #Para los puntos C y D agrege un if y un else anidados al elif en caso de querer eliminar elementos cuando ya esta vacia, en vez de tirar error en la terminal
        #El programa vuelve a iniciar indicando al usuario que la lista esta vacia
        
        elif opcion == 'C':
            if lista:
                elemento = lista.pop()
                print(f"Elemento '{elemento}' quitado del final.")
            else:
                print("La lista ya esta vacia. No vas a poder quitar ningún elemento.")
            print(f"Lista actualizada: {lista}")
        
        elif opcion == 'D':
            if lista:
                elemento = lista.pop(0)
                print(f"Elemento '{elemento}' quitado del principio.")
            else:
                print("La lista ya esta vacia. No vas a poder quitar ningún elemento.")
            print(f"Lista actualizada: {lista}")
        
        #Un break al final para terminar el bucle y cerrar el programa, tambien agrege un else que verifica que si nada de lo que el  usuario ingreso corresponde a lo pedido vuelve al principio   
    
        elif opcion == 'E':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, elija una opción del menú.")

modificar_lista()