import unittest
from calculadora import somar

class TestCalculadora(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(somar(5,3),8)