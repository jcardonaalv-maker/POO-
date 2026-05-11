class PruebaEscritorio:
    def __init__(self):
        # Inicializamos las variables que menciona el problema
        self.suma = 0
        self.x = 0
        self.y = 0

    def ejecutar_instrucciones(self):
        # Seguimos el pseudocódigo línea por línea
        self.suma = 0
        self.x = 20
        self.suma = self.suma + self.x
        self.y = 40
        
        # El operador ** significa "elevado a" (potencia)
        self.x = self.x + (self.y ** 2) 
        
        self.suma = self.suma + (self.x / self.y)
        
        print("EL VALOR DE LA SUMA ES:", self.suma)
