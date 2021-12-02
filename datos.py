import json

#Abrir y cerrar json file para guardar en diccionario
portafolio = dict()
f = open("investment.json", "r")
portafolio = json.load(f)
f.close()

#Guardo información en el json
def saveData():
    with open("investment.json", "w") as outfile:
        json.dump(portafolio, outfile, indent=4)

#Creo data inicial del usuario
def create():
    dataInicial = dict()
    dataInicial["Saldo Inicial"] = 1500000
    dataInicial["Total Invertido"] = 0
    dataInicial["Restante"] = 1500000
    dataInicial["Ganancias"] = 0
    dataInicial["Perdida"] = 0
    dataInicial["Forward"] = 0
    dataInicial["Bonos"] = 0
    dataInicial["Acciones"] = dict()
    dataInicial["Venta"] = dict()
    return dataInicial

#Consigo el nombre del usuario y lo guardo si es necesario
def getUser(nombre):
    if nombre not in portafolio.keys():
        portafolio[nombre] = create()
        saveData()
    return portafolio[nombre]

def verPortafolio(nombre, diccionario):
    diccionarioAcciones = diccionario["Acciones"]
    print("----------------------------------------------")
    print("USUARIO:" + nombre)
    print()
    print("{:<20} {:<20} {:<20} {:<20}".format("Acciones", "Cantidad", "Precio Unitario", "Total"))
    print("---------------------------------------------------------------------------------------------------")

    for key in diccionarioAcciones.keys():
        diccionarioNombre = diccionarioAcciones[key]
        print("{:<20} {:<20} {:<20} {:<20}".format(key, str(diccionarioNombre["Cantidad"]), str(round(diccionarioNombre["Precio Unitario"], 2)), str(round(diccionarioNombre["Total"], 2))))
    print("---------------------------------------------------------------------------------------------------")

    print("Dinero invertido en: \n")
    print("Contrato Forward: $" + str(format(round(diccionario["Forward"], 3), ",")))
    print("Bonos: " + str(format(round(diccionario["Bonos"], 3), ",")))

    print("----------------------------------------------")
    print("Llevas invertido $" + str(format(round(diccionario["Total Invertido"], 3), ",")))
    print("Tu ganancia es de $" + str(format(round(diccionario["Ganancias"], 3), ",")))
    print("Tu perdida es de $" + str(format(round(diccionario["Perdida"], 3), ",")))
    print("Te sobran $" + str(format(round(diccionario["Restante"], 3), ",")) + " en tu portafolio")
    print("---------------------------------------------------------------------------------------------------\n")