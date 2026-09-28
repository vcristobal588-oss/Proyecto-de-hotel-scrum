import mysql.connector

def iniciar_sesion():
    print("--- HOTEL DUERME BIEN: SISTEMA DE LOGIN ---")
    email_ingresado = input("Ingresa tu correo: ")
    password_ingresada = input("Ingresa tu contraseña: ")

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",          
            password="",          
            database="hotel_duerme_bien"
        )
        
        cursor = conexion.cursor(dictionary=True)

        consulta = "SELECT * FROM usuarios WHERE email = %s"
        cursor.execute(consulta, (email_ingresado,))
        usuario = cursor.fetchone()

        if usuario:
            if usuario['password'] == password_ingresada:
                print(f"\n¡Bienvenido/a, {usuario['nombre']}!")
                
                if usuario['rol'] == 'administrador':
                    print("-> Acceso concedido: Perfil de ADMINISTRADOR (Control total del sistema).")
                elif usuario['rol'] == 'encargado':
                    print("-> Acceso concedido: Perfil de ENCARGADO (Gestión de habitaciones y check-in).")
            else:
                print("\nError: Contraseña incorrecta.")
        else:
            print("\nError: El correo no está registrado en el sistema.")

        cursor.close()
        conexion.close()

    except mysql.connector.Error as error:
        print(f"Error al conectar con la base de datos: {error}")

if __name__ == "__main__":
    iniciar_sesion()