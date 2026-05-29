import math
import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod

# --- JERARQUÍA DE CLASES ---

class FiguraGeometrica(ABC):
    def __init__(self):
        self._volumen = 0.0
        self._superficie = 0.0

    def get_volumen(self):
        return self._volumen

    def get_superficie(self):
        return self._superficie

    @abstractmethod
    def calcular_volumen(self):
        pass

    @abstractmethod
    def calcular_superficie(self):
        pass


class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self):
        self._volumen = math.pi * (self.radio ** 2) * self.altura

    def calcular_superficie(self):
        self._superficie = 2 * math.pi * self.radio * self.altura + 2 * math.pi * (self.radio ** 2)


class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio

    def calcular_volumen(self):
        self._volumen = (4.0 / 3.0) * math.pi * (self.radio ** 3)

    def calcular_superficie(self):
        self._superficie = 4 * math.pi * (self.radio ** 2)


class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema

    def calcular_volumen(self):
        self._volumen = ((self.base ** 2) * self.altura) / 3.0

    def calcular_superficie(self):
        # Se asume una pirámide de base cuadrada
        self._superficie = (self.base ** 2) + (2 * self.base * self.apotema)


# --- INTERFAZ GRÁFICA (GUI) Y GESTIÓN DE EVENTOS ---

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas")
        self.geometry("350x550")

        # --- Panel Cilindro ---
        frame_cilindro = tk.LabelFrame(self, text="Cilindro", padx=10, pady=10)
        frame_cilindro.pack(fill="x", padx=10, pady=10)

        tk.Label(frame_cilindro, text="Radio (cm):").grid(row=0, column=0, sticky="e", pady=2)
        self.txt_radio_cilindro = tk.Entry(frame_cilindro)
        self.txt_radio_cilindro.grid(row=0, column=1, pady=2)

        tk.Label(frame_cilindro, text="Altura (cm):").grid(row=1, column=0, sticky="e", pady=2)
        self.txt_altura_cilindro = tk.Entry(frame_cilindro)
        self.txt_altura_cilindro.grid(row=1, column=1, pady=2)

        btn_cilindro = tk.Button(frame_cilindro, text="Calcular Cilindro", command=self.evento_cilindro)
        btn_cilindro.grid(row=2, columnspan=2, pady=10)

        # --- Panel Esfera ---
        frame_esfera = tk.LabelFrame(self, text="Esfera", padx=10, pady=10)
        frame_esfera.pack(fill="x", padx=10, pady=10)

        tk.Label(frame_esfera, text="Radio (cm):").grid(row=0, column=0, sticky="e", pady=2)
        self.txt_radio_esfera = tk.Entry(frame_esfera)
        self.txt_radio_esfera.grid(row=0, column=1, pady=2)

        btn_esfera = tk.Button(frame_esfera, text="Calcular Esfera", command=self.evento_esfera)
        btn_esfera.grid(row=1, columnspan=2, pady=10)

        # --- Panel Pirámide ---
        frame_piramide = tk.LabelFrame(self, text="Pirámide", padx=10, pady=10)
        frame_piramide.pack(fill="x", padx=10, pady=10)

        tk.Label(frame_piramide, text="Base (cm):").grid(row=0, column=0, sticky="e", pady=2)
        self.txt_base_piramide = tk.Entry(frame_piramide)
        self.txt_base_piramide.grid(row=0, column=1, pady=2)

        tk.Label(frame_piramide, text="Altura (cm):").grid(row=1, column=0, sticky="e", pady=2)
        self.txt_altura_piramide = tk.Entry(frame_piramide)
        self.txt_altura_piramide.grid(row=1, column=1, pady=2)

        tk.Label(frame_piramide, text="Apotema (cm):").grid(row=2, column=0, sticky="e", pady=2)
        self.txt_apotema_piramide = tk.Entry(frame_piramide)
        self.txt_apotema_piramide.grid(row=2, column=1, pady=2)

        btn_piramide = tk.Button(frame_piramide, text="Calcular Pirámide", command=self.evento_piramide)
        btn_piramide.grid(row=3, columnspan=2, pady=10)

    # --- Oyentes (Listeners) de los botones ---
    
    def evento_cilindro(self):
        try:
            r = float(self.txt_radio_cilindro.get())
            h = float(self.txt_altura_cilindro.get())
            cilindro = Cilindro(r, h)
            cilindro.calcular_volumen()
            cilindro.calcular_superficie()
            self.mostrar_resultado("Cilindro", cilindro.get_volumen(), cilindro.get_superficie())
        except ValueError:
            self.mostrar_error()

    def evento_esfera(self):
        try:
            r = float(self.txt_radio_esfera.get())
            esfera = Esfera(r)
            esfera.calcular_volumen()
            esfera.calcular_superficie()
            self.mostrar_resultado("Esfera", esfera.get_volumen(), esfera.get_superficie())
        except ValueError:
            self.mostrar_error()

    def evento_piramide(self):
        try:
            b = float(self.txt_base_piramide.get())
            h = float(self.txt_altura_piramide.get())
            a = float(self.txt_apotema_piramide.get())
            piramide = Piramide(b, h, a)
            piramide.calcular_volumen()
            piramide.calcular_superficie()
            self.mostrar_resultado("Pirámide", piramide.get_volumen(), piramide.get_superficie())
        except ValueError:
            self.mostrar_error()

    def mostrar_resultado(self, figura, vol, sup):
        mensaje = f"Resultados de la figura {figura}:\n\nVolumen: {vol:.2f} cm³\nSuperficie: {sup:.2f} cm²"
        messagebox.showinfo(f"Resultado - {figura}", mensaje)

    def mostrar_error(self):
        messagebox.showerror("Error de entrada", "Por favor, ingresa únicamente valores numéricos válidos.")

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()