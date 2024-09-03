############################################################################################################
#Trabajo practico integrador de Programacion 1
#Alumno: Matias Vespa
#DNI: 40325120
#Trabajo realizado de forma individual
############################################################################################################

import json
from datetime import datetime

class Reportes:
    def __init__(self):
        try:
            with open('datos/1prestamos.json', 'r', encoding='utf-8') as file:
                self.prestamos = json.load(file)
        except FileNotFoundError:
            self.prestamos = []
            self.guardar_datos("datos/1prestamos.json", self.prestamos)
            
    
    ############################################################################################################
    #prestamos_por_socio toma un ID de socio como parametro y devuelve una lista de los prestamos activos de ese socio, solamente los activos.
    #prestamos_por_libros toma un ID de libro o un nombre de libro como parametro y devuelve una lista de los prestamos activos de ese libro, solamente los activos.
    #prestamos_por_fecha toma dos fechas como parametro y devuelve una lista de los prestamos activos que fueron realizados dentro de esas fechas, solamente los activos.
    ############################################################################################################        
    def prestamos_por_socio(self, id_socio):
        id_socio = str(id_socio)
        return [prestamo for prestamo in self.prestamos if prestamo["ID_Socio"] == id_socio and prestamo["Fecha_Devolucion"] is None] 

    def prestamos_por_libros(self, id_libro=None, nombre_libro=None):
        resultados = []
        
        if id_libro:
            resultados = [prestamo for prestamo in self.prestamos if prestamo["ID_Libro"] == id_libro and prestamo["Fecha_Devolucion"] is None]
        elif nombre_libro:
            resultados = [prestamo for prestamo in self.prestamos if prestamo["Nombre_Libro"] == nombre_libro and prestamo["Fecha_Devolucion"] is None]
    
        return resultados

    def prestamos_por_fecha(self, fecha_inicio, fecha_fin):
        fecha_inicio = datetime.strptime(fecha_inicio, "%d-%m-%Y")
        fecha_fin = datetime.strptime(fecha_fin, "%d-%m-%Y") 
        return [prestamo for prestamo in self.prestamos if fecha_inicio <= datetime.strptime(prestamo["Fecha_Prestamo"], "%d-%m-%Y") <= fecha_fin and prestamo["Fecha_Devolucion"] is None]
    
    
    ############################################################################################################################################
    # devoluciones_por_socio toma un ID de socio como parametro y devuelve una lista de las devoluciones realizadas de ese socio.
    # devoluciones_por_libros toma un ID de libro o un nombre de libro como parametro y devuelve una lista de las devoluciones realizadas de ese libro.
    # devoluciones_por_fecha toma dos fechas como parametro y devuelve una lista de las devoluciones realizadas dentro de esas fechas.
    ############################################################################################################################################
    def devoluciones_por_socio(self, id_socio):
        id_socio = str(id_socio)
        # Filtra préstamos por ID de socio y que han sido devueltos
        return [prestamo for prestamo in self.prestamos if prestamo["ID_Socio"] == id_socio and prestamo["Fecha_Devolucion"] is not None]

    def devoluciones_por_libros(self, id_libro=None, nombre_libro=None):
        resultados = []
        
        if id_libro:
            # Filtra préstamos por ID de libro y que han sido devueltos
            resultados = [prestamo for prestamo in self.prestamos if prestamo["ID_Libro"] == id_libro and prestamo["Fecha_Devolucion"] is not None]
        elif nombre_libro:
            # Filtra préstamos por nombre de libro y que han sido devueltos
            resultados = [prestamo for prestamo in self.prestamos if prestamo["Nombre_Libro"] == nombre_libro and prestamo["Fecha_Devolucion"] is not None]
    
        return resultados

    def devoluciones_por_fecha(self, fecha_inicio, fecha_fin):
        fecha_inicio = datetime.strptime(fecha_inicio, "%d-%m-%Y")
        fecha_fin = datetime.strptime(fecha_fin, "%d-%m-%Y")
        # Filtra préstamos por rango de fecha y que han sido devueltos
        return [prestamo for prestamo in self.prestamos if fecha_inicio <= datetime.strptime(prestamo["Fecha_Prestamo"], "%d-%m-%Y") <= fecha_fin and prestamo["Fecha_Devolucion"] is not None]