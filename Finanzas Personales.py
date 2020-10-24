from Egresos import Egresos
from Ingresos import Ingreso

saldoInicial = 0.00
while True:
    options = input(
        "ingrese una opcion 0- Salir 1- Ingrese dinero 2- Retire dinero 3-Reporte Ingresos 4-Reporte  Egresos 5-Movimiento Cuenta 6-Total"
    )

    if options == "0":
        break
    elif options == "1":
        ingreso = float(input(" Cuánto dinero deseas ingresar a tu cuenta"))
        saldoInicial = saldoInicial + ingreso
        print(f"Su total es de: {saldoInicial} ")
    elif options == "2":
        egreso = float(input(" Cuánto dinero deseas reitirar de tu cuenta"))
        saldoInicial = saldoInicial - egreso
        if egreso > saldoInicial:
            print("No tienes suficiente dinero")
        else:
            saldoInicial < egreso
            print(f"El dinero en su cuenta es: {saldoInicial} ")

    elif options == "3":
        print(f"El dinero en su cuenta es: {saldoInicial} ")
    elif options == "4":
        print(f"El dinero en su cuenta es: {saldoInicial} ")
    elif options == "5":
        transacciones = float(input(" Quieres conocer los movimientos en tus cuentas"))
        print(f"El dinero en su cuenta es: {saldoIngreso} ")
        print(f"El dinero en su cuenta es: {saldoEgreso} ")
    elif options == "6":
        saldoTotal = float(input(" El monto total en su cuenta es"))
        saldoTotal = saldoIngreso - saldoEgreso
        print(f"El dinero en su cuenta es: {saldoTotal} ")