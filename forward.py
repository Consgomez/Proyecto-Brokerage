import json
import datetime
import carta

def crearForward():
    forwardDict = dict()
    #preguntar por los datos
    date = datetime.datetime.now()
    
    fechaActual = date.strftime("%x")
    bien = input("¿Qué tipo de divisa va a usar? ")
    monto = float(input("¿Cuál es el monto inicial? "))
    plazo = int(input("¿Cuál es el plazo? "))
    spot = float(input("¿Cuál es el precio SPOT? "))
    forward = float(input("¿Cuál es el precio por adelantado? "))
    print("\n")

    forwardDict["Fecha Inicial"] = fechaActual
    forwardDict["Bien"] = bien
    forwardDict["Monto"] = monto
    forwardDict["Plazo dias"] = plazo
    forwardDict["Spot"] = spot
    forwardDict["Precio Forward"] = forward
    forwardDict["Valor Nominal"] = monto * forward
    forwardDict["Estatus"] = "Pendiente"

    return forwardDict

def do_forward(nombre, diccionario):

    forwardDB = open('forward.json', )
    forwardDict = json.load(forwardDB)
    forwardDB.close()

    print("Desea: ")
    print("1. Crear Forward")
    print("2. Ejercer Forward")
    tipo = int(input())
    print("\n")

    if tipo == 1:
        #crear nuevo
        idForward = len(forwardDict.keys()) + 1
        nombreForward = nombre+str(idForward)
        print("\n")
        print("+++++ Nuevo Forward: " + nombreForward + " +++++\n")
        forwardDict[nombreForward] = crearForward()
        #guardar en el json
        with open("forward.json", "w", errors="ignore") as outfile:
            json.dump(forwardDict, outfile, indent=4)
    elif tipo == 2:
        nombreForward = input("¿Cuál es el id del forward que quiere completar? ")
        bien = forwardDict[nombreForward]["Bien"]
        spotActual = float(input("¿Cuál es el precio SPOT del " + bien + "? "))
        precio = forwardDict[nombreForward]["Precio Forward"]
        monto = forwardDict[nombreForward]["Monto"]
        print("\n")

        diccionario["Forward"] = diccionario["Forward"] + monto
        diccionario["Restante"] = diccionario["Restante"] - monto

        if nombreForward not in forwardDict.keys():
            print("Ese forward no existe, intente de nuevo")
            print("\n")
        else:
            forwardDict[nombreForward]["Estatus"] = "Completado"
            ganancia = int((precio - spotActual) * monto)
            forwardDict[nombreForward]["Ganancia"] = ganancia
            forwardDict["_"+nombreForward] = forwardDict[nombreForward]
            fechaInicio = forwardDict[nombreForward]["Fecha Inicial"]
            forwardDict.pop(nombreForward)

            with open("forward.json", "w", errors="ignore") as outfile:
                json.dump(forwardDict, outfile, indent=4)

            date = datetime.datetime.now()
            fechaActual = date.strftime("%x")

            carta.crearCarta('FX Opción', fechaActual, nombre, fechaInicio, bien + " " +str(monto), fechaActual, precio, monto)

            print("Exercise completo")
            print("\n")

    print("----- Forward " + nombreForward + " editado -----")

    return diccionario