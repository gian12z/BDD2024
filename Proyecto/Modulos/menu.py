from productos import agregarProducto, modificarProducto, eliminarProducto, listarProductos, agregarStock, productosMenosVendidos, productosStockBajo, productosStockAlto
from conexionBaseDeDatos import conectarBaseDeDatos
from clientes import registrar_cliente, actualizar_cliente, ver_clientes

#Mostrar el menu de productos
def menuProductos():
    while True:
        print("\n \n -[Menú Productos]-")
        print("[1] Agregar producto.")
        print("[2] Modificar producto.")
        print("[3] Eliminar producto.")
        print("[4] Listar productos.")
        print("[5] Agregar stock de un producto.")
        print("[6] Mostrar productos menos vendidos.")
        print("[7] Mostrar productos con stock menor a 20.")
        print("[8] Mostrar productos con stock mayor a 20.")
        print("[9] Regresar al menú principal.")
        opcion = input("Seleccione la operación que quiera realizar: (Utilizar los numeros de índice)")

        if opcion == "1":
            agregarProducto()
        elif opcion == "2":
            modificarProducto()
        elif opcion == "3":
            eliminarProducto()
        elif opcion == "4":
            listarProductos()
        elif opcion == "5":
            agregarStock()
        elif opcion == "6":
            productosMenosVendidos()
        elif opcion == "7":
            productosStockBajo()
        elif opcion == "8":
            productosStockAlto()
        elif opcion == "9":
            print("Regresando al menú principal.")
            break
        else:
            print("La opción seleccionada no existe. Intente de nuevo.")
            
def menuClientes():
    while True:
        print("\n \n -[Menú Clientes]-")
        print("[1] Agregar cliente.")
        print("[2] Modificar cliente.")
        print("[3] Listar clientes.")
        print("[4] Regresar al menú principal.")
        opcion = input("Seleccione la operación que quiera realizar: (Utilizar los numeros de índice)")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            actualizar_cliente()
        elif opcion == "3":
            ver_clientes()
        elif opcion == "4":
            print("Regresando al menú principal.")
            break
        else:
            print("La opción seleccionada no existe. Intente de nuevo.")

#Mostrar las ordenes pedidas por un cliente dado
def MostrarOrdenes():
    conexion = conectarBaseDeDatos()

    if conexion:
        try:
            cursor = conexion.cursor()
            id_cliente = int(input("Ingrese el ID del cliente para ver sus ordenes: "))
            cursor.execute("SELECT * FROM ordenes WHERE id_cliente = %s", (id_cliente, ))
            ordenes = cursor.fetchall()

            for orden in ordenes:
                print(orden)
        except Exception as e:
            print(f"Error listando los productos: {e}")

        finally:
            conexion.close()

#Mostrar el producto mas vendido
def reporteProductoMasVendido():
    conexion = conectarBaseDeDatos()

    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id_producto, SUM(cantidad) AS total FROM ordenes GROUP BY id_producto ORDER BY total DESC LIMIT 1")
            producto_mas_vendido = cursor.fetchone()
            print(f"El producto más vendido es el ID {producto_mas_vendido[0]} con un total de {producto_mas_vendido[1]} unidades vendidas.")
        except Exception as e:
            print(f"Error listando los productos: {e}")

        finally:
            conexion.close()

def menuPrincipal():
    while True:
        print("\n \n -[Menú Principal]-")
        print("[1] Menú de productos.")
        print("[2] Menú de clientes.")
        print("[3] Mostrar las ordenes de un cliente específico.")
        print("[4] Reporte producto mas vendido.")
        print("[5] Salir del sistema.")
        opcion = input("Seleccione la operación que quiera realizar: (Utilizar los numeros de índice)")

        if opcion == "1":
            menuProductos()
        elif opcion == "2":
            menuClientes()
        elif opcion == "3":
            MostrarOrdenes()
        elif opcion == "4":
            reporteProductoMasVendido()
        elif opcion == "5":
            print("Saliendo del sistema.")
            break
        else:
            print("La opción seleccionada no existe. Intente de nuevo.")

if __name__ == "__main__":
    menuPrincipal()