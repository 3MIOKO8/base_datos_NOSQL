from app.utilidades import limpiar_pantalla

def menu_cliente(servicio):

    while True:
        limpiar_pantalla()

        print("\n========== GESTIÓN CLIENTES ==========")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente por RUT")
        print("4. Actualizar cliente")
        print("5. Desactivar cliente")
        print("6. Buscar clientes por estado")
        print("x. Volver")

        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            registrar_cliente(servicio)
        elif opcion == "2":
            listar_clientes(servicio)
        elif opcion == "3":
            buscar_cliente(servicio)
        elif opcion == "4":
            actualizar_cliente(servicio)
        elif opcion == "5":
            eliminar_cliente(servicio)
        elif opcion == "6":
            buscar_por_estado(servicio)
        elif opcion == "x":
            break
        else:
            print("Opción no válida.")
    
        input("\nPresione Enter para continuar...")


def registrar_cliente(servicio):
    print("\n========== REGISTRO CLIENTE ==========")
    # RUT
    while True:
        rut = input("Ingrese RUT: ")
        resultado, mensaje = servicio.validar_rut_cliente(rut)
        print(mensaje)
        if resultado:
            break
    # Nombre
    while True:
        nombre = input("Ingrese nombre: ")
        resultado, mensaje = servicio.validar_nombre_cliente(nombre)
        print(mensaje)
        if resultado:
            break
    # Correo
    while True:
        correo = input("Ingrese correo: ")
        resultado, mensaje = servicio.validar_correo_cliente(correo)
        print(mensaje)
        if resultado:
            break
    # Teléfono
    while True:
        telefono = input("Ingrese teléfono: ")
        resultado, mensaje = servicio.validar_telefono_cliente(telefono)
        print(mensaje)
        if resultado:
            break
    # Dirección
    while True:
        calle = input("Calle: ")
        resultado, mensaje = servicio.validar_calle_cliente(calle)
        print(mensaje)
        if resultado:
            break
    while True:
        numero = input("Número: ")
        resultado, mensaje = servicio.validar_numero_cliente(numero)
        print(mensaje)
        if resultado:
            break
    while True:
        ciudad = input("Ciudad: ")
        resultado, mensaje = servicio.validar_ciudad_cliente(ciudad)
        print(mensaje)
        if resultado:
            break
    while True:
        region = input("Región: ")
        resultado, mensaje = servicio.validar_region_cliente(region)
        print(mensaje)
        if resultado:
            break

    direccion = {
        "calle": calle.strip(),
        "numero": numero.strip(),
        "ciudad": ciudad.strip(),
        "region": region.strip()
    }

    resultado, mensaje = servicio.registrar_cliente(
        rut,
        nombre,
        correo,
        telefono,
        direccion
    )
    print("\n" + mensaje)



def listar_clientes(servicio):
    resultado, clientes = servicio.listar_clientes()
    if resultado:
        print("\n========== CLIENTES ==========")

        for cliente in clientes:

            print("\n----------------------")

            print(f"{'RUT':<10}: {cliente['rut']}")
            print(f"{'Nombre':<10}: {cliente['nombre']}")
            print(f"{'Correo':<10}: {cliente['correo']}")
            print(f"{'Teléfono':<10}: {cliente['telefono']}")

            print("Dirección:")

            print(f"  {'Calle':<8}: {cliente['direccion']['calle']}")
            print(f"  {'Número':<8}: {cliente['direccion']['numero']}")
            print(f"  {'Ciudad':<8}: {cliente['direccion']['ciudad']}")
            print(f"  {'Región':<8}: {cliente['direccion']['region']}")

            print(f"{'Estado':<10}: {cliente['estado']}")
    else:
        print(clientes)

def buscar_cliente(servicio):
    print("\n========== BUSCAR CLIENTE ==========")

    rut = input("Ingrese RUT del cliente: ")
    resultado, cliente = servicio.buscar_cliente(rut)
    if resultado:

        print("\n========== CLIENTE ENCONTRADO ==========")

        print(f"{'RUT':<10}: {cliente['rut']}")
        print(f"{'Nombre':<10}: {cliente['nombre']}")
        print(f"{'Correo':<10}: {cliente['correo']}")
        print(f"{'Teléfono':<10}: {cliente['telefono']}")
        print(f"{'Estado':<10}: {cliente['estado']}")

        print("\nDirección:")

        print(f"  {'Calle':<8}: {cliente['direccion']['calle']}")
        print(f"  {'Número':<8}: {cliente['direccion']['numero']}")
        print(f"  {'Ciudad':<8}: {cliente['direccion']['ciudad']}")
        print(f"  {'Región':<8}: {cliente['direccion']['region']}")

    else:
        print(cliente)

def buscar_por_estado(servicio):
    print("\n========== BUSCAR POR ESTADO ==========")
    while True:
        estado = input(
            "Ingrese estado (Activo/Inactivo): "
        ).strip().title()
        if estado in ["Activo", "Inactivo"]:
            break
        print("Estado inválido. Ingrese Activo o Inactivo.")
    resultado, clientes = servicio.buscar_por_estado(estado)
    if resultado:
        print(
            f"\n========== CLIENTES {estado.upper()} =========="
        )
        print(
            f"{'RUT':<15}"
            f"{'NOMBRE':<25}"
            f"{'CORREO':<30}"
            f"{'TELÉFONO':<15}"
        )
        print("-" * 85)
        for cliente in clientes:
            print(
                f"{cliente['rut']:<15}"
                f"{cliente['nombre']:<25}"
                f"{cliente['correo']:<30}"
                f"{cliente['telefono']:<15}"
            )
    else:
        print(clientes)


def actualizar_cliente(servicio):
    print("\n========== ACTUALIZAR CLIENTE ==========")
    rut = input("Ingrese RUT del cliente: ")

    resultado, cliente = servicio.buscar_cliente(rut)

    if not resultado:
        print(cliente)
        return

    while True:
        limpiar_pantalla()
        print("\n========== ACTUALIZAR CLIENTE ==========")
        print("\nCliente actual:")
        print(f"Nombre: {cliente['nombre']}")
        print(f"Correo: {cliente['correo']}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Estado: {cliente['estado']}")

        print("\n¿Qué desea modificar?")
        print("1. Nombre")
        print("2. Correo")
        print("3. Teléfono")
        print("4. Dirección")
        print("5. Estado")
        print("x. Volver")

        opcion = input("Seleccione: ")

        if opcion == "x":
            break

        cambios = {}

        if opcion == "1":
            while True:
                nombre = input("Nuevo nombre: ")
                resultado, mensaje = servicio.validar_nombre_cliente(nombre)
                print(mensaje)
                if resultado:
                    cambios["nombre"] = nombre.strip()
                    break

        elif opcion == "2":
            while True:
                correo = input("Nuevo correo: ")
                resultado, mensaje = servicio.validar_correo_cliente(correo)
                print(mensaje)
                if resultado:
                    cambios["correo"] = correo.strip().lower()
                    break

        elif opcion == "3":
            while True:
                telefono = input("Nuevo teléfono: ")
                resultado, mensaje = servicio.validar_telefono_cliente(telefono)
                print(mensaje)
                if resultado:
                    cambios["telefono"] = telefono.strip()
                    break

        elif opcion == "4":
            print("\nNueva dirección:")
            while True:
                calle = input("Calle: ")
                resultado, mensaje = servicio.validar_calle_cliente(calle)
                print(mensaje)
                if resultado:
                    break
            while True:
                numero = input("Número: ")
                resultado, mensaje = servicio.validar_numero_cliente(numero)
                print(mensaje)
                if resultado:
                    break
            while True:
                ciudad = input("Ciudad: ")
                resultado, mensaje = servicio.validar_ciudad_cliente(ciudad)
                print(mensaje)
                if resultado:
                    break
            while True:
                region = input("Región: ")
                resultado, mensaje = servicio.validar_region_cliente(region)
                print(mensaje)
                if resultado:
                    break
            cambios["direccion"] = {
                "calle": calle.strip(),
                "numero": numero.strip(),
                "ciudad": ciudad.strip(),
                "region": region.strip()
            }
        elif opcion == "5":
            while True:
                estado = input("Nuevo estado (Activo/Inactivo): ").strip().title()
                if estado in ["Activo", "Inactivo"]:
                    cambios["estado"] = estado
                    break
                print("Estado inválido.")
        else:
            print("Opción inválida.")
            input("\nPresione Enter para continuar...")
            continue

        resultado, mensaje = servicio.actualizar_cliente(rut, cambios)
        print(mensaje)
        
        if resultado:
            # Refrescar datos locales del cliente para mostrar el cambio en el menú
            _, cliente = servicio.buscar_cliente(rut)

        input("\nPresione Enter para continuar...")


def eliminar_cliente(servicio):
    print("\n========== ELIMINAR CLIENTE ==========")

    rut = input("Ingrese RUT del cliente: ")
    resultado, mensaje = servicio.eliminar_cliente(rut)
    print(mensaje)

