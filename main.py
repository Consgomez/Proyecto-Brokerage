import random
import acciones
import datos
import forward

#pido nombre de persona
nombre = input("Nombre: ")
print("-------------------------------")

#guardo nombre si no existe con valores iniciales
infoUsuario = datos.getUser(nombre)

quit = 0
while quit == 0:
    #enseña el menu de opciones
    print("¿Qué quiere hacer?")
    print("1. Comprar acciones")
    print("2. Vender acciones")
    print("3. Crear o ejercer forward")
    print("4. Ver tu portafolio")
    eleccion = int(input())
    print("\n")

    if eleccion == 1:
        #obtener información de la accion
        precioCompra = random.randint(90, 140)
        accion = input("¿Qué acción quieré comprar? ")
        print("La acción de " + accion + " está a " + str(precioCompra))
        cantidad = input("¿Cuántas acciones quieres comprar? ")
        #agregar a bd
        infoUsuario = acciones.compraAcciones(accion, precioCompra, int(cantidad), infoUsuario, nombre, cantidad)
        datos.portafolio[nombre] = infoUsuario
        datos.saveData()
    elif eleccion == 2:
        #obtener información de la accion
        precioVenta = random.randint(50, 200)
        accion = input("¿Qué acción quieré vender? ")
        print("La venta de " + accion + " está a " + str(precioVenta))
        cantidad = input("¿Cuántas acciones quieres vender? ")
        #agregar a bd
        infoUsuario = acciones.ventaAcciones(accion, precioVenta, int(cantidad), infoUsuario)
        datos.portafolio[nombre] = infoUsuario
        datos.saveData()
    elif eleccion == 3:
        infoUsuario = forward.do_forward(nombre, infoUsuario)
        datos.portafolio[nombre] = infoUsuario
        datos.saveData()
        print("\n")
    elif eleccion == 4:
        datos.verPortafolio(nombre, infoUsuario)
    else: 
        quit = 1