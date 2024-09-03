#Alumno: Matias Vespa

# 9. Que el usuario ingrese dos números y muestre cuál de los dos es menor. Considerar el caso en que ambos números son iguales.

#Definiciones
def comprobador_numeros(numero_uno, numero_dos):
    if numero_uno > numero_dos:
        print(f"{numero_dos} es el numero menos de los dos dados.")
    else:
        if numero_uno == numero_dos:
            print(f"Ambos numeros son iguales.")
        else:
            print(f"{numero_uno} es el numero menos de los dos dados.")

#Logica programa
primer_numero = float(input("Ingrese un número: "))
segundo_numero = float(input("Ingrese un número: "))

comprobador_numeros(primer_numero, segundo_numero)