from conexionBaseDeDatos import conectarBaseDeDatos

#Registrar un cliente
def registrar_cliente():
    conexion = conectarBaseDeDatos()
    
    if conexion:
        try:
            cursor = conexion.cursor()
            nombre = input("Ingrese el nombre del cliente: ")
            email = input("Ingrese el email del cliente: ")
            numero = input("Ingrese el numero del cliente: ")
            direccion = input("Ingrese la direccion del cliente: ")
            cursor.execute("""
                INSERT INTO clientes (nombre, email, telefono, direccion) VALUES (%s, %s, %s, %s)
            """, (nombre, email, numero, direccion))
            
            conexion.commit()
            print("Cliente agregado con éxito.")
        except Exception as e:
            print(f"Error agregando el cliente: {e}")
        
        finally:
            conexion.close()
#Actualizar cliente
def actualizar_cliente():
    conexion = conectarBaseDeDatos()
    
    if conexion:
        try:
            cursor = conexion.cursor()
            id_cliente = int(input("Ingrese el ID del cliente a modificar: "))
            nombre = input("Ingrese el nuevo nombre del cliente: ")
            email = input("Ingrese el nuevo email del cliente: ")
            numero = input("Ingrese el nuevo numero del cliente: ")
            direccion = input("Ingrese la nueva direccion del cliente: ")
            
            cursor.execute("""
                UPDATE clientes SET nombre = %s, email = %s, telefono = %s, direccion = %s WHERE id_cliente = %s
            """, (nombre, email, numero, direccion, id_cliente))
            
            conexion.commit()
            print("Cliente modificado con éxito.")
        except Exception as e:
            print(f"Error modificando el cliente: {e}")
        
        finally:
            conexion.close()

#Mostrar la lista de todos los clientes
def ver_clientes():
    conexion = conectarBaseDeDatos()
    
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM clientes")
            clientes = cursor.fetchall()

            print("\n--- Lista de Clientes ---")
            if not clientes:
                print("No hay clientes registrados.")
                return
            for cliente in clientes:
                print(cliente)
        except Exception as e:
            print(f"Error mostrando los clientes: {e}")
        
        finally:
            conexion.close()