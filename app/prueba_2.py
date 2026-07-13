from app.conexion import ConexionMongo
from app.servicios.servicio_pedido import ServicioPedido


def crear_pedido(servicio):
    print("\n========== REGISTRO PEDIDO ==========")
    # VALIDAR CLIENTE
    while True:
        rut = input(
            "Ingrese RUT cliente: "
        ).strip()
        resultado, cliente = (
            servicio.servicio_cliente.buscar_cliente_pedido(
                rut
            )
        )
        if resultado:
            break
        print(cliente)
    print("\nCliente encontrado:")
    print(
        f"{'Nombre':<10}: {cliente['nombre']}"
    )
    print(
        f"{'Correo':<10}: {cliente['correo']}"
    )
    carrito = []
    while True:
        print("\n========== AGREGAR PRODUCTO ==========")
        # BUSCAR PRODUCTO
        while True:
            codigo = input(
                "Ingrese código producto: "
            ).strip()
            resultado, producto = (
                servicio.servicio_producto.buscar_producto_pedido(
                    codigo
                )
            )
            if resultado:
                break
            print(producto)

        print("\nProducto encontrado:")
        print(
            f"{'Nombre':<10}: {producto['nombre']}"
        )
        print(
            f"{'Precio':<10}: ${producto['precio']}"
        )
        print(
            f"{'Stock':<10}: {producto['stock']}"
        )
        print(
            f"{'Estado':<10}: {producto['estado']}"
        )
        if producto["stock"] == 0:
            print(
                "El producto no tiene stock disponible."
            )
            continue
        # VALIDAR CANTIDAD
        while True:
            cantidad = input(
                "Ingrese cantidad: "
            )
            resultado, mensaje = (
                servicio.validar_cantidad_pedido(
                    cantidad
                )
            )
            if not resultado:
                print(mensaje)
                continue
            cantidad = int(cantidad)
            if cantidad <= producto["stock"]:
                break
            print(
                "La cantidad supera el stock disponible."
            )

        # VERIFICAR SI EL PRODUCTO YA EXISTE EN EL CARRITO
        existe = False
        agregado = False
        for item in carrito:
            if item["codigo_producto"] == producto["codigo_producto"]:
                nueva_cantidad = item["cantidad"] + cantidad
                if nueva_cantidad > producto["stock"]:
                    print(
                        "La cantidad acumulada supera el stock disponible."
                    )
                    existe = True
                    break
                item["cantidad"] = nueva_cantidad
                item["subtotal"] = (
                    item["precio"] * nueva_cantidad
                )
                existe = True
                agregado = True
                break

        # SI NO EXISTE, SE AGREGA AL CARRITO
        if not existe:
            carrito.append({
                "codigo_producto": producto["codigo_producto"],
                "nombre": producto["nombre"],
                "precio": producto["precio"],
                "cantidad": cantidad,
                "subtotal": producto["precio"] * cantidad
            })
            agregado = True

        if agregado:
            print(
                "\nProducto agregado al carrito."
            )

        while True:
            continuar = input(
                "\n¿Desea agregar otro producto? (s/n): "
            ).lower().strip()
            if continuar in ["s", "n"]:
                break
            print(
                "Opción inválida. Responda solamente s o n."
            )

        if continuar == "n":
            break

    print("\n========== RESUMEN PEDIDO ==========")

    for producto in carrito:
        print("\n----------------------")
        print(
            f"{'Código':<12}: {producto['codigo_producto']}"
        )

        print(
            f"{'Producto':<12}: {producto['nombre']}"
        )

        print(
            f"{'Precio':<12}: ${producto['precio']}"
        )

        print(
            f"{'Cantidad':<12}: {producto['cantidad']}"
        )

        print(
            f"{'Subtotal':<12}: ${producto['subtotal']}"
        )

    total = servicio.calcular_total(carrito)
    print("\n----------------------")
    print(
        f"{'TOTAL':<12}: ${total}"
    )

    while True:
        confirmar = input(
            "\n¿Confirmar pedido? (s/n): "
        ).lower().strip()
        if confirmar in ["s", "n"]:
            break
        print(
            "Opción inválida. Responda solamente s o n."
        )

    if confirmar == "s":
        resultado, mensaje = (
            servicio.registrar_pedido(
                rut,
                carrito
            )
        )
        print("\n" + mensaje)
    else:
        print(
            "Pedido cancelado."
        )

def listar_pedidos(servicio):
    print("\n========== LISTADO DE PEDIDOS ==========")
    resultado, pedidos = servicio.listar_pedidos()
    if not resultado:
        print(pedidos)
        return
    contador = 1
    for pedido in pedidos:
        print("\n")
        print("=" * 45)
        print(f"{'PEDIDO N°':<15}: {contador}")
        print("=" * 45)
        print(
            f"{'Código':<15}: {pedido['codigo_pedido']}"
        )
        print(
            f"{'Cliente':<15}: {pedido['cliente_rut']}"
        )
        print(
            f"{'Estado':<15}: {pedido['estado']}"
        )
        print(
            f"{'Total':<15}: ${pedido['total']}"
        )
        print(
            f"{'Fecha':<15}: {pedido['fecha_pedido']}"
        )
        print("\n---------- PRODUCTOS ----------")
        for producto in pedido["productos"]:
            print(
                f"{'Código':<15}: {producto['codigo_producto']}"
            )
            print(
                f"{'Nombre':<15}: {producto['nombre']}"
            )
            print(
                f"{'Cantidad':<15}: {producto['cantidad']}"
            )
            print(
                f"{'Precio':<15}: ${producto['precio']}"
            )
            print(
                f"{'Subtotal':<15}: ${producto['subtotal']}"
            )
            print("------------------------------")
        contador += 1
    print("\n" + "=" * 45)
    print("Fin del listado de pedidos.")


def buscar_codigo(servicio):
    print("\n========== BUSCAR PEDIDO POR CÓDIGO ==========")
    codigo = input(
        "Ingrese código pedido: "
    )
    resultado, pedido = (
        servicio.buscar_pedido_codigo(
            codigo
        )
    )
    if not resultado:
        print(pedido)
        return
    print("\n========== PEDIDO ENCONTRADO ==========")
    print(
        f"{'Código':<12}: {pedido['codigo_pedido']}"
    )
    print(
        f"{'Cliente':<12}: {pedido['cliente_rut']}"
    )
    print(
        f"{'Estado':<12}: {pedido['estado']}"
    )
    print(
        f"{'Total':<12}: ${pedido['total']}"
    )
    print("\nProductos:")
    for producto in pedido["productos"]:
        print("----------------------")
        print(f"{'Nombre':<12}: {producto['nombre']}")
        print(f"{'Cantidad':<12}: {producto['cantidad']}")
        print(f"{'Subtotal':<12}: ${producto['subtotal']}")
def buscar_cliente(servicio):
    print("\n========== BUSCAR PEDIDOS POR CLIENTE ==========")
    rut = input(
        "Ingrese RUT cliente: "
    ).strip()
    resultado, pedidos = (
        servicio.buscar_pedidos_cliente(
            rut
        )
    )
    if not resultado:
        print(pedidos)
        return
    print("\n========== PEDIDOS DEL CLIENTE ==========")
    for pedido in pedidos:
        print("\n")
        print("=" * 45)
        print(
            f"{'Código':<15}: {pedido['codigo_pedido']}"
        )
        print(
            f"{'Estado':<15}: {pedido['estado']}"
        )
        print(
            f"{'Total':<15}: ${pedido['total']}"
        )
        print(
            f"{'Fecha':<15}: {pedido['fecha_pedido']}"
        )
        print("\nProductos:")
        for producto in pedido["productos"]:
            print(
                f"  {'Nombre':<12}: {producto['nombre']}"
            )
            print(
                f"  {'Cantidad':<12}: {producto['cantidad']}"
            )
            print(
                f"  {'Subtotal':<12}: ${producto['subtotal']}"
            )
            print("----------------------")

def cambiar_estado(servicio):
    print("\n========== CAMBIAR ESTADO PEDIDO ==========")
    codigo = input(
        "Ingrese código pedido: "
    ).strip()
    resultado, pedido = (
        servicio.buscar_pedido_codigo(
            codigo
        )
    )
    if not resultado:
        print(pedido)
        return
    print("\nPedido encontrado:")
    print(f"{'Código':<12}: {pedido['codigo_pedido']}")
    print(f"{'Cliente':<12}: {pedido['cliente_rut']}")
    print(f"{'Estado actual':<12}: {pedido['estado']}")
    print("\nProductos:")
    for producto in pedido["productos"]:
        print(
            f"{producto['nombre']} "
            f"x{producto['cantidad']}"
        )
    while True:
        estado = input(
            "\nNuevo estado (Completado/Cancelado): "
        ).strip().title()
        resultado, mensaje = (
            servicio.validar_estado_pedido(
                estado
            )
        )
        if resultado:
            if estado == "Pendiente":
                print(
                    "No se puede cambiar nuevamente a Pendiente."
                )
                continue
            break
        print(mensaje)
    resultado, mensaje = (
        servicio.cambiar_estado_pedido(
            codigo,
            estado
        )
    )
    print("\n" + mensaje)


def principal():
    conexion = ConexionMongo()
    db = conexion.obtener_db()
    servicio = ServicioPedido(db)
    listar_pedidos(servicio)



if __name__ == "__main__":
    principal()