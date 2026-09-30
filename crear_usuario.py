import getpass

import mysql.connector

from authentication.auth import hashear_password
from database import obtener_conexion


def crear_usuario():
    nombre = input("Nombre: ").strip()
    email = input("Correo: ").strip()
    rol = input("Rol (administrador/encargado): ").strip().lower()
    password = getpass.getpass("Contraseña: ")

    if rol not in ("administrador", "encargado"):
        print("Rol inválido.")
        return

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nombre, email, password, rol) VALUES (%s, %s, %s, %s)",
            (nombre, email, hashear_password(password), rol),
        )
        conexion.commit()
        print("Usuario creado correctamente.")
        cursor.close()
        conexion.close()
    except mysql.connector.Error as error:
        print(f"Error en la base de datos: {error}")


if __name__ == "__main__":
    crear_usuario()