from datetime import datetime
from models import Pasajero, Habitacion, Reserva

class SistemaHotel:
    def __init__(self):
        self.habitaciones = {}
        self.reservas = {}
        self.contador_reservas = 1

    def registrar_habitacion(self, numero: str, capacidad: int):
        hab = Habitacion(numero, capacidad)
        self.habitaciones[numero] = hab
        return hab

    def realizar_checkin(self, responsable: Pasajero, alojado_responsable: bool, 
                         acompañantes: list, numeros_habitaciones: list):
        alojados = list(acompañantes)
        if alojado_responsable:
            alojados.append(responsable)

        if len(alojados) == 0:
            raise ValueError("Error: Debe existir al menos un pasajero alojado.")

        capacidad_total = 0
        habs_a_ocupar = []
        for num in numeros_habitaciones:
            hab = self.habitaciones[num]
            if hab.ocupada:
                raise ValueError(f"Habitación {num} ya está ocupada.")
            capacidad_total += hab.capacidad
            habs_a_ocupar.append(hab)

        if capacidad_total < len(alojados):
            raise ValueError("Capacidad insuficiente en las habitaciones seleccionadas.")

        reserva = Reserva(self.contador_reservas, responsable, alojado_responsable)
        self.contador_reservas += 1
        reserva.pasajeros_alojados = alojados
        reserva.habitaciones_asignadas = habs_a_ocupar
        reserva.fecha_checkin = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        reserva.calcular_costo()

        for hab in habs_a_ocupar:
            hab.ocupada = True

        self.reservas[reserva.id_reserva] = reserva
        return reserva

    def realizar_checkout(self, id_reserva: int):
        reserva = self.reservas[id_reserva]
        reserva.fecha_checkout = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for hab in reserva.habitaciones_asignadas:
            hab.ocupada = False
        return reserva
