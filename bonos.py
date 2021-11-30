import json
import datetime
import pandas as pd
import carta 
import random
import math

def crear_bono():
    bono = dict()
    date = datetime.datetime.now()
    
    valorNom = float(input("¿Cuánto dinero va a invertir en el bono? "))
    plazo = int(input("¿De cuántos años va a ser el plazo de su bono? "))
    cupon = int(input("¿De cuántos meses va a ser el plazo del cupón?"))
    tipo_tasa = int(input("1. Tasa Fija \n2. Tasa Variable \n"))
    
    endDate = date + datetime.timedelta(days=plazo * 365)
    fechaActual = date.strftime("%x")
    fechaFinal = endDate.strftime("%x")

    porAnio = math.floor(12 / cupon)
    totalTasas = plazo * porAnio
    listaTasas = []
    tasa = 6.59

    for x in range(totalTasas):
        if tipo_tasa == 1:
            listaTasas.append(tasa)
        elif tipo_tasa == 2:
            listaTasas.append(round(tasa, 2))
            tasa = random.uniform(6.42, 6.76)

    bono["Valor Nominal"] = valorNom
    bono["Plazo Anios"] = plazo
    bono["Fecha de inicio"] = fechaActual
    bono["Fecha de vencimiento"] = fechaFinal
    bono["Tasas"] = listaTasas
    bono["ISR"] = 0.16
    bono["Ganancia"] = 0

    return bono

def data_bono(nombre, info):
    cantidad = info['Valor Nominal']
    isr = info["ISR"]
    plazo = info["Plazo Anios"] * 2

    df = pd.DataFrame([[nombre, cantidad]], columns=['Dato', 'Valor'])

    total = 0

    for x in range(plazo):
        tasa = info['Tasas'][x]
        if x == 0:
            ganancia = cantidad * (tasa / 100)
            con_isr = ganancia * isr
            total = cantidad + ganancia - con_isr
        else:
            ganancia = total * (tasa / 100)
            con_isr = ganancia * isr
            total = total + ganancia - con_isr
        tasaN = 'Tasa' + str(x+1)
        totalN = 'Total' + str(x+1)
        df_new = pd.DataFrame([[tasaN, tasa], ['Ganancia', ganancia], ['ISR', isr], [totalN, total]], 
            columns=['Dato', 'Valor'])
        df = df.append(df_new)

    print(df)
    print("GANANCIA FINAL: " + str(round(total - cantidad, 2)))

    return round(total - cantidad, 2)

def check_bono(bonos, portafolio, nombre):
    date = datetime.datetime.now()
    fechaActual = date.strftime("%x")

    for key in bonos:
        vencimiento = bonos[key]['Fecha de vencimiento']
        monto = bonos[key]['Valor Nominal']
        inicio = bonos[key]['Fecha de inicio']
        if vencimiento < fechaActual or vencimiento == fechaActual:
            if bonos[key]['Ganancia'] > 0:
                portafolio["Ganancias"] = portafolio["Ganancias"] + bonos[key]['Ganancia']
            elif bonos[key]['Ganancia'] < 0:
                portafolio["Perdida"] = portafolio["Perdida"] + bonos[key]['Ganancia']
            carta.crearCarta('Bono', fechaActual, nombre, inicio, str(monto) + 'MXN', fechaActual, 1, monto)

def do_bono(usuario, diccionario):
    bonoDB = open('bono.json', )
    bonoDict = json.load(bonoDB)
    bonoDB.close()

    idBono = len(bonoDict.keys()) + 1
    nombre = usuario + "_Bono_" + str(idBono)
    print("+++++ Bono: " + nombre + " +++++\n")
    bonoDict[nombre] = crear_bono()

    monto = bonoDict[nombre]["Valor Nominal"]
    diccionario["Total Invertido"] = diccionario["Total Invertido"] + monto
    diccionario["Bonos"] = diccionario["Bonos"] + monto
    diccionario["Restante"] = diccionario["Restante"] - monto
        
    ganancia = data_bono(nombre, bonoDict[nombre])
    bonoDict[nombre]["Ganancia"] = ganancia

    date = datetime.datetime.now()
    fechaActual = date.strftime("%x")
    carta.cartaBono('Bono', fechaActual, usuario, bonoDict[nombre]["Plazo Anios"], 
        bonoDict[nombre]["Fecha de inicio"], bonoDict[nombre]["Fecha de vencimiento"], 
        bonoDict[nombre]['Tasas'][0], monto)

    with open("bono.json", "w", errors="ignore") as outfile:
        json.dump(bonoDict, outfile, indent=4)

    check_bono(bonoDict, diccionario, usuario)

    return diccionario