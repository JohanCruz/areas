import unittest

# Función principal que calcula el área de un rectángulo    
"""
   Elaborar la función area_rectangulo 
"""
def area_rectangulo(base, altura):
    # Espacio por hacer, borre la siguiente línea
    pass


# Clase de prueba para la función calcular_area
class TestCalcularArea(unittest.TestCase):
    # Prueba para asegurarnos de que se calcule correctamente el área de un triángulo con números enteros
    def test_area_enteros(self):
        self.assertEqual(area_rectangulo(5, 10), 50)

    # Prueba para asegurarnos de que se calcule correctamente el área de un triángulo con números decimales
    def test_area_decimales(self):
        self.assertAlmostEqual(area_rectangulo(3.5, 7.2), 25.2, delta=0.01)

    # Prueba para asegurarnos de que la función levante un ValueError si se ingresan números negativos
    def test_numeros_negativos(self):
        with self.assertRaises(ValueError):
            area_rectangulo(-5, 10)

    # Prueba para asegurarnos de que la función levante un ValueError si se ingresan cero como parámetros
    def test_numeros_cero(self):
        with self.assertRaises(ValueError):
            area_rectangulo(0, 10)

    # Prueba para asegurarnos de que la función levante un ValueError si se ingresan cadenas como parámetros
    def test_cadenas(self):
        with self.assertRaises(TypeError):
            area_rectangulo("base", "altura")

# Función secundaria que llama a la función principal y ejecuta las pruebas unitarias
def ejecutar_pruebas():
    # Crear una instancia de la clase TestCalcularArea
    test = TestCalcularArea()

    # Ejecutar las pruebas unitarias
    unittest.main(argv=[''], exit=False)
    

# Llamar a la función secundaria
ejecutar_pruebas()

