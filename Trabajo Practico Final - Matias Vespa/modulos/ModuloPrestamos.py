############################################################################################################
#Trabajo practico integrador de Programacion 1
#Alumno: Matias Vespa
#DNI: 40325120
#Trabajo realizado de forma individual
############################################################################################################

import json
from PIL import Image, ImageDraw, ImageFont
class Prestamos:
    def __init__(self):
        self.prestamos = self.cargar_datos("datos/1prestamos.json")
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
#registrar_prestamo recibe el id del socio, el id del libro y la fecha de prestamo, y luego los registra en la lista como prestamo activo.
############################################################################################################
    def registrar_prestamo(self, id_socio, id_libro, fecha_prestamo):
        id_prestamo = len(self.prestamos) + 1
        libro_encontrador = False
        nombre_libro = ""
        
        for libro in self.libros:
            if int(libro["ID"]) == int(id_libro):
                nombre_libro = libro["Titulo"]
                break
        if not nombre_libro:
            print("Libro no encontrado.")
            return
        
        nuevo_prestamo = {
            "ID": id_prestamo,
            "ID_Socio": id_socio,
            "ID_Libro": id_libro,
            "Nombre_Libro":nombre_libro,
            "Fecha_Prestamo": fecha_prestamo,
            "Fecha_Devolucion": None,
            "Estado_Prestamo": "En Curso"
        }
        self.prestamos.append(nuevo_prestamo)
        self.guardar_datos("datos/1prestamos.json", self.prestamos)
        self.generar_recibo(nuevo_prestamo)
        
        libro_encontrado = False
        for libro in self.libros:
            if int(libro["ID"]) == int(id_libro):
                libro_encontrado = True
                if libro["Cantidad_Disponible"] > 0:
                    libro["Cantidad_Disponible"] -= 1
                    print("Préstamo registrado con éxito.")
                    self.guardar_datos("datos/1libros.json", self.libros)
                    return
                else:
                    print("No hay libros disponibles para prestar.")
                    return
        if not libro_encontrado:
            print("Libro no encontrado.")
            
    ############################################################################################################
    #genera una imagen sencilla con los datos del prestamo, que seria dado al asociado.
    ############################################################################################################        
    def generar_recibo(self, prestamo):
        width, height = 300, 150
        img = Image.new("RGB", (width, height), color="white")
        draw = ImageDraw.Draw(img)
        font_path = "modulos/Roboto-Regular.ttf"
        font = ImageFont.truetype(font_path, size=14)
        draw.text((20, 20), f"Recibo de Préstamo", font=font, fill="black")
        draw.text((20, 40), f"ID Prestamo: {prestamo['ID']}", font=font, fill="black")
        draw.text((20, 60), f"ID Socio: {prestamo['ID_Socio']}", font=font, fill="black")
        draw.text((20, 80), f"Libro: {prestamo['Nombre_Libro']}", font=font, fill="black")
        draw.text((20, 100), f"Fecha de Prestamo: {prestamo['Fecha_Prestamo']}", font=font, fill="black")
        img.save(f"recibos/recibo_{prestamo['ID']}.png")
            
############################################################################################################    
#registrar_devolucion funciona de la misma manera, solo que en vez de registrar un prestamo activo, registra un prestamo devuelto.
############################################################################################################
    def registrar_devolucion(self, id_prestamo, fecha_devolucion):
        prestamo_encontrado = False
        for prestamo in self.prestamos:
            if prestamo["ID"] == id_prestamo:
                prestamo_encontrado = True
                prestamo["Fecha_Devolucion"] = fecha_devolucion
                prestamo["Estado_Prestamo"] = "Devuelto"
                self.guardar_datos("datos/1prestamos.json", self.prestamos)

                id_libro_int = int(prestamo["ID_Libro"])   
                for libro in self.libros:
                    if libro["ID"] == id_libro_int:
                        libro["Cantidad_Disponible"] += 1
                        print("Devolución registrada con éxito.")
                        self.guardar_datos("datos/1libros.json", self.libros)  
                        return
        if not prestamo_encontrado:
            print("Préstamo no encontrado.")

############################################################################################################
#listar_prestamos devuelve la lista de todos los prestamos, ordenados por el id.
############################################################################################################
    def listar_prestamos(self, orden='ID'):
        return sorted(self.prestamos, key=lambda prestamo: prestamo[orden])