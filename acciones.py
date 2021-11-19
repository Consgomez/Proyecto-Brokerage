import json
import random
import datetime
import carta

def neteoCompra(cantidad, precioUnidad, data):
    #obtener informacion anterior
    totalAnterior = data["Total"]
    totalActual = precioUnidad * cantidad
    #poner la informacion en el diccionario
    data["Cantidad"] = data["Cantidad"] + cantidad
    data["Precio Unitario"] = (totalAnterior+totalActual)/data["Cantidad"]
    data["Total"] = data["Precio Unitario"] * data["Cantidad"]
    # lastTotalPrice = (info[1] * info[0])
    # addingTotalPrice = (precioUnidad * cantidad)
    # info[0] = info[0] + cantidad
    # info[1] = (LastTotalPrice+addingTotalPrice)/info[0]
    return data

def compraAcciones(accion, precio, cant, diccionario, nombre, cantidad):
    #obtener diccionario de acciones
    diccionarioAcciones = diccionario["Acciones"]
    dataAccion = diccionarioAcciones.get(accion, {
        "Cantidad": 0,
        "Precio Unitario": 0,
        "Total": 0 
    })
    diccionarioAcciones[accion] = neteoCompra(cant, precio, dataAccion)
    #guardar la informacion nueva en el diccionario
    diccionario["Acciones"] = diccionarioAcciones
    diccionario["Total Invertido"] = diccionario["Total Invertido"] + (precio * cant)
    diccionario["Restante"] = diccionario["Restante"] - (precio * cant)

    date = datetime.datetime.now()
    fechaActual = date.strftime("%x")
    carta.crearCarta('capitales', fechaActual, nombre, fechaActual, accion + " " + cantidad, fechaActual, precio, cant)

    return diccionario

def neteoVentaTotal(cant, precio, dataVenta, dataAcciones, diccionario):
    dataVenta["Cantidad"] = dataVenta["Cantidad"] + cant
    dataVenta["Precio Venta"] = precio
    dataVenta["Total"] = dataVenta["Cantidad"] * dataVenta["Precio Venta"]

    #se actualizan otros valores
    totalVenta = cant * precio
    totalAccion = dataAcciones["Total"]
    dataAcciones["Cantidad"] = 0
    dataAcciones["Total"] = dataAcciones["Precio Unitario"] * dataAcciones["Cantidad"]
    if totalVenta - totalAccion < 0:
        diccionario["Perdida"] = diccionario["Perdida"] + (totalVenta - totalAccion)
    else:
        diccionario["Ganancias"] = diccionario["Ganancias"] + (totalVenta - totalAccion)

    return dataVenta

def neteoVentaParcial(cant, precio, dataVenta, dataAcciones, diccionario, cantAnterior):
    dataVenta["Cantidad"] = dataVenta["Cantidad"] + cant
    dataVenta["Precio Venta"] = precio
    dataVenta["Total"] = dataVenta["Cantidad"] * dataVenta["Precio Venta"]

    #se actualizan otros valores
    totalVenta = cant * precio
    precioUnidad = dataAcciones["Precio Unitario"]
    dataAcciones["Cantidad"] = cantAnterior - cant
    if totalVenta - (precioUnidad * cant) < 0:
        diccionario["Perdida"] = diccionario["Perdida"] + (totalVenta - (precioUnidad * cant))
    else:
        diccionario["Ganancias"] = diccionario["Ganancias"] + (totalVenta - (precioUnidad * cant))

    return dataVenta

def ventaAcciones(accion, precio, cant, diccionario):
    diccionarioAcciones = diccionario["Acciones"]
    dataAcciones = diccionarioAcciones.get(accion, 0)
    #obtener diccionario de ventas
    if dataAcciones != 0:
        diccionarioVentas = diccionario["Venta"]
        dataVenta = diccionarioVentas.get(accion, {
            "Cantidad": 0,
            "Precio Venta": 0,
            "Total": 0 
        })
        #checar si tenemos las acciones suficientes
        cantAcciones = dataAcciones["Cantidad"]
        if cant <= cantAcciones:
            #checar si hay que hacer venta parcial o total
            if cantAcciones - cant == 0:
                diccionarioVentas[accion] = neteoVentaTotal(cant, precio, dataVenta, dataAcciones, diccionario)
            else:
                diccionarioVentas[accion] = neteoVentaParcial(cant, precio, dataVenta, dataAcciones, diccionario, cantAcciones)
            #guardar en el db
            diccionario["Venta"] = diccionarioVentas
        else:
            print("----------- No tienes esa cantidad para vender -----------")
    else:
        print("----------- No tienes esas acciones -----------")
    return diccionario
