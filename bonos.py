import json
import datetime

def crear_bono():
    bono = dict()
    date = datetime.datetime.now()
    
    valorNom = float(input("¿Cuánto dinero va a invertir en el bono?"))
    plazo = int(input("El plazo del bono va a ser de:\n 1. 3 años\n 2. 5 años\n 3. 10 años\n 4. 20 años\n 5. 30 años\n"))
    # if plazo == 1:
    #     tasa = 6
    # elif plazo == 2:
    #     tasa = 10
    # elif plazo == 3:
    #     tasa = 20
    # elif plazo == 4:
    #     tasa = 60

    endDate = date + datetime.timedelta(days=plazo)
    fechaActual = date.strftime("%x")
    fechaFinal = endDate.strftime("%x")

    bono["Valor Nominal"] = valorNom
    bono["Plazo"] = plazo
    bono["Fecha de inicio"] = fechaActual
    bono["Fecha de vencimiento"] = fechaFinal
    bono["Tasas"] = [6.42, 6.58, 6.79, 6.98]

    return bono

def do_bono(usuario):
    bonoDB = open('bono.json', )
    bonoDict = json.load(bonoDB)
    bonoDB.close()

    print("Desea: ")
    print("1. Capturar un bono")
    print("2. Hacer fixing de su bono")
    opcion = int(input())
    print("\n")

    if opcion == 1:
        idBono = len(bonoDict.keys()) + 1
        nombre = usuario + "_Bono_" + str(idBono)
        print("+++++ Bono: " + nombre + " +++++\n")
        print("\n")
        bonoDict[nombre] = crear_bono()

        with open("bono.json", "w", errors="ignore") as outfile:
            json.dump(bonoDict, outfile, indent=4)