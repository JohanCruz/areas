import unittest

# Función principal que calcula el área de un cuadrado    
"""
   Elaborar la funcion area_cuadrado 
"""
def area_cuadrado(lado):
    pass

# Clase de prueba para la función calcular_area
class TestCalcularArea(unittest.TestCase):
    # Prueba para asegurarnos de que se calcule correctamente el área de un triángulo con números enteros
    def test_area_enteros(self):
        self.assertEqual(area_cuadrado(5), 25)

    # Prueba para asegurarnos de que se calcule correctamente el área de un triángulo con números decimales
    def test_area_decimales(self):
        self.assertAlmostEqual(area_cuadrado(3.5), 12.25, delta=0.01)

    # Prueba para asegurarnos de que la función levante un ValueError si se ingresan números negativos
    def test_numeros_negativos(self):
        with self.assertRaises(ValueError):
            area_cuadrado(-5)

    # Prueba para asegurarnos de que la función levante un ValueError si se ingresan cero como parámetros
    def test_numeros_cero(self):
        with self.assertRaises(ValueError):
            area_cuadrado(0)

    # Prueba para asegurarnos de que la función levante un ValueError si se ingresan cadenas como parámetros
    def test_cadenas(self):
        with self.assertRaises(TypeError):
            area_cuadrado("lado")

# Función secundaria que llama a la función principal y ejecuta las pruebas unitarias
def ejecutar_pruebas():
    # Crear una instancia de la clase TestCalcularArea
    test = TestCalcularArea()

    # Ejecutar las pruebas unitarias
    unittest.main(argv=[''], exit=False)
    

# Llamar a la función secundaria
ejecutar_pruebas()

