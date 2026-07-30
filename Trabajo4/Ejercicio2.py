class Vendedor:
    """Clase que representa a un vendedor y valida sus reglas de negocio."""

    def __init__(self, nombre, apellidos, edad):
        # 1. Validamos la edad ANTES de asignar los atributos
        self.verificar_edad(edad)
        
        # 2. Si la validación pasa sin lanzar excepciones, construimos el objeto
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def verificar_edad(self, edad):
        """
        Método que evalúa la edad. 
        Utiliza 'raise' (equivalente a 'throw' en Java) para lanzar excepciones.
        """
        # Primera condición: Rango inválido
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120")
        
        # Segunda condición: Minoría de edad
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años")

    def imprimir(self):
        """Muestra por pantalla los valores de los atributos del vendedor."""
        print("\n--- Tarjeta de Presentación del Vendedor ---")
        print(f"Nombre Completo : {self.nombre} {self.apellidos}")
        print(f"Edad            : {self.edad} años")
        print("--------------------------------------------")


# --- Código Principal (Ingreso por teclado y gestión de errores) ---
def main():
    print("====================================")
    print("   SISTEMA DE REGISTRO DE VENTAS    ")
    print("====================================")
    
    try:
        # Solicitamos los datos por teclado
        input_nombre = input("Ingrese el nombre del vendedor: ")
        input_apellidos = input("Ingrese los apellidos del vendedor: ")
        input_edad_str = input("Ingrese la edad del vendedor: ")
        
        # Convertimos el texto ingresado a un número entero
        edad_entero = int(input_edad_str)
        
        # Intentamos instanciar el objeto. Aquí es donde verificar_edad() actuará.
        nuevo_vendedor = Vendedor(input_nombre, input_apellidos, edad_entero)
        
        # Si la línea anterior no lanzó una excepción, imprimimos los datos
        print("\n[Éxito]: Vendedor registrado correctamente.")
        nuevo_vendedor.imprimir()

    # Capturamos las excepciones que nosotros lanzamos (ValueError) o errores de conversión
    except ValueError as error_validacion:
        print(f"\n[ERROR DE VALIDACIÓN]: {error_validacion}. No se pudo crear el vendedor.")
        
    except Exception as error_general:
         print(f"\n[ERROR INESPERADO]: Ha ocurrido un fallo general -> {error_general}")

if __name__ == "__main__":
    main()