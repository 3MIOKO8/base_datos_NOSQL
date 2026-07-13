from app.validaciones import (
    validar_rut,
    validar_nombre,
    validar_correo,
    validar_telefono,
    validar_estado,
    validar_calle,
    validar_numero_direccion,
    validar_ciudad,
    validar_region
)


class ServicioCliente:

    def __init__(self, db):

        self.coleccion = db["clientes"]
    
    def buscar_cliente_pedido(self, rut):
        rut = rut.strip().upper().replace(".", "").replace("-", "")
        cliente = self.coleccion.find_one(
            {
                "rut": rut
            }
        )
        if not cliente:
            return False, "El cliente no existe."
        if cliente["estado"] == "Inactivo":
            return False, "El cliente se encuentra inactivo."
        return True, cliente
    
    #valida la existencia de estos parametros que son los importantes
    def existe_rut(self, rut):

        return self.coleccion.find_one({
            "rut": rut
        })


    def existe_correo(self, correo):

        return self.coleccion.find_one({
            "correo": correo
        })


    def existe_telefono(self, telefono):

        return self.coleccion.find_one({
            "telefono": telefono
        })





    #estos si son validadores pero logicos del modelo de cliente por eso no van en validadores 
    #ya que ahi van solo validadores logicos genericos que pueden funcionar para otras cosas a futuro
    def validar_rut_cliente(self, rut):

        rut = rut.strip().upper().replace(".", "").replace("-", "")

        if not validar_rut(rut):

            return False, "El RUT ingresado no es válido."


        if self.existe_rut(rut):

            return False, "El RUT ya se encuentra registrado."


        return True, "RUT válido."

    def validar_nombre_cliente(self, nombre):

        nombre = nombre.strip()

        if not validar_nombre(nombre):

            return False, "El nombre ingresado no es válido."

        return True, "Nombre válido."

    def validar_correo_cliente(self, correo):

        correo = correo.strip().lower()

        if not validar_correo(correo):

            return False, "El correo electrónico ingresado no es válido."


        if self.existe_correo(correo):

            return False, "El correo electrónico ya se encuentra registrado."


        return True, "Correo válido."

    def validar_telefono_cliente(self, telefono):

        telefono = telefono.strip()

        if not validar_telefono(telefono):

            return False, "El teléfono ingresado no es válido."


        if self.existe_telefono(telefono):

            return False, "El teléfono ya se encuentra registrado."


        return True, "Teléfono válido."
    
    def validar_calle_cliente(self, calle):
        if not validar_calle(calle):
            return False, "La calle ingresada no es válida (entre 3 y 100 caracteres)."
        return True, "Calle válida."

    def validar_numero_cliente(self, numero):
        if not validar_numero_direccion(numero):
            return False, "El número ingresado no es válido (solo dígitos, máximo 10)."
        return True, "Número válido."

    def validar_ciudad_cliente(self, ciudad):
        if not validar_ciudad(ciudad):
            return False, "La ciudad ingresada no es válida (solo letras, entre 3 y 50 caracteres)."
        return True, "Ciudad válida."

    def validar_region_cliente(self, region):
        if not validar_region(region):
            return False, "La región ingresada no es válida (solo letras o guiones, entre 3 y 50 caracteres)."
        return True, "Región válida."

    #aca recien empieza el CRUD
    def registrar_cliente(self,rut,nombre,correo,telefono,direccion,estado="Activo"):
        try:
            cliente = {
                "rut": rut.strip().upper().replace(".", "").replace("-", ""),

                "nombre": nombre.strip(),

                "correo": correo.strip().lower(),

                "telefono": telefono.strip(),

                "direccion": direccion,

                "estado": estado.strip().title()
            }
            self.coleccion.insert_one(cliente)
            return True, "Cliente registrado correctamente."
        except Exception as error:
            return False, f"Error al registrar cliente: {error}"

    def listar_clientes(self):
        try:

            clientes = list(
                self.coleccion.find(
                    {},
                    {
                        "_id": 0
                    }
                )
            )
            if not clientes:
                return False, "No existen clientes registrados."
            return True, clientes
        except Exception as error:
            return False, f"Error al listar clientes: {error}"

    def buscar_cliente(self, rut):
        try:
            cliente = self.coleccion.find_one(
                {
                    "rut": rut.strip().upper().replace(".", "").replace("-", "")
                },
                {
                    "_id": 0
                }
            )
            if not cliente:
                return False, "No existe un cliente con ese RUT."
            return True, cliente
        except Exception as error:
            return False, f"Error al buscar cliente: {error}"
    
    #estas dos son importantes para el codigo de actualizar
    def existe_correo_otro_cliente(self, correo, rut):

        cliente = self.coleccion.find_one(
            {
                "correo": correo,
                "rut": {
                    "$ne": rut
                }
            }
        )

        return cliente is not None
    #esta tambien es importante para en caso de colocar el mismo telular si se 
    #peuda colocar ya que de por si es de ese cliente
    def existe_telefono_otro_cliente(self, telefono, rut):

        cliente = self.coleccion.find_one(
            {
                "telefono": telefono,
                "rut": {
                    "$ne": rut
                }
            }
        )

        return cliente is not None
    
    def actualizar_cliente(self, rut, cambios):
        try:
            rut_normalizado = rut.strip().upper().replace(".", "").replace("-", "")

            # Normalizar estado si viene en los cambios
            if "estado" in cambios:
                estado_norm = cambios["estado"].strip().title()
                if estado_norm not in ["Activo", "Inactivo"]:
                    return False, "El estado ingresado no es válido."
                cambios["estado"] = estado_norm

            cliente = self.coleccion.find_one({"rut": rut_normalizado})
            if not cliente:
                return False, "El cliente no existe."

            resultado = self.coleccion.update_one(
                {"rut": rut_normalizado},
                {"$set": cambios}
            )
            if resultado.modified_count == 0:
                return False, "No se realizaron cambios."
            return True, "Cliente actualizado correctamente."

        except Exception as error:
            return False, f"Error al actualizar cliente: {error}"
    
    def eliminar_cliente(self, rut):
        try:
            cliente = self.coleccion.find_one(
                {
                    "rut": rut.strip().upper().replace(".", "").replace("-", "")
                }
            )
            if not cliente:
                return False, "El cliente no existe."

            resultado = self.coleccion.update_one(
                {
                    "rut": rut.strip().upper().replace(".", "").replace("-", "")
                },
                {
                    "$set": {
                        "estado": "Inactivo"
                    }
                }
            )

            if resultado.modified_count == 0:
                return False, "El cliente ya se encuentra inactivo."
            return True, "Cliente desactivado correctamente."

        except Exception as error:
            return False, f"Error al eliminar cliente: {error}"

    def buscar_por_estado(self, estado):
        try:
            estado = estado.strip().title()
            if estado not in ["Activo", "Inactivo"]:
                return False, "Estado no válido. Use 'Activo' o 'Inactivo'."
            clientes = list(
                self.coleccion.find(
                    {"estado": estado},
                    {"_id": 0}
                )
            )
            if not clientes:
                return False, f"No existen clientes con estado {estado}."
            return True, clientes
        except Exception as error:
            return False, f"Error al buscar clientes por estado: {error}"