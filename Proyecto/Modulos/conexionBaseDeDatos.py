import mysql.connector

def conectarBaseDeDatos():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root", #El usuario debe ser modificado por el usuario de la base de datos
            password="password", #La contraseña debe ser modificada por la contraseña de la base de datos
            database="basededatos" #La base de datos debe llevar el nombre usado en MySQL Workbench
        )
    except mysql.connector.Error as e:
        print(f"Error conectando a la base de datos: {e}")
        return None
