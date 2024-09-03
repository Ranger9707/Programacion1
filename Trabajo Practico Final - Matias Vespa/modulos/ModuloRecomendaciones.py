############################################################################################################
#Trabajo practico integrador de Programacion 1
#Alumno: Matias Vespa
#DNI: 40325120
#Trabajo realizado de forma individual
############################################################################################################

import json

class Recomendaciones:
    def __init__(self):
        self.libros = self.cargar_datos("datos/1libros.json")
                
    def cargar_datos(self, archivo):
        try:
                with open(archivo, 'r', encoding='utf-8') as file:
                        return json.load(file)
        except FileNotFoundError:
                return []
        
    def guardar_datos(self, archivo, datos):
        with open(archivo, 'w', encoding='utf-8') as file:
                json.dump(datos, file, indent=4)
    
    
    ############################################################################################################
    #recomendar_libros toma un genero como parametro y devuelve una lista de libros que coinciden con ese genero.
    #mostrar_generos devuelve una lista de los generos disponibles en la biblioteca.
    #menu_seleccion_genero presenta al usuario un menu con los generos disponibles y le pide al usuario seleccionar un género.
    ############################################################################################################
    def recomendar_libros(self, genero):
        recomendar = [libro for libro in self.libros if libro["Genero"].lower() == genero.lower()]
        return recomendar
    
    def mostrar_generos(self):
        generos = set(libro["Genero"] for libro in self.libros)
        generos = sorted(list(generos))
        print("Géneros disponibles:")
        for i, genero in enumerate(generos, 1):
            print(f"{i}. {genero}")
        return generos

    def menu_seleccion_genero(self):
        generos = self.mostrar_generos()
        while True:
            try:
                seleccion = int(input("Seleccione un género por número: "))
                if 1 <= seleccion <= len(generos):
                    genero_seleccionado = generos[seleccion - 1]
                    break
                else:
                    print("Por favor, seleccione un número válido.")
            except ValueError:
                print("Por favor, ingrese un número.")
        return genero_seleccionado