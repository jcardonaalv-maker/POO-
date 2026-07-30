class Numero:
    # Constructor: aquí guardamos el número que el usuario quiere calcular
    def __init__(self, valor):
        self.valor = valor

    # Método para hacer los cálculos matemáticos
    def mostrar_potencias(self):
        # En Python, el doble asterisco (**) se usa para calcular potencias
        cuadrado = self.valor ** 2
        cubo = self.valor ** 3
        
        print("--- Cálculos del Número ---")
        print(f"Número original: {self.valor}")
        print(f"El cuadrado de {self.valor} es: {cuadrado}")
        print(f"El cubo de {self.valor} es: {cubo}")
