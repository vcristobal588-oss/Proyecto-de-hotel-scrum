import mysql.connector

CONFIG_DB = {
    "host": "localhost",
    "user": "root",
    "password": "",  # XAMPP por defecto
    "database": "hotel_duerme_bien",
}


def obtener_conexion():
    """Devuelve una conexión nueva a MySQL. Quien la pida debe cerrarla."""
    return mysql.connector.connect(**CONFIG_DB)