import mysql.connector
from models.db import conectar
from models.comunas import comunas


def crear_comuna(nombre, gerente_id):
    # Función para crear un comuna
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO comunas (nombre, gerente_id) VALUES (%s, %s)",
            (nombre, gerente_id),
        )
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def obtener_comunas():
    # Función para obtener todos los comunas
    conn = conectar()
    if conn is None:
        return []
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT d.id, d.nombre, e.nombre FROM comunas d JOIN clientes e ON d.id = e.id"
        )
        comunas = cursor.fetchall()
        return [
            {
                "id": id,
                "nombre": nombre,
            }
            for id, nombre in comunas
        ]
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        cursor.close()
        conn.close()



def buscar_comuna_por_id(id):
    # Función para buscar un comuna por id
    conn = conectar()
    if conn is None:
        return None
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT d.id, d.nombre, d.gerente_id, e.nombre FROM comunas d JOIN empleados e ON d.gerente_id = e.id WHERE d.id = %s",
            (id,)
        )
        comuna = cursor.fetchone()
        if comuna:
            id, nombre, gerente_id, gerente_nombre = comuna
            return comunas(
                id,
                nombre,
                gerente_id
            )
        return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        conn.close()



def actualizar_comuna(id, nombre, gerente_id):
    # Función para actualizar un comuna
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE comunas SET nombre = %s, gerente_id = %s WHERE id = %s",
            (nombre, gerente_id, id)
        )
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def eliminar_comuna(id):
    # Función para eliminar un comuna
    conn = conectar()
    if conn is None:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM comunas WHERE id = %s", (id,))
        conn.commit()
        print("comuna eliminado exitosamente.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()