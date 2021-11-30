import glob
import os

def crearCarta(operacion, fecha, nombre, fechaTrade, monto, fechaVal, unidad, cantidad):
    myFiles = glob.glob('*.txt')
    archivos = len(myFiles) + 1
    titulo = "CartaConfirmacion" + str(archivos) + ".txt"
    with open(titulo, 'w+') as c:
        c.write("CONFIRMACIÓN DE OPERACIÓN: " + operacion +
        "\n"
        "FECHA: " + fecha +
        "\n \n"
        "DIRIGIDO A:"
        "\n" + 
        nombre +
        "\n \n"
        "ESTIMADOS SRES.,"
        "\n \n"
        "Hemos procedido a realizar la siguiete operación de " + operacion + ", de acuerdo a la carta de instrucción nro. " + str(archivos) + " enviada por Uds:"
        "\n \n"
        "1. Detalles de la operación al inicio: "
        "\n \n"
        "Términos generales"
        "\n \n"
        "Nuestra referencia: "  + "Operación" + str(archivos) +
        "\n"
        "Referencia original: " + "Operación" + str(archivos) +
        "\n"
        "Fecha trade (concretación): " + fechaTrade +
        "\n \n"
        "De acuerdo con nuestro acuerdo de la fecha de negociación como se indica anteriormente, confirmamos la siguiente transacción " + operacion +
        "\n \n" +
        nombre + " compra"
        "\n \n"
        "Monto: " + monto +
        "\n"
        "Fecha valor: " + fechaVal +
        "\n"
        "Valor unitario: " + str(unidad) +
        "\n \n"
        "Banco vende"
        "\n \n"
        "Monto: " + str(unidad * cantidad) +
        "\n"
        "Fecha Valor: " + fechaVal)

def cartaBono(operacion, fecha, nombre, plazo, inicio, vencimiento, tasa, monto):
    myFiles = glob.glob('*.txt')
    archivos = len(myFiles) + 1
    titulo = "CartaConfirmacion" + str(archivos) + ".txt"
    with open(titulo, 'w+') as c:
        c.write("CONFIRMACIÓN DE OPERACIÓN: " + operacion + 
        "\nFECHA: " + fecha + 
        "\n \nDIRIGIDO A: \n" + nombre +
        "\n \nESTIMADOS SRES., \n \n"
        "Hemos procedido a realizar la siguiente operación de " + operacion + ", de acuerdo a la carta de instrucción nro. " + str(archivos) + " enviada por Uds: "
        "\n \n1. Detalles de la operación al inicio: "
        "\n \nTérminos generales"
        "\n \nNuestra referencia: Operación" + str(archivos) +
        "\nReferencia original: Operación " + str(archivos) +
        "\nFecha captura: " + fecha +
        "\n \n"
        "De acuerdo con nuestro acuerdo de la fecha de negociación como se indica anteriormente, confirmamos la siguiente transacción " + operacion + 
        "\nA nombre de " + nombre + 
        "\nCon un plazo de " + str(plazo) +
        "\nMonto inicial: " + str(monto) +
        "\nFecha de inicio: " + inicio +
        "\nFecha de vencimiento: " + vencimiento + 
        "\nY una tasa inicial del " + str(tasa) + "%") 