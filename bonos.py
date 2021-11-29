import json
import datetime
import pandas as pd

def crear_bono():
    bono = dict()
    date = datetime.datetime.now()
    
    valorNom = float(input("¿Cuánto dinero va a invertir en el bono? "))
    plazo = int(input("¿De cuántos años va a ser el plazo de su bono? "))
    
    endDate = date + datetime.timedelta(days=plazo * 365)
    fechaActual = date.strftime("%x")
    fechaFinal = endDate.strftime("%x")

    totalTasas = plazo * 2
    listaTasas = []
    tasa = 6.42

    for x in range(totalTasas):
        listaTasas.append(round(tasa, 2))
        tasa = tasa + 0.15

    bono["Valor Nominal"] = valorNom
    bono["Plazo Anios"] = plazo
    bono["Fecha de inicio"] = fechaActual
    bono["Fecha de vencimiento"] = fechaFinal
    bono["Tasas"] = listaTasas
    bono["ISR"] = 16
    bono["Ganancia"] = 0

    return bono

def data_bono(nombre, info):
    cantidad = info['Valor Nominal']

    tasa_1 = info['Tasas'][0]
    tasa_2 = info['Tasas'][1]
    tasa_3 = info['Tasas'][2]
    tasa_4 = info['Tasas'][3]
    isr = info["ISR"] / 100

    ganancia_1 = cantidad * (tasa_1 / 100)
    isr_1 = ganancia_1 * isr
    total_1 = cantidad + ganancia_1 - isr_1

    ganancia_2 = total_1 * (tasa_2 / 100)
    isr_2 = ganancia_2 * isr
    total_2 = total_1 + ganancia_2 - isr_2

    ganancia_3 = total_2 * (tasa_3 / 100)
    isr_3 = ganancia_3 * isr
    total_3 = total_2 + ganancia_3 - isr_3

    ganancia_4 = total_3 * (tasa_4 / 100)
    isr_4 = ganancia_4 * isr
    total_4 = total_3 + ganancia_4 - isr_4

    data = [[nombre, cantidad], ['Tasa 1', tasa_1], ['Ganancia', ganancia_1], ['ISR', isr_1], ['Ganancia 1', total_1],
        ['Tasa 2', tasa_2], ['Ganancia', ganancia_2], ['ISR', isr_2], ['Ganancia 2', total_2],
        ['Tasa 3', tasa_3], ['Ganancia', ganancia_3], ['ISR', isr_3], ['Ganancia 3', total_3],
        ['Tasa 4', tasa_4], ['Ganancia', ganancia_4], ['ISR', isr_4], ['Ganancia 4', total_4]]
    df = pd.DataFrame(data, columns=['Dato', 'Valor'])

    print(df)
    print("GANANCIA FINAL: " + str(round(total_4 - cantidad, 2)))

    return round(total_4 - cantidad, 2)

def check_bono(bonos, portafolio):
    date = datetime.datetime.now()
    fechaActual = date.strftime("%x")

    for key in bonos:
        vencimiento = bonos[key]['Fecha de vencimiento']
        if vencimiento < fechaActual or vencimiento == fechaActual:
            portafolio["Ganancias"] = portafolio["Ganancias"] + bonos[key]['Ganancia']

def do_bono(usuario, diccionario):
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

        monto = bonoDict[nombre]["Valor Nominal"]
        diccionario["Total Invertido"] = diccionario["Total Invertido"] + monto
        diccionario["Restante"] = diccionario["Restante"] - monto
        
        ganancia = data_bono(nombre, bonoDict[nombre])
        bonoDict[nombre]["Ganancia"] = ganancia

        with open("bono.json", "w", errors="ignore") as outfile:
            json.dump(bonoDict, outfile, indent=4)
        
        check_bono(bonoDict, diccionario)

        return diccionario