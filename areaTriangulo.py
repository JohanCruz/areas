"""
En este ejemplo, la función principal  calcular_area()  calcula el área de un triángulo y utiliza 
una estructura condicional para asegurarse de que los parámetros sean números positivos. La clase  
TestCalcularArea  contiene cinco pruebas unitarias que verifican que la función  calcular_area()  
funcione correctamente en diferentes situaciones. La función secundaria  ejecutar_pruebas()  
crea una instancia de la clase  TestCalcularArea  y ejecuta las pruebas unitarias utilizando 
la biblioteca unittest. 
 
esto facilita entender cómo crear una función en Python y cómo utilizar la
biblioteca de pruebas unitarias unittest.

"""


import unittest

# Función principal que calcula el área de un triángulo
def calcular_area(base, altura):
    # estructura condicional para asegurarnos de que los parámetros sean números positivos
    if base <= 0 or altura <= 0:
        #si son negativos o cero levanta el error
        raise ValueError("La base y la altura deben ser números positivos")

    # Calcular el área del triángulo
    area = (base * altura) / 2

    # Devolver el resultado
    return area
    

# Clase de prueba para la función calcular_area
class TestCalcularArea(unittest.TestCase):
    # Prueba para asegurarnos de que se calcule correctamente el área de un triángulo con números enteros
    def test_area_enteros(self):
        self.assertEqual(calcular_area(5, 10), 25)

    # Prueba para asegurarnos de que se calcule correctamente el área de un triángulo con números decimales
    def test_area_decimales(self):
        self.assertAlmostEqual(calcular_area(3.5, 7.2), 12.6, delta=0.01)

    # Prueba para asegurarnos de que la función levante un ValueError si se ingresan números negativos
    def test_numeros_negativos(self):
        with self.assertRaises(ValueError):
            calcular_area(-5, 10)

    # Prueba para asegurarnos de que la función levante un ValueError si se ingresan cero como parámetros
    def test_numeros_cero(self):
        with self.assertRaises(ValueError):
            calcular_area(0, 10)

    # Prueba para asegurarnos de que la función levante un ValueError si se ingresan cadenas como parámetros
    def test_cadenas(self):
        with self.assertRaises(TypeError):
            calcular_area("base", "altura")

# Función secundaria que llama a la función principal y ejecuta las pruebas unitarias
def ejecutar_pruebas():
    # Crear una instancia de la clase TestCalcularArea
    test = TestCalcularArea()

    # Ejecutar las pruebas unitarias
    unittest.main(argv=[''], exit=False)
    

# Llamar a la función secundaria
ejecutar_pruebas()

