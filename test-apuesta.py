import unittest
from apuesta import Apuesta 

class TestApuesta(unittest.Testcase):
    def test_ponerFicha_agrega_correctamente(self)
        apuesta = Apuesta ()
        apuesta.ponerFicha(3)
        self.assertEqual(apuesta.fichas,3)

        def test_tomarFicha_quitar_correctamente(self):
            apuesta = Apuesta ()
            apuesta = ponerFicha(5)
            apuesta = tomarFicha(3)
            self.assertEqual(apuesta.fichas,2)