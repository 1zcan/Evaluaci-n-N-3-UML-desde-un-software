import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        print("Intentando conectar a la base de datos...")
        conn = mysql.connector.connect(
            host='localhost',
            database='pyjoin',
            user='root',
            password=''
        )
        print("Conexión exitosa!")
        return conn
    except Error as e:
        print(f"Error al conectar a MariaDB: {e}")
        return None

def crear_tablas():
    conn = conectar()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        print("Creando tablas...")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                run INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                apellido VARCHAR(50),
                telefono VARCHAR(20),
                id_comuna int(500),
                nombre_comuna VARCHAR(50),
                FOREIGN KEY (id_comuna) REFERENCES comunas(id) ON DELETE SET NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS comunas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
            )
        ''')

        conn.commit()
        print("Tablas creadas exitosamente!")
    except Error as e:
        print(f"Error al crear tablas: {e}")
    finally:
        cursor.close()
        conn.close()

crear_tablas()

