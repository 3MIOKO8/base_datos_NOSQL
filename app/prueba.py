from app.conexion import ConexionMongo
from app.servicios.servicio_producto import ServicioProducto



def registrar_producto(servicio):

    print("\n========== REGISTRO PRODUCTO ==========")

    # Nombre
    while True:
        nombre = input("Nombre producto: ")
        resultado, mensaje = servicio.validar_nombre_producto(nombre)
        print(mensaje)
        if resultado:
            break

    # Descripción
    while True:
        descripcion = input("Descripción: ")
        resultado, mensaje = servicio.validar_descripcion_producto(descripcion)
        print(mensaje)
        if resultado:
            break

    # Categoría
    while True:
        categoria = input("Categoría: ")
        resultado, mensaje = servicio.validar_categoria_producto(categoria)
        print(mensaje)
        if resultado:
            break

    # Precio
    while True:
        precio = input("Precio: ")
        resultado, mensaje = servicio.validar_precio_producto(precio)
        print(mensaje)
        if resultado:
            break

    # Stock
    while True:
        stock = input("Stock: ")
        resultado, mensaje = servicio.validar_stock_producto(stock)
        print(mensaje)
        if resultado:
            break

    # Proveedor
    while True:
        proveedor = input("Proveedor: ")
        resultado, mensaje = servicio.validar_proveedor_producto(proveedor)
        print(mensaje)
        if resultado:
            break

    # Estado
    while True:
        estado = input("Estado (Activo/Inactivo): ").strip().title()
        resultado, mensaje = servicio.validar_estado_producto(estado)
        print(mensaje)
        if resultado:
            break

    resultado, mensaje = servicio.registrar_producto(
        nombre,
        descripcion,
        categoria,
        precio,
        stock,
        proveedor,
        estado

    )
    print("\n" + mensaje)

def listar_productos(servicio):
    print("\n========== LISTADO PRODUCTOS ==========")
    resultado, productos = servicio.listar_productos()
    if not resultado:
        print(productos)
        return
    if len(productos) == 0:
        print("No existen productos registrados.")
        return
    for producto in productos:
        print("\n========== PRODUCTO ==========")
        print(f"{'Código':15}: {producto['codigo_producto']}")
        print(f"{'Nombre':15}: {producto['nombre']}")
        print(f"{'Descripción':15}: {producto['descripcion']}")
        print(f"{'Categoría':15}: {producto['categoria']}")
        print(f"{'Precio':15}: ${producto['precio']}")
        print(f"{'Stock':15}: {producto['stock']}")
        print(f"{'Proveedor':15}: {producto['proveedor']}")
        print(f"{'Estado':15}: {producto['estado_mostrar']}")
        print("==============================")

def buscar_producto(servicio):
    print("\n========== BUSCAR PRODUCTO ==========")
    codigo = input("Ingrese código del producto: ")
    resultado, producto = servicio.buscar_producto_codigo(codigo)
    if not resultado:
        print(producto)
        return
    print("\n========== PRODUCTO ==========")
    print(f"{'Código':15}: {producto['codigo_producto']}")
    print(f"{'Nombre':15}: {producto['nombre']}")
    print(f"{'Descripción':15}: {producto['descripcion']}")
    print(f"{'Categoría':15}: {producto['categoria']}")
    print(f"{'Precio':15}: ${producto['precio']}")
    print(f"{'Stock':15}: {producto['stock']}")
    print(f"{'Proveedor':15}: {producto['proveedor']}")
    print(f"{'Estado':15}: {producto['estado_mostrar']}")
    print("==============================")

def actualizar_producto(servicio):
    print("\n========== ACTUALIZAR PRODUCTO ==========")
    codigo = input("Ingrese código del producto: ")
    resultado, producto = servicio.buscar_producto_codigo(codigo)
    if not resultado:
        print(producto)
        return
    print("\n========== PRODUCTO ENCONTRADO ==========")

    print(f"{'Código':15}: {producto['codigo_producto']}")

    print(f"{'Nombre':15}: {producto['nombre']}")

    print(f"{'Precio':15}: ${producto['precio']}")

    print(f"{'Stock':15}: {producto['stock']}")

    print(f"{'Estado':15}: {producto['estado_mostrar']}")

    print("==========================================")
    while True:
        print("\n¿Qué desea modificar?")

        print("1. Nombre")
        print("2. Descripción")
        print("3. Categoría")
        print("4. Precio")
        print("5. Stock")
        print("6. Proveedor")
        print("7. Estado")
        print("8. Volver")

        opcion = input("\nSeleccione una opción: ")

        datos_actualizados = {}
        if opcion == "1":
            while True:
                nombre = input("Nuevo nombre: ")
                resultado, mensaje = servicio.validar_nombre_producto(nombre)
                print(mensaje)
                if resultado:
                    datos_actualizados["nombre"] = nombre.strip()
                    break

        elif opcion == "2":
            while True:
                descripcion = input("Nueva descripción: ")
                resultado, mensaje = servicio.validar_descripcion_producto(descripcion)
                print(mensaje)
                if resultado:
                    datos_actualizados["descripcion"] = descripcion.strip()
                    break

        elif opcion == "3":
            while True:
                categoria = input("Nueva categoría: ")
                resultado, mensaje = servicio.validar_categoria_producto(categoria)
                print(mensaje)
                if resultado:
                    datos_actualizados["categoria"] = categoria.strip()
                    break

        elif opcion == "4":
            while True:
                precio = input("Nuevo precio: ")
                resultado, mensaje = servicio.validar_precio_producto(precio)
                print(mensaje)
                if resultado:
                    datos_actualizados["precio"] = float(precio)
                    break

        elif opcion == "5":
            while True:
                stock = input("Nuevo stock: ")
                resultado, mensaje = servicio.validar_stock_producto(stock)
                print(mensaje)
                if resultado:
                    datos_actualizados["stock"] = int(stock)
                    break

        elif opcion == "6":
            while True:
                proveedor = input("Nuevo proveedor: ")
                resultado, mensaje = servicio.validar_proveedor_producto(proveedor)
                print(mensaje)
                if resultado:
                    datos_actualizados["proveedor"] = proveedor.strip()
                    break

        elif opcion == "7":
            while True:
                estado = input("Nuevo estado (Activo/Inactivo): ").strip().title()
                resultado, mensaje = servicio.validar_estado_producto(estado)
                print(mensaje)
                if resultado:
                    datos_actualizados["estado"] = estado
                    break

        elif opcion == "8":
            break

        else:
            print("Opción no válida.")
            continue

        if len(datos_actualizados) > 0:
            resultado, mensaje = servicio.actualizar_producto(
                codigo,
                datos_actualizados
            )
            print(mensaje)

            
def desactivar_producto(servicio):
    print("\n========== DESACTIVAR PRODUCTO ==========")
    codigo = input("Ingrese código del producto: ")
    resultado, producto = servicio.buscar_producto_codigo(codigo)
    if not resultado:
        print(producto)
        return
    print("\n========== PRODUCTO ENCONTRADO ==========")
    print(f"{'Código':15}: {producto['codigo_producto']}")
    print(f"{'Nombre':15}: {producto['nombre']}")
    print(f"{'Precio':15}: ${producto['precio']}")
    print(f"{'Stock':15}: {producto['stock']}")
    print(f"{'Estado':15}: {producto['estado_mostrar']}")
    print("==========================================")
    while True:
        confirmar = input("\n¿Desea desactivar este producto? (S/N): ").strip().upper()
        if confirmar == "S":
            resultado, mensaje = servicio.desactivar_producto(codigo)
            print("\n" + mensaje)
            break
        elif confirmar == "N":
            print("Operación cancelada.")
            break
        else:
            print("Opción no válida. Ingrese S o N.")


def buscar_estado_producto(servicio):
    print("\n========== BUSCAR POR ESTADO ==========")
    print("1. Activo")
    print("2. Inactivo")
    print("3. Agotados")
    opcion = input("\nSeleccione: ")
    if opcion == "1":
        estado = "Activo"
    elif opcion == "2":
        estado = "Inactivo"
    elif opcion == "3":
        estado = "Agotado"
    else:
        print("Opción inválida.")
        return

    resultado, productos = servicio.buscar_productos_estado(estado)
    if not resultado:
        print(productos)
        return

    if len(productos) == 0:
        print("No existen productos con ese estado.")
        return

    for producto in productos:
        print("\n========== PRODUCTO ==========")
        print(f"{'Código':15}: {producto['codigo_producto']}")
        print(f"{'Nombre':15}: {producto['nombre']}")
        print(f"{'Precio':15}: ${producto['precio']}")
        print(f"{'Stock':15}: {producto['stock']}")
        print(f"{'Estado':15}: {producto['estado_mostrar']}")
        print("==============================")

from app.conexion import ConexionMongo
from app.servicios.servicio_pedido import ServicioPedido


def crear_pedido(servicio):
    print("\n========== REGISTRO PEDIDO ==========")
    # VALIDAR CLIENTE
    while True:
        rut = input("Ingrese RUT cliente: ").strip()
        resultado, mensaje = (
            servicio.servicio_cliente.validar_rut_cliente(rut)
        )
        if not resultado:
            print(mensaje)
            continue
        resultado, cliente = (
            servicio.servicio_cliente.buscar_cliente(rut)
        )
        if resultado:
            break
        else:
            print("El cliente no existe.")
    print("\nCliente encontrado:")
    print(f"Nombre : {cliente['nombre']}")
    print(f"Correo : {cliente['correo']}")
    carrito = []
    while True:
        print("\n========== AGREGAR PRODUCTO ==========")
        # BUSCAR PRODUCTO
        while True:
            codigo = input(
                "Ingrese código producto: "
            ).strip()
            resultado, producto = (
                servicio.servicio_producto.buscar_producto_codigo(
                    codigo
                )
            )
            if resultado:
                break
            print(producto)

        print("\nProducto encontrado:")
        print(f"Nombre : {producto['nombre']}")
        print(f"Precio : ${producto['precio']}")
        print(f"Stock  : {producto['stock']}")
        print(f"Estado : {producto['estado']}")


        # VALIDAR ESTADO
        if producto["estado"] == "Inactivo":
            print("El producto se encuentra inactivo.")
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
            else:
                print(
                    "La cantidad supera el stock disponible."
                )


        carrito.append({
            "codigo_producto": producto["codigo_producto"],
            "nombre": producto["nombre"],
            "precio": producto["precio"],
            "cantidad": cantidad,
            "subtotal": producto["precio"] * cantidad

        })
        print("\nProducto agregado al carrito.")
        continuar = input(
            "\n¿Desea agregar otro producto? (s/n): "
        )
        if continuar.lower() != "s":
            break

    print("\n========== RESUMEN PEDIDO ==========")
    for producto in carrito:
        print("\n----------------------")
        print(f"{'Producto':<12}: {producto['nombre']}")
        print(f"{'Cantidad':<12}: {producto['cantidad']}")
        print(f"{'Subtotal':<12}: ${producto['subtotal']}")

    total = servicio.calcular_total(carrito)

    print("\n----------------------")
    print(f"{'TOTAL':<12}: ${total}")

    confirmar = input(
        "\n¿Confirmar pedido? (s/n): "
    )
    if confirmar.lower() == "s":
        resultado, mensaje = (
            servicio.registrar_pedido(
                rut,
                carrito
            )
        )
        print("\n" + mensaje)
    else:
        print("Pedido cancelado.")



def principal():
    conexion = ConexionMongo()
    db = conexion.obtener_db()
    servicio = ServicioPedido(db)
    crear_pedido(servicio)



if __name__ == "__main__":
    principal()