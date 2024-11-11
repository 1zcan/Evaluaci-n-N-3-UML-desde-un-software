import mysql.connector
from models.db import conectar
from models.clientes import clientes

def crear_cliente(nombre, apellido, telefono, id_comuna, nombre_comuna):
    #Función para crear un cliente.
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO clientes (nombre, apellido, telefono, id_comuna, nombre_comuna) VALUES (%s, %s, %s, %s, %s, %s)",
            (nombre, apellido, telefono, id_comuna, nombre_comuna)
        )
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def obtener_clientes():
    # Función para obtener todos los clientes.
    conn = conectar()
    if conn is None:
        return []
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        return [cliente for cliente in clientes]
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        cursor.close()
        conn.close()


def buscar_cliente_por_id(id):
    #Función para buscar un cliente por nombre.
    conn = conectar()
    if conn is None:
        return None
    cursor = conn.cursor()
    try:
        cursor.execute( """
        SELECT c.run, c.nombre, c.apellido, c.telefono, c.id_comuna, c.nombre_comuna
        FROM cliente AS c
        JOIN comuna AS com 
        ON c.id_comuna_fk = c.id_comuna
        WHERE c.run LIKE %s OR c.nombre LIKE %s OR c.apellido LIKE %s
        """)
        cliente = cursor.fetchone()
        if cliente:
            return clientes(*cliente)
        return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        conn.close()

def actualizar_cliente(id, nuevo_nombre, apellido, telefono, id_comuna, nombre_comuna):
    #Función para actualizar un cliente.
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE clientes SET nombre = %s, apellido = %s, telefono = %s, id_comuna = %s, nombre_comuna = %s = %s WHERE id = %s",
            (nuevo_nombre, apellido, telefono, id_comuna, nombre_comuna, id)
        )
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def eliminar_cliente(id):
    #Función para eliminar un cliente.
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
