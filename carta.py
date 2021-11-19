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
