from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


class ConexionMongo:

    def __init__(self):

        self.host = "localhost"
        self.puerto = 27018
        self.usuario = "app_gestion"
        self.password = "AppPassword2026"
        self.base_datos = "ComercioTech"

        self.cliente = None
        self.db = None


    def conectar(self):

        try:

            self.cliente = MongoClient(
                host=self.host,
                port=self.puerto,
                username=self.usuario,
                password=self.password,
                authSource=self.base_datos,
                authMechanism="SCRAM-SHA-256",
                serverSelectionTimeoutMS=5000
            )

            self.cliente[self.base_datos].command("ping")

            self.db = self.cliente[self.base_datos]

            print("[EXITO] Conexión exitosa a MongoDB")

            return self.db


        except ConnectionFailure as error:

            print("[ERROR] Error conectando a MongoDB")
            print(error)

            return None


    def obtener_db(self):

        if self.db is None:
            return self.conectar()

        return self.db


    def cerrar(self):

        if self.cliente:

            self.cliente.close()
            print("Conexión cerrada")