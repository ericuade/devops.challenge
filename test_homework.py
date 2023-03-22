from homework import *
import unittest


class TestingMethods(unittest.TestCase):
  def test_suma(self):
    self.assertEqual(suma(1, 2), 3, "La suma NO funciono")
  def test_resta(self):
    self.assertEqual(resta(2, 1), 1, "La resta NO es correcta")
  def test_multiplica(self):
    self.assertEqual(multiplica(1, 2), 2, "La multiplicacion NO es correcta")
  def test_divide(self):
    self.assertEqual(divide(4, 2), 2, "La division NO es correcta")

if __name__ == "__main__":  
    unittest.main()
      