from numpy.core.fromnumeric import std, var
import yfinance as yf
from scipy.stats import norm
from tabulate import tabulate
import datetime
import pandas as pd

def getPorcentaje(var_99, var_95, pasado_99, pasado_95):
    diferencia99 = (var_99 - pasado_99) / pasado_99
    diferencia95 = (var_95 - pasado_95) / pasado_95
    promedio = (diferencia99 + diferencia95) / 2
    final = promedio * 100
    
    return final

def getVar():
    date = datetime.datetime.now()
    fechaActual = date.strftime("%Y-%m-%d")

    daily = yf.download('MXN=X', '2020-01-01', fechaActual) #
    daily['returns'] = daily.Close.pct_change()
    dolarHoy = daily['Open'].iloc[-1]
    daily = daily.dropna()

    daily.sort_values('returns', inplace=True, ascending=True)

    var_99 = daily['returns'].quantile(0.01)
    var_95 = daily['returns'].quantile(0.05)

    print("*******************************************")
    print("Value at Risk del día de hoy: " + fechaActual)
    print(tabulate([['99%', var_99], ['95%', var_95]], headers=['Porcentaje', 'Value at Risk']))
    print("*******************************************")
    invertido = 1000 * round(dolarHoy, 2)

    print("\nDolar hoy: " + str(dolarHoy))
    print("--------------")
    print("CASO EJEMPLO")
    print("Con $1,000USD invertidos, lo que equivale a $" + str(format(invertido, ",")) + "MXN hay:")
    print(tabulate([['99%', var_99*invertido, '1% de probabilidad de perder más de esto'], ['95%', var_95*invertido, '5% de probabilidad de perder más de esto']]))

    pastData = pd.read_csv("pastVar.csv", index_col=0)
    pasado_99 = round(pastData['Value at risk'][0], 6)
    pasado_95 = round(pastData['Value at risk'][1], 6)
    diferencia = getPorcentaje(round(var_99, 6), round(var_95, 6), pasado_99, pasado_95)
    print("De acuerdo a la última actualización el VaR ha cambiado un " + str(diferencia) + "%")

    if(pastData['Fecha'][0] != fechaActual):
        data = {'Percentage': ['99%', '95%'], 'Value at risk': [var_99, var_95], 'Fecha': [fechaActual, fechaActual]}
        dataFrame = pd.DataFrame(data)
        dataFrame.to_csv("pastVar.csv")