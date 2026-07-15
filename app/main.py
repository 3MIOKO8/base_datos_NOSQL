from app.conexion import ConexionMongo

from app.servicios.servicio_cliente import ServicioCliente
from app.servicios.servicio_producto import ServicioProducto
from app.servicios.servicio_pedido import ServicioPedido

from app.menus.menu_principal import menu_principal


def principal():

    conexion = ConexionMongo()

    db = conexion.obtener_db()

    servicio_cliente = ServicioCliente(db)
    servicio_producto = ServicioProducto(db)
    servicio_pedido = ServicioPedido(db)


    menu_principal(
        servicio_cliente,
        servicio_producto,
        servicio_pedido
    )


if __name__ == "__main__":
    principal()