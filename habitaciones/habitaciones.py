import mysql.connector

from database import obtener_conexion


def registrar_habitacion():
    print("\n--- REGISTRAR NUEVA HABITACIÓN ---")
    try:
        numero = int(input("Ingrese el número de la habitación: "))
        capacidad = int(input("Ingrese la capacidad (pasajeros admitidos): "))
        orientacion = input("Ingrese la orientación (ej. Vista al mar, Poniente): ").strip()
    except ValueError:
        print("\nError: Ingrese valores numéricos válidos para el número y la capacidad.")
        return

    conexion = None
    cursor = None
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            """
            INSERT INTO habitaciones (numero_habitacion, capacidad, orientacion, estado)
            VALUES (%s, %s, %s, 'disponible')
            """,
            (numero, capacidad, orientacion),
        )
        conexion.commit()
        print(f"\n¡Éxito! Habitación número {numero} registrada correctamente como 'disponible'.")
    except mysql.connector.Error as error:
        print(f"\nError en la base de datos: {error}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()


def listar_habitaciones():
    print("\n--- LISTADO DE HABITACIONES REGISTRADAS ---")
    conexion = None
    cursor = None
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, numero_habitacion, capacidad, orientacion, estado FROM habitaciones"
        )
        resultados = cursor.fetchall()

        if not resultados:
            print("No hay habitaciones registradas en el sistema.")
            return

        print(f"{'ID':<5} | {'NÚMERO':<8} | {'CAPACIDAD':<10} | {'ORIENTACIÓN':<18} | {'ESTADO':<12}")
        print("-" * 65)
        for id_, numero, capacidad, orientacion, estado in resultados:
            print(f"{id_:<5} | {numero:<8} | {capacidad:<10} | {orientacion or '-':<18} | {estado:<12}")
    except mysql.connector.Error as error:
        print(f"\nError al consultar la base de datos: {error}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()


def menu():
    while True:
        print("\n=== HOTEL DUERME BIEN: GESTIÓN DE HABITACIONES ===")
        print("1. Registrar habitación")
        print("2. Listar habitaciones")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == "1":
            registrar_habitacion()
        elif opcion == "2":
            listar_habitaciones()
        elif opcion == "3":
            print("\nSaliendo del sistema de gestión. ¡Hasta luego!")
            break
        else:
            print("\nOpción inválida. Por favor, elija entre 1 y 3.")


if __name__ == "__main__":
    menu()