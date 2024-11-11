from controllers.clientes_controller import (
    crear_cliente,
    obtener_clientes,
    actualizar_cliente,
    eliminar_cliente,
    buscar_cliente_por_id,
) 

from controllers.comunas_controller import (
    crear_comuna,
    obtener_comunas,
    actualizar_comuna,
    eliminar_comuna,
    buscar_comuna_por_id,
)

from models.db import (
    crear_tablas,
) 

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


def mostrar_menu():  # Función para mostrar el menú
    crear_tablas()  # Crear las tablas si no existen

    while (
        True
    ):  # Ciclo infinito para mostrar el menú, hasta que el usuario decida salir
        print("\n--- Menú ---")
        print("1. Crear clientes")
        print("2. Crear comuna")
        print("3. Mostrar clientes")
        print("4. Mostrar comunas")
        print("5. Actualizar clientes")
        print("6. Actualizar comuna")
        print("7. Eliminar clientes")
        print("8. Eliminar comuna")
        print("9. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":  # Si la opción es 1, se piden los datos del cliente y se llama a la función crear_cliente
            nombre = input("Nombre del cliente: ")
            apellido = input("apellido del cliente: ")
            telefono = input("Teléfono del cliente: ")
            id_comuna = input("id_comuna del cliente: ")
            nombre_comuna = input("Nombre de la comuna del cliente: ")
            crear_cliente(
                nombre, apellido, telefono, id_comuna, nombre_comuna
            )  # Llamamos a la función crear_cliente

        elif opcion == "2":  # Si la opcion es 2, se pide el nombre y el gerente del comuna y se llama a la funcion crear_comuna
            nombre = input("Nombre del comuna: ")
            gerente = input("id del gerente del comuna: ")
            crear_comuna(nombre, gerente)

        elif opcion == "3":
            Clientes = obtener_clientes()  # llamamos a la funcion obtener_Clientes que se encuentra en el archivo clientes_controller.py
            if Clientes:
                for clientes in Clientes:
                    print(
                        f"nombre: {clientes[1]}, apellido:{clientes[2]}, telefono: {clientes[3]}, id_comuna: {clientes[4]}, trabaja desde: {clientes[5]}, : {clientes[6]}"
                    )
            else:
                print("No hay Clientes registrados.")

        elif opcion == "4":
            comunas = obtener_comunas()  # Llamamos a la función obtener_comunas que se encuentra en el archivo comuna_controller.py
            if comunas:  # Si hay comunas registrados, se recorre la lista de comunas y se imprime el nombre y el gerente de cada uno
                for comuna in comunas:  # Recorremos la lista de comunas
                    print(f"comuna: {comuna['nombre']}, gerente ID: {comuna['gerente_id']}")
            else:
                print("No hay comunas registrados.")

        elif opcion == "5":
          # Si la opcion es 5, se pide el nombre del clientes a actualizar y se llama a la funcion buscar_cliente_por_nombre
            id = input("id del cliente a actualizar: ")
            cliente = buscar_cliente_por_id(id)
            if cliente:  # Si el cliente existe..

                nuevo_nombre = input("Nuevo nombre del cliente: ")
                apellido = input("Nuevo apellido del cliente: ")
                telefono = input("Nuevo teléfono del cliente: ")
                id_comuna = input("Nuevo id_comuna del cliente: ")
                nombre_comuna = input("Nueva fecha de contrato del cliente (YYYY-MM-DD): ")
                actualizar_cliente(id,nuevo_nombre, apellido, telefono, id_comuna, nombre_comuna, )

                print("Cliente actualizado exitosamente.")
            else:
                print("Cliente no encontrado.")


        elif opcion == "6":
            id = input("ID del comuna a actualizar: ")
            comuna = buscar_comuna_por_id(id)
            if comuna:
                nuevo_nombre = input("Nuevo nombre del comuna: ")
                gerente = input("Nuevo ID del gerente del comuna: ")
                actualizar_comuna(id, nuevo_nombre, gerente)
                print("comuna actualizada exitosamente.")
            else:
                print("comuna no encontrada.")


        elif opcion == "7":
            id = input("id del cliente a eliminar: ")
            eliminar_cliente(id)
            print("cliente eliminado exitosamente.")

        elif opcion == "8":
            id = input("id del comuna a eliminar: ")
            eliminar_comuna(id)
            print("comuna eliminado exitosamente.")

        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")
