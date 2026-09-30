from datetime import datetime

class Pasajero:
    def __init__(self, rut: str, nombre: str):
        self.rut = rut
        self.nombre = nombre

class Habitacion:
    def __init__(self, numero: str, capacidad: int):
        self.numero = numero
        self.capacidad = capacidad
        self.ocupada = False
        self.activa = True

class Reserva:
    def __init__(self, id_reserva: int, responsable: Pasajero, alojado_responsable: bool):
        self.id_reserva = id_reserva
        self.responsable = responsable
        self.alojado_responsable = alojado_responsable
        self.pasajeros_alojados = []
        self.habitaciones_asignadas = []
        self.fecha_checkin = None
        self.fecha_checkout = None
        self.costo_total = 0.0

    def calcular_costo(self):
        # Multiplica $20.000 solo por pasajeros efectivamente alojados
        self.costo_total = len(self.pasajeros_alojados) * 20000.0
        return self.costo_total
