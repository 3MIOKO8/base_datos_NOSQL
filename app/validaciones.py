import re

def validar_nombre(nombre):
    nombre = nombre.strip()
    if not nombre:
        return False
    if len(nombre) < 3:
        return False
    if len(nombre) > 100:
        return False
    patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$"
    return bool(re.fullmatch(patron, nombre))

def validar_correo(correo):
    correo = correo.strip().lower()
    if not correo:
        return False
    patron = (
        r"^[a-zA-Z0-9._%+-]+"
        r"@[a-zA-Z0-9.-]+"
        r"\.[a-zA-Z]{2,}$"
    )
    return bool(re.fullmatch(patron, correo))

def validar_telefono(telefono):
    telefono = telefono.replace(" ", "")
    if not telefono:
        return False
    patron = r"^(\+569|9)\d{8}$"
    return bool(re.fullmatch(patron, telefono))

def validar_estado(estado):
    estado = estado.strip().title()
    estados = [
        "Activo",
        "Inactivo"
    ]
    return estado in estados

def calcular_dv(cuerpo):
    suma = 0
    multiplicador = 2
    for digito in reversed(cuerpo):
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
    resto = suma % 11
    resultado = 11 - resto
    if resultado == 11:
        return "0"
    if resultado == 10:
        return "K"
    return str(resultado)
    
def validar_rut(rut):
    rut = rut.strip().upper()
    rut = rut.replace(".", "")
    rut = rut.replace("-", "")
    if len(rut) < 2:
        return False
    cuerpo = rut[:-1]
    dv_ingresado = rut[-1]
    if not 7 <= len(cuerpo) <= 8:
        return False
    if not cuerpo.isdigit():
        return False
    dv_calculado = calcular_dv(cuerpo)
    return dv_calculado == dv_ingresado

def validar_calle(calle):
    calle = calle.strip()
    if not calle:
        return False
    if not (3 <= len(calle) <= 100):
        return False
    return True

def validar_numero_direccion(numero):
    numero = numero.strip()
    if not numero:
        return False
    if not numero.isdigit():
        return False
    if len(numero) > 10:
        return False
    return True

def validar_ciudad(ciudad):
    ciudad = ciudad.strip()
    if not ciudad:
        return False
    if not (3 <= len(ciudad) <= 50):
        return False
    patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$"
    return bool(re.fullmatch(patron, ciudad))

def validar_region(region):
    region = region.strip()
    if not region:
        return False
    if not (3 <= len(region) <= 50):
        return False
    patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\- ]+$"
    return bool(re.fullmatch(patron, region))


#productos 

def validar_nombre_producto(nombre):
    nombre = nombre.strip()
    if not nombre:
        return False
    if len(nombre) < 3:
        return False
    if len(nombre) > 100:
        return False
    return True

def validar_descripcion_producto(descripcion):
    descripcion = descripcion.strip()
    if not descripcion:
        return False
    if len(descripcion) > 255:
        return False
    return True

def validar_categoria_producto(categoria):
    categoria = categoria.strip()
    if not categoria:
        return False
    if len(categoria) < 3:
        return False
    if len(categoria) > 50:
        return False
    patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$"
    return bool(re.fullmatch(patron, categoria))

def validar_precio_producto(precio):
    try:
        precio = float(precio)
    except ValueError:
        return False
    if precio <= 0:
        return False
    return True

def validar_stock_producto(stock):
    try:
        stock = int(stock)
    except ValueError:
        return False
    if stock < 0:
        return False
    return True

def validar_proveedor_producto(proveedor):
    proveedor = proveedor.strip()
    if not proveedor:
        return False
    if len(proveedor) < 3:
        return False
    if len(proveedor) > 100:
        return False
    patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9 .\-]+$"
    return bool(re.fullmatch(patron, proveedor))

def validar_estado_producto(estado):
    estado = estado.strip().title()
    estados = [
        "Activo",
        "Inactivo"
    ]
    return estado in estados


#pedidos
def validar_cantidad_pedido(cantidad):

    cantidad = cantidad.strip()

    if not cantidad:
        return False

    if not cantidad.isdigit():
        return False

    if int(cantidad) <= 0:
        return False

    return True

def validar_estado_pedido(estado):

    estado = estado.strip().title()

    estados_validos = [
        "Pendiente",
        "Completado",
        "Cancelado"
    ]

    return estado in estados_validos

def validar_codigo_pedido(codigo):

    codigo = codigo.strip().upper()

    patron = r"^PD\d{9}$"

    return bool(re.fullmatch(patron, codigo))