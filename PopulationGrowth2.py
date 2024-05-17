import tkinter as tk
from tkinter import ttk, messagebox
import sympy as sp
import math
import matplotlib.pyplot as plt


class ParametrosVentana(tk.Toplevel):
    """
    Ventana para configurar los parámetros de la simulación.
    """

    def __init__(self, parent):
        """
        Inicializa la ventana con los parámetros de la simulación.
        
        Args:
            parent (tk.Tk): La ventana principal de la aplicación.
        """
        super().__init__(parent)
        self.title("Parámetros de la Simulación")
        self.geometry("400x300")
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        """
        Crea los widgets de la ventana de configuración de parámetros.
        """
        style = ttk.Style()
        style.configure("Custom.TEntry", padding=5, borderwidth=2, relief="solid", bordercolor="black", borderradius=10, width=30)
        self.geometry("330x400")

        # Subdivisión de nacimientos
        lbl_nacimientos = ttk.Label(self, text="Nacimientos:", font=("Arial", 12, "bold"), background="lightgray", foreground="black")
        lbl_nacimientos.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        lbl_sorpresa = ttk.Label(self, text="Embarazos sorpresa:")
        lbl_sorpresa.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.txt_sorpresa = ttk.Entry(self, style='Custom.TEntry')
        self.txt_sorpresa.insert(tk.END, "sp.sqrt(tiempo)")
        self.txt_sorpresa.grid(row=1, column=1, padx=5, pady=5)

        lbl_planeados = ttk.Label(self, text="Embarazos planeados:")
        lbl_planeados.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.txt_planeados = ttk.Entry(self)
        self.txt_planeados.insert(tk.END, "tiempo ** 3/2*sp.sqrt(tiempo)")
        self.txt_planeados.grid(row=2, column=1, padx=5, pady=5)

        # Subdivisión de muertes
        lbl_muertes = ttk.Label(self, text="Muertes:", font=("Arial", 12, "bold"), background="lightgray", foreground="black")
        lbl_muertes.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        lbl_accidente = ttk.Label(self, text="Muerte por accidente:")
        lbl_accidente.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        self.txt_accidente = ttk.Entry(self)
        self.txt_accidente.insert(tk.END, "20 * (tiempo ** 2)")
        self.txt_accidente.grid(row=4, column=1, padx=5, pady=5)

        lbl_enfermedad = ttk.Label(self, text="Muerte por enfermedad:")
        lbl_enfermedad.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        self.txt_enfermedad = ttk.Entry(self)
        self.txt_enfermedad.insert(tk.END, "tiempo * 15")
        self.txt_enfermedad.grid(row=5, column=1, padx=5, pady=5)

        lbl_robo = ttk.Label(self, text="Muerte por robo:")
        lbl_robo.grid(row=6, column=0, padx=5, pady=5, sticky="w")

        self.txt_robo = ttk.Entry(self)
        self.txt_robo.insert(tk.END, "50 * tiempo")
        self.txt_robo.grid(row=6, column=1, padx=5, pady=5)

        # Subdivisión de inmigrantes
        lbl_inmigrantes = ttk.Label(self, text="Inmigrantes:", font=("Arial", 12, "bold"), background="lightgray", foreground="black")
        lbl_inmigrantes.grid(row=7, column=0, padx=5, pady=5, sticky="w")

        lbl_xenofobia = ttk.Label(self, text="Xenofobia:")
        lbl_xenofobia.grid(row=8, column=0, padx=5, pady=5, sticky="w")

        self.txt_xenofobia = ttk.Entry(self)
        self.txt_xenofobia.insert(tk.END, "tiempo*3/(sp.sqrt(tiempo))")
        self.txt_xenofobia.grid(row=8, column=1, padx=5, pady=5)

        lbl_asilo = ttk.Label(self, text="Asilo:")
        lbl_asilo.grid(row=9, column=0, padx=5, pady=5, sticky="w")

        self.txt_asilo = ttk.Entry(self)
        self.txt_asilo.insert(tk.END, "sp.sqrt(tiempo)")
        self.txt_asilo.grid(row=9, column=1, padx=5, pady=5)

        lbl_laboral = ttk.Label(self, text="Oportunidad laboral:")
        lbl_laboral.grid(row=10, column=0, padx=5, pady=5, sticky="w")

        self.txt_laboral = ttk.Entry(self)
        self.txt_laboral.insert(tk.END, "tiempo * 2")
        self.txt_laboral.grid(row=10, column=1, padx=5, pady=5)

        btn_aceptar = ttk.Button(self, text="Aceptar", command=self.aceptar)
        btn_aceptar.grid(row=12, columnspan=2, padx=5, pady=5)

    def aceptar(self):
        """
        Guarda los parámetros ingresados y cierra la ventana.
        """
        nacimientos = {
            'sorpresa': self.txt_sorpresa.get(),
            'planeados': self.txt_planeados.get()
        }

        muertes = {
            'accidente': self.txt_accidente.get(),
            'enfermedad': self.txt_enfermedad.get(),
            'robo': self.txt_robo.get()
        }

        inmigrantes = {
            'xenofobia': self.txt_xenofobia.get(),
            'asilo': self.txt_asilo.get(),
            'laboral': self.txt_laboral.get()
        }
        print(nacimientos)
        print(muertes)
        print(inmigrantes)

        self.parent.actualizar_parametros(nacimientos, muertes, inmigrantes)
        self.destroy()




class Simulacion(tk.Tk):
    """
    La ventana principal de la aplicación de simulación de población.
    """
    poblacion = 0

    def __init__(self):
        """
        Inicializa la ventana principal de la simulación.
        """
        super().__init__()
        self.title("Simulación de Población")
        self.geometry("400x300")
        messagebox.showwarning("Advertencia", "De este proyecto no esperen nada de Interfaz Gráfica, ya no nos gusta centrar divs, entramos en huelga.")
        self.create_widgets()

    def create_widgets(self):
        """
        Crea los widgets de la ventana principal.
        """
        lbl_poblacion = ttk.Label(self, text="Población inicial:")
        lbl_poblacion.grid(row=0, column=0, padx=5, pady=5)

        self.txt_poblacion = ttk.Entry(self)
        self.txt_poblacion.grid(row=0, column=1, padx=5, pady=5)

        lbl_duracion = ttk.Label(self, text="Duración de la simulación (años):")
        lbl_duracion.grid(row=1, column=0, padx=5, pady=5)

        self.txt_duracion = ttk.Entry(self)
        self.txt_duracion.grid(row=1, column=1, padx=5, pady=5)

        btn_parametros = ttk.Button(self, text="Configurar Parámetros", command=self.configurar_parametros)
        btn_parametros.grid(row=2, columnspan=2, padx=5, pady=5)

        btn_simular = ttk.Button(self, text="Simular", command=self.ejecutar_simulacion)
        btn_simular.grid(row=3, columnspan=2, padx=5, pady=5)

    def configurar_parametros(self):
        """
        Abre la ventana de configuración de parámetros.
        """
        parametros_window = ParametrosVentana(self)
        parametros_window.grab_set()

    def actualizar_parametros(self, nacimientos, muertes, inmigrantes):
        """
        Actualiza los parámetros de la simulación.
        
        Args:
            nacimientos (dict): Parámetros relacionados con los nacimientos.
            muertes (dict): Parámetros relacionados con las muertes.
            inmigrantes (dict): Parámetros relacionados con los inmigrantes.
        """
        self.nacimientos = nacimientos
        self.muertes = muertes
        self.inmigrantes = inmigrantes

    def tasa_muertes(self, tiempo):
        """
        Calcula la tasa de muertes en un momento dado.

        Args:
            tiempo (float): El tiempo en el que se calcula la tasa de muertes.
            poblacion_actual (int): La población actual en ese momento.

        Returns:
            float: La tasa total de muertes en el tiempo especificado.
        """
        muerte_por_accidentes = eval(self.muertes['accidente'], {'tiempo': tiempo}, {'sp': sp})
        muerte_por_enfermedades = eval(self.muertes['enfermedad'], {'tiempo': tiempo}, {'sp': sp})
        muerte_por_robo = eval(self.muertes['robo'], {'tiempo': tiempo}, {'sp': sp})
        total_muertes = muerte_por_accidentes + muerte_por_enfermedades + muerte_por_robo
        return total_muertes

    def tasa_muertes_integral(self, tiempo_inicio, tiempo_fin):
        """
        Calcula la tasa integral de muertes durante un período de tiempo.

        Args:
            tiempo_inicio (float): El inicio del período de tiempo.
            tiempo_fin (float): El final del período de tiempo.
            poblacion (int): La población durante el período de tiempo.

        Returns:
            int: La tasa integral de muertes durante el período de tiempo especificado.
        """
        tiempo = sp.symbols('tiempo')
        integral = sp.integrate(self.tasa_muertes(tiempo), (tiempo, tiempo_inicio, tiempo_fin))
        return math.ceil(integral.evalf())

    def tasa_nacimientos(self, tiempo):
        """
        Calcula la tasa de nacimientos en un momento dado.

        Args:
            tiempo (float): El tiempo en el que se calcula la tasa de nacimientos.
            poblacion_actual (int): La población actual en ese momento.

        Returns:
            float: La tasa total de nacimientos en el tiempo especificado.
        """
        embarazos_sorpresa = eval(self.nacimientos['sorpresa'], {'tiempo': tiempo}, {'sp': sp})
        embarazos_planeados = eval(self.nacimientos['planeados'], {'tiempo': tiempo}, {'sp': sp})
        total_nacimientos = embarazos_sorpresa + embarazos_planeados
        return total_nacimientos

    def tasa_nacimientos_integral(self, tiempo_inicio, tiempo_fin):
        """
        Calcula la tasa integral de nacimientos durante un período de tiempo.

        Args:
            tiempo_inicio (float): El inicio del período de tiempo.
            tiempo_fin (float): El final del período de tiempo.
            poblacion (int): La población durante el período de tiempo.

        Returns:
            int: La tasa integral de nacimientos durante el período de tiempo especificado.
        """
        tiempo = sp.symbols('tiempo')
        integral = sp.integrate(self.tasa_nacimientos(tiempo), (tiempo, tiempo_inicio, tiempo_fin))
        return math.ceil(integral.evalf())

    def tasa_inmigrantes(self, tiempo):
        """
        Calcula la tasa de inmigrantes en un momento dado.

        Args:
            tiempo (float): El tiempo en el que se calcula la tasa de inmigrantes.

        Returns:
            float: La tasa total de inmigrantes en el tiempo especificado.
        """
        xenofobia = eval(self.inmigrantes['xenofobia'])
        asilo = eval(self.inmigrantes['asilo'])
        oportunidad_laboral = eval(self.inmigrantes['laboral'])
        total_inmigrantes = asilo + oportunidad_laboral - xenofobia
        return total_inmigrantes

    def tasa_inmigrantes_integral(self, tiempo_inicio, tiempo_fin):
        """
        Calcula la tasa integral de inmigrantes durante un período de tiempo.

        Args:
            tiempo_inicio (float): El inicio del período de tiempo.
            tiempo_fin (float): El final del período de tiempo.

        Returns:
            int: La tasa integral de inmigrantes durante el período de tiempo especificado.
        """
        tiempo = sp.symbols('tiempo')
        integral = sp.integrate(self.tasa_inmigrantes(tiempo), (tiempo, tiempo_inicio, tiempo_fin))
        return math.ceil(integral.evalf())

    def ejecutar_simulacion(self):
        """
        Ejecuta la simulación de población.
        """
        poblacion_str = self.txt_poblacion.get()
        if not poblacion_str or not poblacion_str.isdigit():
            # Mostrar un mensaje de error o tomar alguna otra acción apropiada si el campo está vacío
            messagebox.showerror("Error", "Por favor, ingrese un valor válido para la población inicial.")
            return
        duracion_str = self.txt_duracion.get()
        if not duracion_str or not duracion_str.isdigit():
            messagebox.showerror("Error", "Por favor, ingrese un valor válido para los años.")
            return
        poblacion_inicial = int(poblacion_str)
        tiempo_simulacion = int(duracion_str)

        fig, axs = plt.subplots(2, 2, figsize=(12, 15))

        axs[0, 0].set_title('Población')
        axs[0, 0].grid(True)
        axs[0, 1].set_title('Muertes')
        axs[0, 1].grid(True)
        axs[1, 0].set_title('Nacimientos')
        axs[1, 0].grid(True)
        axs[1, 1].set_title('Inmigrantes')
        axs[1, 1].grid(True)

        poblacion = poblacion_inicial
        poblacionList = [poblacion_inicial]
        muertes = []
        nacimientos = []
        inmigrantes = []

        for t in range(1, tiempo_simulacion + 1):
            muertes.append(self.tasa_muertes_integral(0, t))
            nacimientos.append(self.tasa_nacimientos_integral(0, t))
            inmigrantes.append(self.tasa_inmigrantes_integral(0, t))
            poblacion_final = nacimientos[-1] + inmigrantes[-1] - muertes[-1]
            poblacion += poblacion_final
            if poblacion < 0:
                messagebox.showerror("Error", "La población ha llegado a ser menor que cero. La simulación se detendrá. Ya no hay nada, ni nadie, soledad y desesperación, el fin del mundo :D. Lo han hecho mejor los humanos en mantenerse vivos, eso deja mucho que desear.")
                return
            poblacionList.append(poblacion)

            axs[0, 0].plot(range(t + 1), poblacionList, color='blue')
            axs[0, 1].plot(range(1, t + 1), muertes, color='red')
            axs[1, 0].plot(range(1, t + 1), nacimientos, color='green')
            axs[1, 1].plot(range(1, t + 1), inmigrantes, color='orange')

            plt.pause(0.5)

        plt.figure()
        plt.plot(range(tiempo_simulacion + 1), poblacionList, label='Población', color='blue')
        plt.plot(range(1, tiempo_simulacion + 1), muertes, label='Muertes', color='red')
        plt.plot(range(1, tiempo_simulacion + 1), nacimientos, label='Nacimientos', color='green')
        plt.plot(range(1, tiempo_simulacion + 1), inmigrantes, label='Inmigrantes', color='orange')
        plt.xlabel('Años')
        plt.ylabel('Cantidad')
        plt.title('Evolución de la población, muertes, nacimientos e inmigrantes')
        plt.legend()
        plt.grid(True)
        messagebox.showwarning("Población final",f"La población final es: {poblacion}")

        plt.show()


if __name__ == '__main__':
    app = Simulacion()
    app.mainloop()