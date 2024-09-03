#Alumno Matias Vespa
#Programe una aplicación de consola que pregunte el precio total de la cuenta, luego 
#pregunte cuántos comensales hay. A continuación deberá dividir la cuenta total por el 
#número de comensales y mostrar cuánto debe pagar cada persona.

precio_cuenta = int (input ("Por favor ingrese el precio total de la cuenta: "))
numero_comensales = int (input ("Ahora ingrese el número de comensales: "))
#Ingreso de datos

pago_comensal = precio_cuenta / numero_comensales
#Se realiza la division

print ("Segun los datos ingresados cada comensal tendra que pagar:", pago_comensal, "pesos")