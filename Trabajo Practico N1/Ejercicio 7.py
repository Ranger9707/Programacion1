#Alumno Matias Vespa
#Pida al usuario un número x de días y luego mostrar por pantalla cuántas horas, minutos y segundos son esos números de días.

numero_dias = int (input ("Por favor ingrese una cantidad de dias: "))
#Se piden los dias

horas = numero_dias * 24
minutos = numero_dias * 60 * 24
segundos = numero_dias * 24 * 60 * 60
#Se hacen los calculos

print (numero_dias, "dias equivalen a", horas, "horas.")
print (numero_dias, "dias equivalen a", minutos, "minutos.")
print (numero_dias, "dias equivalen a", segundos, "segundos.")