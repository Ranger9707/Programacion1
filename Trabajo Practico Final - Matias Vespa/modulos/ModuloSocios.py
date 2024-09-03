############################################################################################################
#Trabajo practico integrador de Programacion 1
#Alumno: Matias Vespa
#DNI: 40325120
#Trabajo realizado de forma individual
############################################################################################################

import json

class Socios:
    
    ############################################################################################################
    #__init__ carga datos desde un archivo JSON y los guarda en el atributo libros. 
    #Así cuando creo un objeto libros, ya tengo la lista de libros disponible para agregar, editar, eliminar y buscar libros 
    # sin tener que cargar los datos manualmente.
    ############################################################################################################
    def __init__(self):
        self.socios = self.cargar_datos("datos/1socios.json")
        
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
    #agregar_socio añade asociados a la base de datos.
    #Toma seis parámetros: nombre, apellido, fecha de nacimiento, direccion, correo y telefono.
    #Calcula un ID único para el asociado sumando 1 a la cantidad total de asociados.
    #Crea un diccionario de socios.
    #Llama al método guardar_datos para guardar la lista actualizada en el archivo JSON.
    ############################################################################################################
    def agregar_socio(self, nombre, apellido, fecha_nacimiento, direccion, correo, telefono):
        id_socio = len(self.socios) + 1
        nuevo_socio = {
            "ID": id_socio,
            "Nombre": nombre,
            "Apellido": apellido,
            "Fecha_Nacimiento": fecha_nacimiento,
            "Direccion": direccion,
            "Correo_Electronico": correo,
            "Telefono": telefono
        }
        self.socios.append(nuevo_socio)
        self.guardar_datos("datos/1socios.json", self.socios)
        print("Socio agregado con éxito.")
        
    ############################################################################################################      
    #editar_socio permite editar los asociados de base de datos
    #Toma los mismos parametros anteriores: nombre, apellido, fecha de nacimiento, direccion, correo y telefono.
    #Y los modifica a gusto del usuario
    #luego lama al método guardar_datos para guardar la lista actualizada en el archivo JSON.
    ############################################################################################################
    def editar_socio(self, id_socio, nombre=None, apellido=None, fecha_nacimiento=None, direccion=None, correo=None, telefono=None):
        for socio in self.socios:
            if socio["ID"] == id_socio:
                if nombre: socio["Nombre"] = nombre
                if apellido: socio["Apellido"] = apellido
                if fecha_nacimiento: socio["Fecha_Nacimiento"] = fecha_nacimiento
                if direccion: socio["Direccion"] = direccion
                if correo: socio["Correo_Electronico"] = correo
                if telefono: socio["Telefono"] = telefono
                self.guardar_datos("datos/1socios.json", self.socios)
                print("Socio editado con éxito.")
                return
        print("Socio no encontrado.")

    ############################################################################################################
    #eliminar_socio elimina un asociado específico de la lista.
    #primero toma el parámetro id_socio, que es el identificador a eliminar.
    #Usa una lista por comprensión para iterar sobre el diccionario.
    #Verifica si si los ID coinciden, si coincide, el asociado no se incluye en la nueva lista.
    #Actualiza la lista para excluir el asociado con el ID coincidente.
    ############################################################################################################
    def eliminar_socio(self, id_socio):
        self.socios = [socio for socio in self.socios if socio["ID"] != id_socio]
        self.guardar_datos("datos/1socios.json", self.socios)
        print("Socio eliminado con éxito.")
    
    
    ########################################################################################################
    #Busca al socio usando los criterios dados por el usuario
    #Devuelve una lista de asociados que coinciden con los criterios.
    ############################################################################################################
    def buscar_socio(self, **criterios):
        resultados = self.socios
        if 'ID' in criterios:
            criterios['ID'] = int(criterios['ID'])
        for key, value in criterios.items():
            resultados = [socio for socio in resultados if socio.get(key) == value]
        return resultados
    
    
    ############################################################################################################
    #Simplemente recorre la lista de asociados y los muestra en pantalla a todos
    ############################################################################################################
    def listar_socios(self, orden='ID'):
        return sorted(self.socios, key=lambda socio: socio[orden])