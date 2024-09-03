# 1. Crear un programa que almacene en una lista las materias de esta u otra carrera y que las muestre por pantalla. 
# (La lista debe ser predefinida, no debe ser ingresada por el usuario).

lista_materias = ["Programacion 1", "Programacion 2", "Diseño Grafico", "Introduccion a la Informatica", "Arquitectura de Computadoras", "Sistemas Operativos", "Introduccion al desarrollo web", "Base de datos", "Programacion 3" ]

i = 0
while i < len(lista_materias):
    print(f"En la posicion {i} se encuentra: {lista_materias[i]}")
    i = i + 1