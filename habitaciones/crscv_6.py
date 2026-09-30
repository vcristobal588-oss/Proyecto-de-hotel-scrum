from database import obtener_conexion


def registrar_habitacion():
    print("\n--- REGISTRAR NUEVA HABITACIÓN ---")
    try:
        numero = int(input("Ingrese el número de la habitación: "))
        capacidad = int(input("Ingrese la capacidad (pasajeros admitidos): "))
        orientacion = input("Ingrese la orientación (ej. Vista al mar, Poniente): ").strip()
    except ValueError:
        print("\nError: Ingrese valores numéricos válidos.")
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
        print(f"\n¡Éxito! Habitación {numero} registrada como 'disponible'.")
    except Exception as error:
        print(f"\nError: {error}")
    finally:
        if cursor: cursor.close()
        if conexion: conexion.close()