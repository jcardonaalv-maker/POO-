class Calculadora:
    """Clase que realiza operaciones matemáticas demostrando el manejo de excepciones."""
    
    def dividir(self, numerador, denominador):
        # Bloque TRY: Donde puede ocurrir la excepción
        try:
            resultado = numerador / denominador
            print(f"Éxito: El resultado de la división es {resultado}")
            
        # Bloque EXCEPT específico (Equivalente al catch de ArithmeticException)
        except ZeroDivisionError as e:
            print("Error Aritmético: ¡No se puede dividir por cero!")
            
        # Bloque EXCEPT general (Equivalente al catch de Exception genérica)
        except Exception as e:
            print(f"Error Inesperado: Ha ocurrido una excepción general -> {e}")
            
        # Bloque FINALLY: Se ejecuta SIEMPRE, haya error o no
        finally:
            print("[Finally] -> Limpieza/Cierre: Esta instrucción se ejecuta siempre, haya o no excepción.\n")


# --- Código para ejecutar el programa ---
if __name__ == "__main__":
    calc = Calculadora()
    
    print("--- CASO 1: División normal ---")
    calc.dividir(10, 2)
    
    print("--- CASO 2: División por cero (Provocando la excepción) ---")
    calc.dividir(5, 0)
    
    print("--- CASO 3: Excepción genérica (Tipos de datos incorrectos) ---")
    calc.dividir("Hola", 2)