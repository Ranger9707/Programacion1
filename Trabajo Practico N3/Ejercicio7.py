# 7. Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings
#    con tareas pendientes y la segunda almacenará strings con tareas terminadas. Permita al usuario:
#       A. Agregar nuevas tareas pendientes.
#       B. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar de la lista de pendientes a la de terminadas.
#       Nota: posterior a cada operación deberá mostrar por pantalla el estado actual de ambas listas.


tareas_pendientes = []
tareas_terminadas = []

def mostrar_tareas(tareas_pendientes, tareas_terminadas):
    #de esta forma imprimo el indice de la tarea (uso +1 para que no empieze desde el 0) asi le es mas facil al usuario elegirlas durante la utilizacion del programa
    #utilizo enumerate para utilizar el indice en vez del elemento
    print("Tareas Pendientes:")
    for i, tarea in enumerate(tareas_pendientes):
        print(f"{i+1}. {tarea}")
    print("\nTareas Terminadas:")
    for i, tarea in enumerate(tareas_terminadas):
        print(f"{i+1}. {tarea}")
    
def agregar_tareas_pendientes():
    nueva_tarea = input("Ingrese la nueva tarea pendiente:")
    tareas_pendientes.append(nueva_tarea)
    print(" ")
    mostrar_tareas(tareas_pendientes, tareas_terminadas)
    print(" ")
    
def agregar_tareas_terminadas():
    if len(tareas_pendientes) == 0:
            
            print(" ")
            print("No hay tareas pendientes para marcar como terminadas.")
            print(" ")  
    else:  
            print(" ")
            mostrar_tareas(tareas_pendientes, tareas_terminadas)
            print(" ")
            seleccionar_tarea = int(input("Ingrese el número de la tarea que desea marcar como terminada:"))
            #aca hago al usuario seleccionar el numero de la tarea que desea terminar
            if seleccionar_tarea > 0 and seleccionar_tarea <= len(tareas_pendientes):
                tarea_terminada = tareas_pendientes.pop(seleccionar_tarea - 1)
                #envio la tarea pendiente a tarea_terminada para luego agregarla a la lista de tareas terminadas
                tareas_terminadas.append(tarea_terminada)  
                print(" ")
                mostrar_tareas(tareas_pendientes, tareas_terminadas)
                print(" ")
            else:
                print("Número de tarea no válido.")
                
def salir_programa():
    print("Saliendo del programa...")

while True:
        opcion = input(
"""A: Agregar tarea pendiente 
B: Marcar tarea como terminada 
C: Salir
    ¿Qué desea hacer?:""").upper()
        match opcion:
            case "A":
                agregar_tareas_pendientes()
            case "B":
                agregar_tareas_terminadas()
            case "C":
                salir_programa()
                break
            case _:
                print("Opción no válida. Por favor, ingrese A, B o C.")