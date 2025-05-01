import mariadb

def conectar_y_consultar():
    try:
        # Establecer conexion a la base de datos
        conexion = mariadb.connect(
            host="localhost",
            database="almacen",
            user="root",
            password="",
            port=3306 # Puerto predeterminado de MariaDB
        )
        print(type(conexion))
        print("Conexion a la base de datos del servidor Ounus")

        #Crear un cursor y ejecutar la consulta
        cursor = conexion.cursor()
        consulta = "select * from usuarios"
        cursor.execute(consulta)

        # Recuperar y mostrar resultados
        resultados = cursor.fetchall()
        print("Resultado ", type(resultados))
        print("Datos en la tabla:")
        for fila in resultados:
            # Cerrar la conexion y el cursor si estan abiertos
            print(f"ID: {fila[0]}, Nombre de Usuario: {fila[1]}, Correo: {fila[2]}, Contraseña: {fila[3]}, Id_rol: {fila[4]}")

    except mariadb.Error as e:
        print(f"Error al conectar con la base de datos: {e}")

    finally:
        if 'cursor' in locals()  and cursor:
            cursor.close()
            print("Conexion cerrada.")
if __name__ == '__main__':
    conectar_y_consultar()