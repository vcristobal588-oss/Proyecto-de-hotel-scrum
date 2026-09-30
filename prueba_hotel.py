import unittest
from hotel_system import SistemaHotel
from models import Pasajero

class TestMetodologiaAgil(unittest.TestCase):

    def test_checkin_responsable_no_alojado(self):
        hotel = SistemaHotel()
        hotel.registrar_habitacion("101", 2)
        
        resp = Pasajero("1-9", "Juan Pérez")
        p1 = Pasajero("2-7", "Ana Soto")
        p2 = Pasajero("3-5", "Pedro Soto")

        # Responsable NO alojado, 2 acompañantes alojados
        reserva = hotel.realizar_checkin(resp, False, [p1, p2], ["101"])

        # Valida que el costo sea $40.000 (2 x $20.000)
        self.assertEqual(reserva.costo_total, 40000.0)
        self.assertTrue(hotel.habitaciones["101"].ocupada)

if __name__ == "__main__":
    unittest.main()
