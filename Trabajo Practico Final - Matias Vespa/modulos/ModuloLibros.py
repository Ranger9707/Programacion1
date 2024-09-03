############################################################################################################
#Trabajo practico integrador de Programacion 1
#Alumno: Matias Vespa
#DNI: 40325120
#Trabajo realizado de forma individual
############################################################################################################

import json

class Libros:
        
        ############################################################################################################
        #__init__ carga datos desde un archivo JSON y los guarda en el atributo libros. 
        #Así cuando creo un objeto libros, ya tengo la lista de libros disponible para agregar, editar, eliminar y buscar libros 
        # sin tener que cargar los datos manualmente.
        ############################################################################################################
        def __init__(self):
                self.libros = self.cargar_datos("datos/1libros.json")
         
        ############################################################################################################
        #Metodos sencillos para cargar y guardar jsons. 
        ############################################################################################################  
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
        #agregar_libro añade un nuevo libro a la colección de la biblioteca.
        #Toma seis parámetros: título, autor, editorial, año de publicación, género y cantidad.
        #Calcula un ID único para el libro sumando 1 a la cantidad actual de libros.
        #Crea un diccionario con los detalles del libro.
        #Llama al método guardar_datos para guardar la lista actualizada en el archivo JSON.
        ############################################################################################################
        def agregar_libro(self, titulo, autor, editorial, ano_publicacion, genero, cantidad):
                id_libro = len(self.libros) + 1
                nuevo_libro = {
                "ID": id_libro,
                "Titulo": titulo,
                "Autor": autor,
                "Editorial": editorial,
                "Ano_Publicacion": ano_publicacion,
                "Genero": genero,
                "Cantidad_Disponible": cantidad
                }
                self.libros.append(nuevo_libro)
                self.guardar_datos("datos/1libros.json", self.libros)
                print("Libro agregado con éxito.")

        ############################################################################################################      
        #editar_libro permite editar los libros de la colección de la biblioteca.
        #Toma los mismos parametros anteriores: título, autor, editorial, año de publicación, género y cantidad.
        #Y los modifica a gusto del usuario
        #luego lama al método guardar_datos para guardar la lista actualizada en el archivo JSON.
        ############################################################################################################
        def editar_libro(self, id_libro, titulo=None, autor=None, editorial=None, ano_publicacion=None, genero=None, cantidad=None):
                for libro in self.libros:
                        if libro["ID"] == id_libro:
                                if titulo: libro["Titulo"] = titulo
                                if autor: libro["Autor"] = autor
                                if editorial: libro["Editorial"] = editorial
                                if ano_publicacion: libro["Ano_Publicacion"] = ano_publicacion
                                if genero: libro["Genero"] = genero
                                if cantidad: libro["Cantidad_Disponible"] = cantidad
                                self.guardar_datos("datos/1libros.json", self.libros)
                                print("Libro editado con éxito.")
                                return
                print("Libro no encontrado.")
        
        ############################################################################################################
        #eliminar_libro elimina un libro específico de la colección de la biblioteca.
        #primero toma el parámetro id_libro, que es el identificador del libro a eliminar.
        #Usa una lista por comprensión para iterar sobre los libros en el diccionario de libros.
        #Verifica si el ID del libro coincide con id_libro si coincide, el libro no se incluye en la nueva lista.
        #Actualiza la lista libros para excluir el libro con el ID coincidente.
        #Llama al método guardar_datos para guardar la lista actualizada en el archivo JSON.
        ############################################################################################################
        def eliminar_libro(self, id_libro):
                self.libros = [libro for libro in self.libros if libro["ID"] != id_libro]
                self.guardar_datos("datos/1libros.json", self.libros)
                print("Libro eliminado con éxito.") 
                
        ############################################################################################################        
        #buscar_libro buscar libros específicos según criterios dados.
        #primero usa argumentos de palabra clave (**criterios), permitiendo cualquier criterios de búsqueda (título, autor, género,etc)
        #Inicia una lista vacia para almacenar los libros que coincidan
        #Itera sobre cada libro en la lista.
        #Para cada libro, itera sobre los criterios de búsqueda proporcionados.
        #Verifica si el criterio actual existe en los detalles del libro
        #Si se encuentra una coincidencia, añade el libro a la lista resultados
        #después de iterar sobre todos los libros, devuelve la lista resultados con los libros que coincidan.
        ############################################################################################################
        def buscar_libro(self, **criterios):
                resultados = []
                for libro in self.libros:
                        for key, value in criterios.items():
                                if key in libro and value.lower() in libro[key].lower():
                                        resultados.append(libro)
                                        break
                return resultados

        ############################################################################################################
        #Simplemente recorre el diccionario de libros y crea una lista con todos los libros para luego imprimirlos.
        ############################################################################################################
        def listar_libros(self, orden='ID'):
                return sorted(self.libros, key=lambda libro: libro[orden])