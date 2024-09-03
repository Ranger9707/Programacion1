#Alumno: Matias Vespa

#3. Que nos calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

#Definiciones
def calculo_iva(factura, iva):
    if iva:
        iva_total = float(iva)
    else:
        iva_total = float(21)
    cuenta_iva = factura * iva_total / 100
    total = factura + cuenta_iva
    return total

#Logica programa
factura_sin_iva = float(input("Ingrese el monto de la factura sin IVA: "))

iva_factura = input("Ingrese el IVA aplicado (si no ingresa nada asumira que el iva es del 21%): ")

factura_total = calculo_iva(factura_sin_iva, iva_factura)

print(f"El total de la factura con IVA es: {factura_total}")