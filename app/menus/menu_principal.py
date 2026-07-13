from app.utilidades import limpiar_pantalla

from app.menus.menu_cliente import menu_cliente
from app.menus.menu_producto import menu_producto
from app.menus.menu_pedido import menu_pedido


def menu_principal(servicio_cliente, servicio_producto, servicio_pedido):

    while True:

        limpiar_pantalla()

        print("\n========== SISTEMA GESTIÓN ==========")
        print("1. Gestión Clientes")
        print("2. Gestión Productos")
        print("3. Gestión Pedidos")
        print("x. Salir")

        opcion = input("\nSeleccione una opción: ")


        if opcion == "1":

            menu_cliente(
                servicio_cliente
            )


        elif opcion == "2":

            menu_producto(
                servicio_producto
            )


        elif opcion == "3":

            menu_pedido(
                servicio_pedido
            )


        elif opcion == "x":

            print("\nCerrando sistema...")
            break


        else:

            print("Opción no válida.")

        input("\nPresione Enter para continuar...")