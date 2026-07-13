from app.utilidades import limpiar_pantalla


def menu_producto(servicio):

    while True:

        limpiar_pantalla()

        print("\n========== GESTIÓN PRODUCTOS ==========")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Buscar producto por código")
        print("4. Actualizar producto")
        print("5. Desactivar producto")
        print("6. Buscar productos por estado")
        print("x. Volver")
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            registrar_producto(servicio)
        elif opcion == "2":
            listar_productos(servicio)
        elif opcion == "3":
            buscar_producto(servicio)
        elif opcion == "4":
            actualizar_producto(servicio)
        elif opcion == "5":
            desactivar_producto(servicio)
        elif opcion == "6":
            buscar_estado_producto(servicio)
        elif opcion == "x":
            break
        else:
            print("Opción no válida.")
        input("\nPresione Enter para continuar...")


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
        print("x. Volver")

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

        elif opcion == "x":
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
    print("x. Volver")
    opcion = input("\nSeleccione: ")
    if opcion == "1":
        estado = "Activo"
    elif opcion == "2":
        estado = "Inactivo"
    elif opcion == "3":
        estado = "Agotado"
    elif opcion == "x":
        return
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



