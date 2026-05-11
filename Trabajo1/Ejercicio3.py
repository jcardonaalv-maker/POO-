class Empleado:
    def __init__(self, horas_trabajadas, valor_hora):
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = 0.125 # 12.5% expresado en decimal

    def calcular_nomina(self):
        # 1. Salario Bruto
        salario_bruto = self.horas_trabajadas * self.valor_hora
        
        # 2. Retención en la fuente
        retencion = salario_bruto * self.porcentaje_retencion
        
        # 3. Salario Neto
        salario_neto = salario_bruto - retencion

        print("--- Nómina del Empleado ---")
        print(f"Salario Bruto: ${salario_bruto}")
        print(f"Retención en la fuente: ${retencion}")
        print(f"Salario Neto: ${salario_neto}")

