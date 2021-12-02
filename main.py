import yfinance as yf
import acciones
import datos
import forward
import bonos
import valueRisk

#conseguir tipo de cambio
cambio = yf.Ticker('MXN=X')
dolar = cambio.info['open']

#pido nombre de persona
nombre = input("Nombre: ")
print("-------------------------------")

#guardo nombre si no existe con valores iniciales
infoUsuario = datos.getUser(nombre)

quit = 0
while quit == 0:
    #enseña el menu de opciones
    print("¿Qué quiere hacer?")
    print("1. Comprar acciones")
    print("2. Vender acciones")
    print("3. Crear o ejercer forward")
    print("4. Capturar un bono")
    print("5. Calcular VaR del tipo de cambio")
    print("6. Ver tu portafolio")
    eleccion = int(input())
    print("\n")

    if eleccion == 1:
        #obtener información de la accion
        accion = input("¿Qué acción quieré comprar? ")
        ticker = yf.Ticker(accion)
        precioCompra = ticker.info['currentPrice']
        nombreAccion = ticker.info['shortName']
        currency = ticker.info['financialCurrency']
        print("La acción de " + nombreAccion + " está a " + str(precioCompra) + currency)
        cantidad = input("¿Cuántas acciones quieres comprar? ")
        #agregar a bd
        if currency == "MXN":
            precioFinal = precioCompra
        elif currency == "HK":
            precioFinal = round(precioCompra * 2.75, 2)
        else:
            precioFinal = round(precioCompra * dolar, 2)
        infoUsuario = acciones.compraAcciones(accion.upper(), precioFinal, int(cantidad), infoUsuario, nombre, cantidad)
        datos.portafolio[nombre] = infoUsuario
        datos.saveData()
    elif eleccion == 2:
        #obtener información de la accion
        accion = input("¿Qué acción quieré vender? ")
        ticker = yf.Ticker(accion)
        nombreAccion = ticker.info['shortName']
        precioVenta = ticker.info['ask']
        print("La venta de " + nombreAccion + " está a " + str(precioVenta))
        cantidad = input("¿Cuántas acciones quieres vender? ")
        #agregar a bd
        precioFinal = round(precioVenta * dolar, 2)
        infoUsuario = acciones.ventaAcciones(accion.upper(), precioFinal, int(cantidad), infoUsuario)
        datos.portafolio[nombre] = infoUsuario
        datos.saveData()
    elif eleccion == 3:
        infoUsuario = forward.do_forward(nombre, infoUsuario)
        datos.portafolio[nombre] = infoUsuario
        datos.saveData()
        print("\n")
    elif eleccion == 4:
        infoUsuario = bonos.do_bono(nombre, infoUsuario)
        datos.portafolio[nombre] = infoUsuario
        datos.saveData()
    elif eleccion == 5:
        valueRisk.getVar()
    elif eleccion == 6:
        datos.verPortafolio(nombre, infoUsuario)
    else: 
        quit = 1