class Familia:    
    def __init__(self, edad_juan):
        self.edad_juan = edad_juan

    # Este método realiza los cálculos usando los datos del objeto (self)
    def calcular_edades(self):
        # Alberto tiene 2/3 de la edad de Juan
        edad_alberto = (2 / 3) * self.edad_juan 
        
        # Ana tiene 4/3 de la edad de Juan
        edad_ana = (4 / 3) * self.edad_juan

        # La mamá es la suma de los tres
        edad_mama = self.edad_juan + edad_alberto + edad_ana 
        print("--- Edades de la Familia ---")
        print(f"Edad de Juan: {self.edad_juan}")
        print(f"Edad de Alberto: {edad_alberto}")
        print(f"Edad de Ana: {edad_ana}")
        print(f"Edad de la mamá: {edad_mama}")
