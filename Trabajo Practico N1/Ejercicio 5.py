#Alumno Matias Vespa
#Escriba un programa que pida al usuario que ingrese 3 números. Sume los dos primeros y 
#luego multiplique este total por el tercero. Mostrar la respuesta en pantalla de la siguiente forma: “La respuesta es XX”.

numero_1 = int (input ("Escribe el primer número para la suma: "))
numero_2 = int (input ("Escribe el segundo número para la suma: "))
numero_3 = int (input ("Escribe un tercer numero para multiplicar los numeros sumados: "))
#Pide los datos

suma = numero_1 + numero_2
multiplicacion = suma * numero_3
#Se realiza el calculo

print ("La respuesta es:", multiplicacion)