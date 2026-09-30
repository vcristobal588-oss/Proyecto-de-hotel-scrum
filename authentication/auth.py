import getpass

import bcrypt
import mysql.connector

from database import obtener_conexion


def hashear_password(password: str) -> str:
    """Genera el hash bcrypt (con salt incluido) listo para guardar en la BD."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verificar_password(password: str, hash_guardado: str) -> bool:
    """Compara la contraseña ingresada contra el hash almacenado."""
    try:
        return bcrypt.checkpw(password.encode("utf-8"), hash_guardado.encode("utf-8"))
    except ValueError:
        # El valor guardado no es un hash bcrypt válido (p. ej. texto plano antiguo)
        return False


def iniciar_sesion():
    print("\n--- INICIO DE SESIÓN: HOTEL DUERME BIEN ---")
    email = input("Ingrese su correo electrónico: ").strip()
    password = getpass.getpass("Ingrese su contraseña: ")

    conexion = None
    cursor = None
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        usuario = cursor.fetchone()

        # Mensaje único para no revelar si el correo existe o no
        if usuario and verificar_password(password, usuario["password"]):
            print(f"\n¡Bienvenido, {usuario['nombre']}!")
            print(f"Rol asignado en el sistema: {usuario['rol'].upper()}")
            return usuario

        print("\nError: Correo o contraseña incorrectos.")

    except mysql.connector.Error as error:
        print(f"\nError de conexión a la base de datos: {error}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

    return None


if __name__ == "__main__":
    iniciar_sesion()