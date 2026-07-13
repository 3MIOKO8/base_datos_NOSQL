from datetime import datetime
from pymongo import ReturnDocument

from app.servicios.servicio_cliente import ServicioCliente
from app.servicios.servicio_producto import ServicioProducto

from app.validaciones import (
    validar_cantidad_pedido,
    validar_estado_pedido
)


class ServicioPedido:
    def __init__(self, db):

        self.pedidos = db["pedidos"]
        self.contadores = db["contadores"]

        self.servicio_cliente = ServicioCliente(db)
        self.servicio_producto = ServicioProducto(db)

    def devolver_stock(self, codigo_producto, cantidad):
        try:
            resultado, producto = (
                self.servicio_producto.buscar_producto_codigo(
                    codigo_producto
                )
            )
            if not resultado:
                return False, (
                    "No se pudo devolver stock. "
                    "Producto no encontrado."
                )
            nuevo_stock = producto["stock"] + cantidad
            self.servicio_producto.coleccion.update_one(
                {
                    "codigo_producto": codigo_producto
                },
                {
                    "$set": {
                        "stock": nuevo_stock
                    }
                }
            )
            return True, "Stock devuelto correctamente."
        except Exception as error:
            return False, (
                f"Error al devolver stock: {error}")

    def generar_codigo_pedido(self):
        contador = self.contadores.find_one_and_update(
            {
                "_id": "pedidos"
            },
            {
                "$inc": {
                    "ultimo_codigo": 1
                }
            },
            return_document=ReturnDocument.AFTER
        )
        numero = contador["ultimo_codigo"]
        codigo = f"PD{numero:09d}"
        return codigo



    def validar_cantidad_pedido(self, cantidad):
        if not validar_cantidad_pedido(cantidad):
            return False, (
                "La cantidad debe ser "
                "un número entero mayor a 0."
            )
        return True, "Cantidad válida."



    def validar_estado_pedido(self, estado):
        if not validar_estado_pedido(estado):
            return False, (
                "El estado debe ser Pendiente, "
                "Completado o Cancelado."
            )
        return True, "Estado válido."



    def calcular_total(self, carrito):
        total = 0
        for producto in carrito:
            total += producto["subtotal"]
        return total

    #CRUD PEDIDO
    def registrar_pedido(self, rut_cliente, carrito):
        resultado, cliente = (
            self.servicio_cliente.buscar_cliente_pedido(
                rut_cliente
            )
        )
        if not resultado:
            return False, cliente
        if not carrito:
            return False, (
                "Debe agregar al menos un producto al pedido."
            )



        for item in carrito:
            resultado, producto = (
                self.servicio_producto.buscar_producto_pedido(
                    item["codigo_producto"]
                )
            )

            if not resultado:
                return False, producto

            if item["cantidad"] > producto["stock"]:
                return False, (
                    f"Stock insuficiente para "
                    f"{producto['nombre']}."
                )



        total = self.calcular_total(carrito)
        codigo = self.generar_codigo_pedido()
        pedido = {
            "codigo_pedido": codigo,
            "cliente_rut": rut_cliente,
            "productos": carrito,
            "total": total,
            "estado": "Pendiente",
            "fecha_pedido": datetime.now()
        }

        try:
            for item in carrito:
                resultado, mensaje = (
                    self.servicio_producto.descontar_stock(
                        item["codigo_producto"],
                        item["cantidad"]
                    )
                )
                if not resultado:
                    return False, mensaje

            self.pedidos.insert_one(pedido)
            return True, (
                f"Pedido {codigo} "
                "registrado correctamente."
            )
        except Exception as error:
            return False, (
                f"Error al registrar pedido: {error}")

    def listar_pedidos(self):
        try:
            pedidos = list(
                self.pedidos.find()
            )
            if not pedidos:
                return False, "No existen pedidos registrados."

            return True, pedidos
        except Exception as error:
            return False, f"Error al listar pedidos: {error}"

    def buscar_pedido_codigo(self, codigo):
        try:
            codigo = codigo.strip().upper()
            pedido = self.pedidos.find_one(
                {
                    "codigo_pedido": codigo
                }
            )
            if not pedido:
                return False, "El pedido no existe."

            return True, pedido
        except Exception as error:
            return False, f"Error al buscar pedido: {error}"

    def buscar_pedidos_cliente(self, rut_cliente):
        try:
            pedidos = list(
                self.pedidos.find(
                    {
                        "cliente_rut": rut_cliente
                    }
                )
            )
            if not pedidos:
                return False, "El cliente no tiene pedidos registrados."
            return True, pedidos
        except Exception as error:
            return False, f"Error al buscar pedidos del cliente: {error}"
    
    def cambiar_estado_pedido(self, codigo, nuevo_estado):
        try:
            codigo = codigo.strip().upper()
            pedido = self.pedidos.find_one(
                {
                    "codigo_pedido": codigo
                }
            )
            if not pedido:
                return False, (
                    "El pedido no existe."
                )
            estado_actual = pedido["estado"]
            if estado_actual == "Completado":
                return False, (
                    "Un pedido completado "
                    "no puede modificarse."
                )
            if estado_actual == "Cancelado":
                return False, (
                    "Un pedido cancelado "
                    "no puede modificarse."
                )
            if nuevo_estado == "Cancelado":
                for producto in pedido["productos"]:
                    resultado, mensaje = (
                        self.devolver_stock(
                            producto["codigo_producto"],
                            producto["cantidad"]
                        )
                    )
                    if not resultado:
                        return False, mensaje
            self.pedidos.update_one(
                {
                    "codigo_pedido": codigo
                },
                {
                    "$set": {
                        "estado": nuevo_estado
                    }
                }
            )
            return True, (
                f"Pedido {codigo} "
                f"cambiado a {nuevo_estado}."
            )
        except Exception as error:
            return False, (
                f"Error al cambiar estado: {error}")
    

    
    
