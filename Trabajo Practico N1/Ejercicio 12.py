#Alumno Matias Vespa
#Pedir al usuario que ingrese una fecha en formato dd/mm/aaaa e imprimir en pantalla el
#día, mes y año. Ej: 
#Usuario ingresa: 17/05/1985
#Programa imprime: Día: 17, Mes: 05 y Año: 1985

fecha = (input ("Ingrese una fecha con el siguiente formato dd/mm/aaaa:"))
#Se pide la fecha en el formato requerido

fecha_dia = fecha[:2]
fecha_mes = fecha[3:5]
fecha_año = fecha[6:]
#Usando slices se separa cada fecha para luego mostrarla

print (f"Día:{fecha_dia}, Mes:{fecha_mes} y Año {fecha_año}")