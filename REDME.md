# Hoja de Ruta - Lógica de la Base de Datos (MongoDB)

## Estado general del proyecto

### Base de datos

* [x] Base de datos creada: **ComercioTech**
* [x] Colección **clientes**
* [x] Colección **productos**
* [x] Colección **pedidos**
* [x] Colección **contadores** (para códigos incrementales)
* [ ] Índices únicos
* [x] Usuario administrador
* [x] Usuario de la aplicación (app_gestion)
* [ ] Backups automáticos probados

---

# Colección: Clientes

### Estructura

* _id (ObjectId automático de MongoDB)
* rut
* nombre
* correo
* telefono
* direccion (subdocumento)
    * calle
    * numero
    * ciudad
    * region
* estado
* fecha_registro

### Reglas de negocio

* [ ] El RUT no puede repetirse.
* [ ] Buscar clientes siempre por RUT.
* [ ] Validar formato del RUT.
* [ ] Validar correo.
* [ ] Validar teléfono.
* [ ] Estado permitido:

  * Activo
  * Inactivo

---

# Colección: Productos

### Estructura

* _id (ObjectId automático)
* codigo_producto
* nombre
* descripcion
* categoria
* precio
* stock
* proveedor
* estado
* fecha_creacion

### Reglas de negocio

* [x] codigo_producto debe ser único.
* [x] El código NO se escribe manualmente.
* [x] El código se genera automáticamente mediante la colección **contadores**.
* [x] Validar que el precio sea mayor que 0.
* [x] Validar que el stock sea mayor o igual a 0.
* [x] Validar longitud de nombre y descripción.
* [x] Estados permitidos:

  * Activo
  * Inactivo

### Importante

No se almacenará el estado "Agotado".

Cuando:

stock == 0

la aplicación mostrará automáticamente:

"Agotado"

sin modificar el documento de MongoDB.

---

# Colección: Pedidos

### Estructura

* _id (ObjectId automático)
* codigo_pedido
* cliente_rut
* productos[]

  * codigo_producto
  * nombre
  * precio
  * cantidad
* total
* estado
* fecha_pedido

### Reglas de negocio

* [ ] codigo_pedido debe ser único.
* [ ] El código se genera automáticamente mediante la colección **contadores**.
* [ ] El cliente debe existir.
* [ ] Cada producto debe existir.
* [ ] El stock debe ser suficiente.
* [ ] El total debe calcularse automáticamente.
* [ ] Descontar stock al crear un pedido.
* [ ] No permitir cantidades menores o iguales a 0.

### Estados permitidos

* Pendiente
* Procesando
* Entregado
* Cancelado

---

# Colección: Contadores

Objetivo:

Generar códigos incrementales sin depender del ObjectId.

Ejemplo:

Productos

P0001

P0002

P0003

Pedidos

PED0001

PED0002

PED0003

Cada vez que se cree un registro nuevo, el contador correspondiente deberá incrementarse automáticamente.

---

# Validaciones pendientes

## Clientes

* [ ] RUT
* [ ] Nombre
* [ ] Correo
* [ ] Teléfono
* [ ] Dirección
* [ ] Estado

## Productos

* [ ] Código automático
* [ ] Nombre
* [ ] Categoría
* [ ] Precio
* [ ] Stock
* [ ] Proveedor
* [ ] Estado

## Pedidos

* [ ] Cliente existente
* [ ] Productos existentes
* [ ] Cantidad válida
* [ ] Stock suficiente
* [ ] Total automático
* [ ] Estado

---

# Servicios a implementar

## ServicioCliente

* [ ] Agregar
* [ ] Buscar por RUT
* [ ] Actualizar
* [ ] Eliminar
* [ ] Listar

## ServicioProducto

* [ ] Generar código
* [ ] Agregar
* [ ] Buscar por código
* [ ] Buscar por nombre
* [ ] Actualizar
* [ ] Eliminar
* [ ] Listar

## ServicioPedido

* [ ] Generar código
* [ ] Crear pedido
* [ ] Buscar por código
* [ ] Actualizar estado
* [ ] Cancelar pedido
* [ ] Listar

---

# Flujo esperado del sistema

Crear cliente

↓

Crear productos

↓

Generar código automático

↓

Registrar pedido

↓

Validar cliente

↓

Validar productos

↓

Validar stock

↓

Calcular total

↓

Guardar pedido

↓

Actualizar stock

---

# Objetivo del proyecto

Mantener toda la lógica centralizada y reutilizable, evitando duplicar código entre el menú, los modelos y los servicios. El menú solo solicitará información al usuario y mostrará resultados; las validaciones y reglas de negocio se implementarán en los servicios correspondientes.
