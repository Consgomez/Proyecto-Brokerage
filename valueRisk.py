from numpy.core.fromnumeric import std, var
import yfinance as yf
from scipy.stats import norm
from tabulate import tabulate
import datetime
import pandas as pd

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
    print("Con $1,000USD invertidos, lo que equivale a " + str(invertido) + "MXN hay:")
    print(tabulate([['99%', var_99*invertido, '1% de probabilidad de perder más de esto'], ['95%', var_95*invertido, '5% de probabilidad de perder más de esto']]))

    pastData = pd.read_csv("pastVar.csv", index_col=0)
    #print("De acuerdo a la última actualización el VaR ha cambiado un " + )

    if(pastData['Fecha'][0] != fechaActual):
        data = {'Percentage': ['99%', '95%'], 'Value at risk': [var_99, var_95], 'Fecha': [fechaActual, fechaActual]}
        dataFrame = pd.DataFrame(data)
        dataFrame.to_csv("pastVar.csv")
    

getVar()