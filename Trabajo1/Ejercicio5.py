import math # Importamos esta librería para poder usar el valor exacto de Pi (math.pi)

class Circulo:
    # Constructor: un círculo se define principalmente por su radio
    def __init__(self, radio):
        self.radio = radio

    def calcular_propiedades(self):
        # Aplicamos la fórmula del área (Pi por radio al cuadrado)
        area = math.pi * (self.radio ** 2)
        
        # Aplicamos la fórmula de la circunferencia (2 por Pi por radio)
        circunferencia = 2 * math.pi * self.radio
        
        print("--- Propiedades del Círculo ---")
        print(f"Radio ingresado: {self.radio}")
        # Usamos :.2f para redondear el resultado a solo 2 decimales y que se vea más limpio
        print(f"El área del círculo es: {area:.2f}") 
        print(f"La longitud de la circunferencia es: {circunferencia:.2f}")
