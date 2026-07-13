from datetime import datetime
from pymongo import ReturnDocument

from app.validaciones import (
    validar_nombre_producto,
    validar_descripcion_producto,
    validar_categoria_producto,
    validar_precio_producto,
    validar_stock_producto,
    validar_proveedor_producto,
    validar_estado_producto
)



class ServicioProducto:
    def __init__(self, db):

        self.coleccion = db["productos"]
        self.contadores = db["contadores"]

    def generar_codigo_producto(self):
        contador = self.contadores.find_one_and_update(
            {
                "_id": "productos"
            },

            {
                "$inc": {
                    "ultimo_codigo": 1
                }
            },
            return_document=ReturnDocument.AFTER
        )
        numero = contador["ultimo_codigo"]
        codigo = f"P{numero:05d}"
        return codigo
    
    def buscar_producto_pedido(self, codigo_producto):
        codigo_producto = codigo_producto.strip().upper()
        producto = self.coleccion.find_one(
            {
                "codigo_producto": codigo_producto
            }
        )
        if not producto:
            return False, "El producto no existe."
        if producto["estado"] == "Inactivo":
            return False, "El producto se encuentra inactivo."
        return True, producto
    

    def validar_nombre_producto(self, nombre):
        if not validar_nombre_producto(nombre):
            return False, "El nombre del producto no es válido."
        return True, "Nombre válido."

    def validar_descripcion_producto(self, descripcion):
        if not validar_descripcion_producto(descripcion):
            return False, "La descripción no es válida."
        return True, "Descripción válida."
        
    def validar_categoria_producto(self, categoria):
        if not validar_categoria_producto(categoria):
            return False, "La categoría no es válida."
        return True, "Categoría válida."
        
    def validar_precio_producto(self, precio):
        if not validar_precio_producto(precio):
            return False, "El precio debe ser mayor a 0."
        return True, "Precio válido."
        
    def validar_stock_producto(self, stock):
        if not validar_stock_producto(stock):
            return False, "El stock debe ser un número mayor o igual a 0."
        return True, "Stock válido."
        
    def validar_proveedor_producto(self, proveedor):
        if not validar_proveedor_producto(proveedor):
            return False, "El proveedor no es válido."
        return True, "Proveedor válido."
        
    def validar_estado_producto(self, estado):
        if not validar_estado_producto(estado):
            return False, "El estado debe ser Activo o Inactivo."
        return True, "Estado válido."
    def descontar_stock(self, codigo_producto, cantidad):
        try:
            producto = self.coleccion.find_one(
                {
                    "codigo_producto": codigo_producto
                }
            )
            if not producto:
                return False, "Producto no encontrado."
            nuevo_stock = producto["stock"] - cantidad
            if nuevo_stock < 0:
                return False, "Stock insuficiente."
            self.coleccion.update_one(
                {
                    "codigo_producto": codigo_producto
                },

                {
                    "$set": {
                        "stock": nuevo_stock
                    }
                }
            )
            return True, "Stock actualizado correctamente."
        except Exception as error:
            return False, f"Error al descontar stock: {error}"
    

    #CRUD PRODUCTO
    def registrar_producto(self,nombre,descripcion,categoria,precio,stock,proveedor,estado):
        try:
            codigo = self.generar_codigo_producto()
            producto = {
                "codigo_producto": codigo,
                "nombre": nombre.strip(),
                "descripcion": descripcion.strip(),
                "categoria": categoria.strip(),
                "precio": float(precio),
                "stock": int(stock),
                "proveedor": proveedor.strip(),
                "estado": estado.strip().title(),
                "fecha_creacion": datetime.now()
            }
            self.coleccion.insert_one(producto)
            return True, f"Producto registrado correctamente. Código asignado: {codigo}"
        except Exception as error:
            return False, f"Error al registrar producto: {error}"
    
    def listar_productos(self):
        try:
            productos = list(self.coleccion.find())
            lista_productos = []
            for producto in productos:
                if producto["estado"] == "Inactivo":
                    estado_mostrar = "Inactivo"
                elif producto["stock"] == 0:
                    estado_mostrar = "Agotado"

                else:
                    estado_mostrar = "Activo"
                producto["estado_mostrar"] = estado_mostrar
                lista_productos.append(producto)

            return True, lista_productos
        except Exception as error:
            return False, f"Error al listar productos: {error}"

    def buscar_producto_codigo(self, codigo):
        try:
            codigo = codigo.strip().upper()
            producto = self.coleccion.find_one(
                {
                    "codigo_producto": codigo
                }
            )
            if producto is None:
                return False, "El producto no existe."
            if producto["estado"] == "Inactivo":
                estado_mostrar = "Inactivo"
            elif producto["stock"] == 0:
                estado_mostrar = "Agotado"
            else:
                estado_mostrar = "Activo"
            producto["estado_mostrar"] = estado_mostrar
            return True, producto
        except Exception as error:
            return False, f"Error al buscar producto: {error}"

    def actualizar_producto(self, codigo, datos_actualizados):
        try:
            codigo = codigo.strip().upper()
            producto = self.coleccion.find_one(
                {
                    "codigo_producto": codigo
                }
            )
            if producto is None:
                return False, "El producto no existe."
            resultado = self.coleccion.update_one(
                {
                    "codigo_producto": codigo
                },

                {
                    "$set": datos_actualizados
                }
            )
            if resultado.modified_count == 0:
                return False, "No se realizaron cambios en el producto."
            return True, "Producto actualizado correctamente."
        except Exception as error:
            return False, f"Error al actualizar producto: {error}"

    def desactivar_producto(self, codigo):
        try:
            codigo = codigo.strip().upper()
            producto = self.coleccion.find_one(
                {
                    "codigo_producto": codigo
                }
            )
            if producto is None:
                return False, "El producto no existe."
            resultado = self.coleccion.update_one(
                {
                    "codigo_producto": codigo
                },

                {
                    "$set": {
                        "estado": "Inactivo"
                    }
                }
            )
            if resultado.modified_count == 0:
                return False, "El producto ya se encuentra inactivo."
            return True, "Producto desactivado correctamente."
        except Exception as error:
            return False, f"Error al desactivar producto: {error}"

    def buscar_productos_estado(self, estado):
        try:
            estado = estado.strip().title()
            if estado == "Activo":
                filtro = {
                    "estado": "Activo",
                    "stock": {
                        "$gt": 0
                    }
                }
            elif estado == "Inactivo":
                filtro = {
                    "estado": "Inactivo"
                }
            elif estado == "Agotado":
                filtro = {
                    "estado": "Activo",
                    "stock": 0
                }
            else:
                return False, "Estado no válido."
            productos = self.coleccion.find(filtro)
            lista_productos = []
            for producto in productos:
                if producto["estado"] == "Inactivo":
                    estado_mostrar = "Inactivo"
                elif producto["stock"] == 0:
                    estado_mostrar = "Agotado"
                else:
                    estado_mostrar = "Activo"
                producto["estado_mostrar"] = estado_mostrar
                lista_productos.append(producto)
            return True, lista_productos
        except Exception as error:
            return False, f"Error al buscar productos por estado: {error}"
            

        


    

        
