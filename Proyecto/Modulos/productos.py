from conexionBaseDeDatos import conectarBaseDeDatos

#Agregar un producto a la base de datos
def agregarProducto():
    conexion = conectarBaseDeDatos()
    
    if conexion:
        try:
            cursor = conexion.cursor()
            nombre = input("Ingrese el nombre del producto: ")
            categoria = input("Ingrese la categoria del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad de producto: "))
            cursor.execute("""
                INSERT INTO Productos (nombre, categoria, precio, stock) VALUES (%s, %s, %s, %s)
            """, (nombre, categoria, precio, cantidad))
            
            conexion.commit()
            print("Producto agregado con éxito.")
        except Exception as e:
            print(f"Error agregando el producto: {e}")
        
        finally:
            conexion.close()
           
#Modificar un producto en la base de datos            
def modificarProducto():
    conexion = conectarBaseDeDatos()
    
    if conexion:
        try:
            cursor = conexion.cursor()
            id_producto = int(input("Ingrese el ID del producto a modificar: "))
            nombre = input("Ingrese el nuevo nombre del producto: ")
            categoria = input("Ingrese la nueva categoria del producto: ")
            precio = float(input("Ingrese el nuevo precio del producto: "))
            cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            
            cursor.execute("""
                UPDATE Productos SET nombre = %s, categoria = %s, precio = %s, stock = %s WHERE id_producto = %s
            """, (nombre, categoria, precio, cantidad, id_producto))
            
            conexion.commit()
            print("Producto modificado con éxito.")
        except Exception as e:
            print(f"Error modificando el producto: {e}")
        
        finally:
            conexion.close()
            
#Eliminar un producto de la base de datos
def eliminarProducto():
    conexion = conectarBaseDeDatos()
    
    if conexion:
        try:
            cursor = conexion.cursor()
            id_producto = int(input("Ingrese el ID del producto a eliminar: "))
            
            cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id_producto,))
            
            conexion.commit()
            print("Producto eliminado con éxito.")
        except Exception as e:
            print(f"Error eliminando el producto: {e}")
        
        finally:
            conexion.close()

#Listar los productos de la base de datos            
def listarProductos():
    conexion = conectarBaseDeDatos()
    
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM productos")
            productos = cursor.fetchall()
            
            for producto in productos:
                print(producto)
        except Exception as e:
            print(f"Error listando los productos: {e}")
        
        finally:
            conexion.close()

#Agregar stock a un producto de la base de datos             
def agregarStock():
    conexion = conectarBaseDeDatos()
    
    if conexion:
        try:
            cursor = conexion.cursor()
            id_producto = int(input("Ingrese el ID del producto al que desea agregar stock: "))
            cantidad = int(input("Ingrese la cantidad de stock a agregar: "))
            
            cursor.execute("""
                UPDATE productos SET stock = stock + %s WHERE id_producto = %s
            """, (cantidad, id_producto))
            
            conexion.commit()
            print("Stock agregado con éxito.")
        except Exception as e:
            print(f"Error agregando stock: {e}")
        
        finally:
            conexion.close()
            
def productosMenosVendidos():
    conexion = conectarBaseDeDatos()
    
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT productos.id_producto, productos.nombre, SUM(ordenes.cantidad) AS cantidad_vendida
                FROM productos
                LEFT JOIN ordenes ON productos.id_producto = ordenes.id_producto
                GROUP BY productos.id_producto
                ORDER BY cantidad_vendida ASC
            """)
            
            productos = cursor.fetchall()
            
            for producto in productos:
                print(producto)
        except Exception as e:
            print(f"Error listando los productos menos vendidos: {e}")
        
        finally:
            conexion.close()

def productosStockBajo():
    conexion = conectarBaseDeDatos()
    
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("""SELECT * FROM productos WHERE productos.stock < 20""")
            productos = cursor.fetchall()
            
            for producto in productos:
                print(producto)
        except Exception as e:
            print(f"Error listando los productos con stock bajo: {e}")
        
        finally:
            conexion.close()

def productosStockAlto():
    conexion = conectarBaseDeDatos()
    
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("""SELECT * FROM productos WHERE productos.stock >= 20""")
            productos = cursor.fetchall()
            
            for producto in productos:
                print(producto)
        except Exception as e:
            print(f"Error listando los productos con stock alto: {e}")
        
        finally:
            conexion.close()