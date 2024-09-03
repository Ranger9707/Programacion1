############################################################################################################
#Trabajo practico integrador de Programacion 1
#Alumno: Matias Vespa
#DNI: 40325120
#Trabajo realizado de forma individual
############################################################################################################

from modulos.ModuloLibros import Libros
from modulos.ModuloSocios import Socios
from modulos.ModuloPrestamos import Prestamos
from modulos.ModuloReportes import Reportes
from modulos.ModuloRecomendaciones import Recomendaciones

############################################################################################################
#esta parte del codigo es parte de la función del menú principal. 
#osea muestra las opciones del menú principal
#ademas maneja la entrada del usuario para navegar por las distintas funcionalidades del sistema
############################################################################################################    
def menu_principal():
        while True:
            print("\n------ Menú Principal ------")
            print("1. Gestión de libros")
            print("2. Gestión de socios")
            print("3. Gestión de préstamos y devoluciones")
            print("4. Generar reportes")
            print("5. Recomendaciones de libros")
            print("6. Salir")
        
            opcion = input("Seleccione una opción: ")
        
            if opcion == "1":
                menu_libros()
            elif opcion == "2":
                menu_socios()
            elif opcion == "3":
                menu_prestamos()
            elif opcion == "4":
                menu_reportes()
            elif opcion == "5":
                menu_recomendaciones()
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
                
############################################################################################################
#esta parte se encarga de manejar varias operaciones relacionadas con los libros 
#como agregar, editar, eliminar, buscar y listar libros
#trate de automatizar lo mas que pude, tratando de siempre hacer que el usuario pueda usar solamente opciones por numero
#ademas realize que las busquedas de libros puedan ser por nombre parcial o solamente alguna frase o palabra especifica
#para hacerlo mas accesible
############################################################################################################                         
def menu_libros():
    biblioteca = Libros()
    while True:
            print("\n------ Gestión de libros ------")
            print("1. Registrar libro")
            print("2. Editar libro")
            print("3. Eliminar libro")
            print("4. Buscar libro")
            print("5. Lista de libros")
            print("6. Volver al menú principal")
        
            opcion = input("Seleccione una opción: ")
        
            if opcion == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                editorial = input("Editorial: ")
                ano_publicacion = input("Año de publicación: ")
                genero = input("Género: ")
                cantidad = int(input("Cantidad disponible: "))
                biblioteca.agregar_libro(titulo, autor, editorial, ano_publicacion, genero, cantidad)
                
            elif opcion == "2":
                id_libro = int(input("ID del libro que desea editar: "))
                titulo = input("Nuevo título (opcional): ")
                autor = input("Nuevo autor (opcional): ")
                editorial = input("Nueva editorial (opcional): ")
                ano_publicacion = input("Nuevo año de publicación (opcional): ")
                genero = input("Nuevo género (opcional): ")
                cantidad = input("Nueva cantidad disponible (opcional): ")
                biblioteca.editar_libro(id_libro, titulo, autor, editorial, ano_publicacion, genero, cantidad)
                
            elif opcion == "3":
                entrada_usuario = input("ID del libro que desea eliminar o escriba salir para volver atras: ")
                #id_libro = int(input("ID del libro que desea eliminar o escriba salir para volver atras: "))
                if entrada_usuario.lower()=='salir':
                    return
                else:
                    try:
                        id_libro = int(entrada_usuario)
                        biblioteca.eliminar_libro(id_libro)
                    except ValueError:
                        print("Por favor, ingrese un ID válido.")
                
            elif opcion == "4":
                print("Buscar por:")
                print("1. Libro")
                print("2. Autor")
                print("3. Editorial")
                print("4. Genero")
                criterios = {
                    "1": "Titulo",
                    "2": "Autor",
                    "3": "Editorial",
                    "4": "Genero"
                }
                while True:
                    opcion_criterio = input("Seleccione una opción: ")
                    if opcion_criterio in criterios:
                        break
                    else:
                        print("Opción inválida. Por favor, seleccione una opción válida (1-4).")
                criterio = criterios[opcion_criterio].capitalize()
                valor = input(f"Nombre de {criterio}: ")
                resultados = biblioteca.buscar_libro(**{criterio: valor})
                for libro in resultados:
                    #print(f"ID: {libro['ID']}, Nombre: {libro['Titulo']}, Autor: {libro['Autor']}, Editorial: {libro['Editorial']}, Año publicado: {libro['Ano_Publicacion']}, Genero: {libro['Genero']}, Cantidad disponible: {libro['Cantidad_Disponible']}")
                    print(f"\n"
                            f"ID: {libro['ID']}\n"
                            f"Nombre: {libro['Titulo']}\n"
                            f"Autor: {libro['Autor']}\n"
                            f"Editorial: {libro['Editorial']}\n"
                            f"Año publicado: {libro['Ano_Publicacion']}\n"
                            f"Genero: {libro['Genero']}\n"
                            f"Cantidad disponible: {libro['Cantidad_Disponible']}")
            
            elif opcion == "5":
                libros_ordenados = biblioteca.listar_libros()
                for libro in libros_ordenados:
                    #print(f"ID: {libro['ID']}, Nombre: {libro['Titulo']}, Autor: {libro['Autor']}, Editorial: {libro['Editorial']}, Año publicado: {libro['Ano_Publicacion']}, Genero: {libro['Genero']}, Cantidad disponible: {libro['Cantidad_Disponible']}")
                    print(f"\n"
                            f"ID: {libro['ID']}\n"
                            f"Nombre: {libro['Titulo']}\n"
                            f"Autor: {libro['Autor']}\n"
                            f"Editorial: {libro['Editorial']}\n"
                            f"Año publicado: {libro['Ano_Publicacion']}\n"
                            f"Genero: {libro['Genero']}\n"
                            f"Cantidad disponible: {libro['Cantidad_Disponible']}")
                    
            elif opcion == "6":
                break
            
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
                         
############################################################################################################
#esta funcion se encarga de manejar varias operaciones relacionadas con la gestión de asociadps a la biblioteca 
#registrarlos, editarlos y eliminarlos asi tambien como buscarlos o ver la lista entera   
############################################################################################################ 
def menu_socios():
        socios = Socios()
        while True:
            print("\n------ Gestión de asociados ------")
            print("1. Registrar nuevo asociado")
            print("2. Editar asociados")
            print("3. Eliminar asociados")
            print("4. Buscar asociados")
            print("5. Listar asociados")
            print("6. Volver al menú principal")
        
            opcion = input("Seleccione una opción: ")
        
            if opcion == "1":
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                fecha_nacimiento = input("Fecha de nacimiento (DD-MM-AAAA): ")
                direccion = input("Dirección: ")
                correo = input("Correo electrónico: ")
                telefono = input("Teléfono: ")
                socios.agregar_socio(nombre, apellido, fecha_nacimiento, direccion, correo, telefono)
                
            elif opcion == "2":
                id_socio = int(input("ID del asociado: "))
                nombre = input("Nuevo nombre (opcional): ")
                apellido = input("Nuevo apellido (opcional): ")
                fecha_nacimiento = input("Nueva fecha de nacimiento (opcional): ")
                direccion = input("Nueva dirección (opcional): ")
                correo = input("Nuevo correo electrónico (opcional): ")
                telefono = input("Nuevo teléfono (opcional): ")
                socios.editar_socio(id_socio, nombre, apellido, fecha_nacimiento, direccion, correo, telefono)
                
            elif opcion == "3":
                id_socio = int(input("ID del asociado que desea eliminar de la base de datos: "))
                socios.eliminar_socio(id_socio)
                
            elif opcion == "4":
                while True:
                        print("\nBuscar por:")
                        print("1. Nombre")
                        print("2. Apellido")
                        print("3. ID")
                        criterio = input("Seleccione una opción: ")

                        if criterio == "1":
                            criterio = "Nombre"
                            break
                        elif criterio == "2":
                            criterio = "Apellido"
                            break
                        elif criterio == "3":
                            criterio = "ID"
                            break
                        else:
                            print("Opción no válida. Por favor, intente de nuevo.")

                valor = input(f"Valor de {criterio}: ").capitalize()
                resultados = socios.buscar_socio(**{criterio: valor})
                print("\nResultados de la búsqueda:")
                for socio in resultados:
                    print(f"ID: {socio['ID']}\n"
                          f"Nombre: {socio['Nombre']}\n"
                          f"Apellido: {socio['Apellido']}\n"
                          f"Fecha de nacimiento: {socio['Fecha_Nacimiento']}\n"
                          f"Dirección: {socio['Direccion']}\n"
                          f"Correo Electrónico: {socio['Correo_Electronico']}\n"
                          f"Teléfono: {socio['Telefono']}\n")
                    
            elif opcion == "5":
                socios_ordenados = socios.listar_socios()
                for socio in socios_ordenados:
                    print(f"\n"
                    f"ID: {socio['ID']}\n"
                    f"Nombre: {socio['Nombre']}\n"
                    f"Apellido: {socio['Apellido']}\n"
                    f"Fecha de nacimiento: {socio['Fecha_Nacimiento']}\n"
                    f"Dirección: {socio['Direccion']}\n"
                    f"Correo Electrónico: {socio['Correo_Electronico']}\n"
                    f"Teléfono: {socio['Telefono']}\n")
                    
            elif opcion == "6":
                break
            
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

############################################################################################################
#maneja las operaciones relacionadas con la gestión de presstamos de libros
#permite registrar prestamos, devoluciones, mostrar prestamos por asociado, por libro o listar todos los prestamos
############################################################################################################           
def menu_prestamos():
    prestamos = Prestamos()
    
    while True:
        print("\n------ Menú de Préstamos ------")
        print("1. Registrar préstamo de libro")
        print("2. Registrar devolución de libro")
        print("3. Listado prestamos")
        print("4. Volver a menu principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_socio = input("Ingrese el ID del asociado: ")
            id_libro = input("Ingrese el ID del libro: ")
            fecha_prestamo = input("Ingrese la fecha de préstamo (dd-mm-yyyy): ")
            prestamos.registrar_prestamo(id_socio, id_libro, fecha_prestamo)
            
        elif opcion == "2":
            id_prestamo = int(input("Ingrese el ID del préstamo: "))
            fecha_devolucion = input("Ingrese la fecha de devolución (dd-mm-yyyy): ")
            prestamos.registrar_devolucion(id_prestamo, fecha_devolucion)
            
        elif opcion == "3":
            prestamos_ordenados = prestamos.listar_prestamos()
            for prestamo in prestamos_ordenados:
                print("\n"
                    f"ID Préstamo: {prestamo['ID']}\n"
                    f"ID Socio: {prestamo['ID_Socio']}\n"
                    f"ID Libro: {prestamo['ID_Libro']}\n"
                    f"Nombre Libro: {prestamo['Nombre_Libro']}\n"
                    f"Fecha en la que se realizo el prestamo: {prestamo['Fecha_Prestamo']}\n" 
                    f"Estado: {prestamo['Estado_Prestamo']}\n"
                    f"Fecha devolucion: {prestamo['Fecha_Devolucion']}\n")
        
        elif opcion == "4":
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

############################################################################################################
#se encarga de generar informes
#ofrece opciones para generar informes basados en aosciado, libro o fecha.
############################################################################################################
def menu_reportes():
    reportes = Reportes()
    while True:
        print("\n------ Generar Reportes ------")
        print("1. Préstamos por asociado")
        print("2. Préstamos por libro")
        print("3. Préstamos por fecha")
        print("4. Devoluciones por asociado")
        print("5. Devoluciones por libro")
        print("6. Devoluciones por fecha")
        print("7. Volver al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            id_socio = int(input("ID del asociado: "))
            resultados = reportes.prestamos_por_socio(id_socio)
            if not resultados:
                print("No hay préstamos para el asociado indicado.")
            else:
                print("\nListado de prestamos:")
                for prestamo in resultados:
                    print("\n"
                        f"ID prestamo: {prestamo['ID']}\n" 
                        f"ID Libro: {prestamo['ID_Libro']}\n"
                        f"Nombre Libro: {prestamo['Nombre_Libro']}\n" 
                        f"Fecha Préstamo: {prestamo['Fecha_Prestamo']}\n" 
                        f"Fecha Devolucion: {prestamo['Fecha_Devolucion']}\n" 
                        f"Estado: {prestamo['Estado_Prestamo']}\n")

        elif opcion == "2":
            
            print("Buscar por:")
            print("1. ID del libro")
            print("2. Nombre de libro")
            criterio = input("Seleccione una opción: ")
            
            if criterio == "1":
                id_libro = input("Ingrese el ID del libro: ")
                resultados = reportes.prestamos_por_libros(id_libro=id_libro)
            elif criterio == "2":
                nombre_libro = input("Ingrese el nombre del libro: ")
                resultados = reportes.prestamos_por_libros(nombre_libro=nombre_libro)
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
            if not resultados:
                print("No hay préstamos para el libro indicado.")
            else:
                print("\nListado de prestamos:")
                for prestamo in resultados:
                    print("\n"
                        f"ID Préstamo: {prestamo['ID']}\n" 
                        f"Asociado: {prestamo['ID_Socio']}\n" 
                        f"Fecha Préstamo: {prestamo['Fecha_Prestamo']}\n" 
                        f"Fecha Devolución: {prestamo['Fecha_Devolucion']}\n" 
                        f"Estado: {prestamo['Estado_Prestamo']}\n")
        
        elif opcion == "3":
            fecha_inicio = input("Fecha de Inicio (DD-MM-YYYY): ")
            fecha_fin = input("Fecha de Fin (DD-MM-YYYY): ")
            resultados = reportes.prestamos_por_fecha(fecha_inicio, fecha_fin)
            if not resultados:
                print("No hay préstamos en el rango de fechas indicado.")
            else:
                print("\nListado de prestamos")
                for prestamo in resultados:
                    print("\n"
                        f"ID Préstamo: {prestamo['ID']}\n"
                        f"Asociado: {prestamo['ID_Socio']}" f"ID Libro: {prestamo['ID_Libro']}\n" 
                        f"Nombre Libro: {prestamo['Nombre_Libro']}\n" 
                        f"Fecha Préstamo: {prestamo['Fecha_Prestamo']}\n" 
                        f"Fecha Devolución: {prestamo['Fecha_Devolucion']}\n" 
                        f"Estado: {prestamo['Estado_Prestamo']}\n")
                    
        elif opcion == "4":
            id_socio = (input("ID del asociado: "))
            resultados = reportes.devoluciones_por_socio(id_socio)
            if not resultados:
                print("No hay devoluciones para el asociado indicado.")
            else:
                print("\nListado de devoluciones:")
                for prestamo in resultados:
                        print("\n"
                            f"ID Devolucion: {prestamo['ID']}\n"
                            f"Asociado: {prestamo['ID_Socio']}\n" 
                            f"ID Libro: {prestamo['ID_Libro']}\n"
                            f"Nombre Libro: {prestamo['Nombre_Libro']}\n" 
                            f"Fecha Devolucion: {prestamo['Fecha_Devolucion']}\n" 
                            f"Estado: {prestamo['Estado_Prestamo']}\n")
                        
        elif opcion == "5":
            print("Buscar por:")
            print("1. ID del libro")
            print("2. Nombre de libro")
            criterio = input("Seleccione una opción: ")
            
            if criterio == "1":
                id_libro = input("Ingrese el ID del libro: ")
                resultados = reportes.devoluciones_por_libros(id_libro=id_libro)
            elif criterio == "2":
                nombre_libro = input("Ingrese el nombre del libro: ")
                resultados = reportes.devoluciones_por_libros(nombre_libro=nombre_libro)
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
            if not resultados:
                print("No hay préstamos para el libro indicado.")
            else:
                print("\nListado de prestamos:")
                for prestamo in resultados:
                    print("\n"
                        f"ID Devolucion: {prestamo['ID']}\n" 
                        f"Asociado: {prestamo['ID_Socio']}\n"
                        f"ID Libro: {prestamo['ID_Libro']}\n"
                        f"Nombre Libro:{prestamo['Nombre_Libro']}\n" 
                        f"Fecha Devolución: {prestamo['Fecha_Devolucion']}\n" 
                        f"Estado: {prestamo['Estado_Prestamo']}\n")
                    
        elif opcion == "6":
            fecha_inicio = input("Fecha de Inicio (DD-MM-YYYY): ")
            fecha_fin = input("Fecha de Fin (DD-MM-YYYY): ")
            resultados = reportes.devoluciones_por_fecha(fecha_inicio, fecha_fin)
            if not resultados:
                print("No hay devoluciones en el rango de fechas indicado.")
            else:
                print("\nListado de devoluciones:")
                for prestamo in resultados:
                    print("\n"
                        f"ID Préstamo: {prestamo['ID']}\n"
                        f"Asociado: {prestamo['ID_Socio']}" 
                        f"ID Libro: {prestamo['ID_Libro']}\n" 
                        f"Nombre Libro: {prestamo['Nombre_Libro']}\n" 
                        f"Fecha Préstamo: {prestamo['Fecha_Prestamo']}\n" 
                        f"Fecha Devolución: {prestamo['Fecha_Devolucion']}\n" 
                        f"Estado: {prestamo['Estado_Prestamo']}\n")
        
        elif opcion == "7":
            break
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        
############################################################################################################
#esta funcion se encarga de recomendar libros según el genero seleccionado por el usuario.
############################################################################################################
def menu_recomendaciones():
    recomendaciones = Recomendaciones()
    genero_seleccionado = recomendaciones.menu_seleccion_genero()
    libros_recomendados = recomendaciones.recomendar_libros(genero_seleccionado)
    print(f"\nLibros recomendados del género {genero_seleccionado}:")
    for libro in libros_recomendados:
        print(f"\n"
                f"ID: {libro['ID']}\n"
                f"Nombre: {libro['Titulo']}\n"
                f"Autor: {libro['Autor']}\n"
                f"Editorial: {libro['Editorial']}\n"
                f"Año publicado: {libro['Ano_Publicacion']}\n"
                f"Genero: {libro['Genero']}\n"
                f"Cantidad disponible: {libro['Cantidad_Disponible']}")

############################################################################################################
#funcion principal que llama a la funcion menu_principal
############################################################################################################            
def main():
    menu_principal()

if __name__ == "__main__":
    main()