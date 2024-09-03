#Alumno Matias Vespa
#Programe una aplicación de consola que solicite al usuario su nombre, después su apellido y
#a continuación su año de nacimiento. Con esos datos deberá generar una sugerencia de
#usuario y contraseña. Por ejemplo: nombre: Martín, apellido: Francisconi, Año nacimiento:
#1985 -> Usuario: mfrancisconi, Contraseña: mf.1985.

nombre = (input ("Por favor ingrese su nombre:"))
apellido = (input ("Por favor ingrese su apellido:"))
año = (input("por ultimo ingrese el año de su nacimiento:"))
#Pido los datos

usuario = nombre[:1]+apellido[:]
contraseña = nombre[:1] + apellido[:1] + "." + año + "."
#Creo el usuario y contraseña usando slices

print(f"Segun sus datos la recomendacion que le damos es de:  \nUsuario:{usuario} \nContraseña:{contraseña}")