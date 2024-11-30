## **Proyecto Final: Proyecto 2**

### Primera forma normal (1NF)
- `productos`: Cada producto tiene su identificador único id_producto, y nombre, categoria, precio y stock contienen valores únicos.
- `clientes`: Cada cliente tiene su identificador unico id_cliente y nombre, email, telefono y dirección contienen valores únicos.
- `ordenes`: Cada orden tiene su identificador único id_orden y id_cliente, id_producto, fecha y cantidad contienen valores únicos.

### Segunda forma normal (2NF)

Cumple con la primera forma normal

- `productos`: La clave primaria id_producto determina de manera unica las columnas `id_producto`, `nombre`, `categoria`, `precio`, `stock`. No existen dependencias parciales.
- `clientes`: La clave primaria id_cliente determina de manera unica las columnas `id_cliente`, `nombre`, `email`, `telefono`, `direccion`. No existen dependencias parciales.
- `ordenes`: La clave primaria id_orden determina de manera unica las columnas `fecha`, `cantidad`, `id_cliente`, `id_producto`. No existen dependencias parciales. Aunque `id_cliente` e `id_producto` se repitan el `id_orden` los diferencia.

### Segunda forma normal (3NF)

Cumple con la segunda forma normal.

Se crearon 3 tablas (`productos`, `clientes`, `ordenes`) para eliminar dependencias transitivas y garantizar que cada atributo no clave dependa únicamente de la clave primaria completa.

1. **Tabla `productos`**
   - `id_producto` (Clave primaria)
   - `nombre`
   - `categoria`
   - `precio`
   - `stock`

2. **Tabla `clientes`**
   - `id_producto` (Clave primaria)
   - `nombre`
   - `email`
   - `telefono`
   - `direccion`

3. **Tabla `ordenes`**
   - `id_orden` (Clave primaria)
   - `id_cliente` (Clave foránea que referencia a `clientes`)
   - `id_producto` (Clave foránea que referencia a `productos`)
   - `fecha`
   - `cantidad`
