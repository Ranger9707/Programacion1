#Alumno: Matias Vespa

"""16. Que imprima el siguiente patrón:
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1"""

#Definiciones

def patron_numeros():
    for i in range(5, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

input("Oprima enter para imprimir el patron de numeros:")
patron_numeros()