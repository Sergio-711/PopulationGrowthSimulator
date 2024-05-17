import tkinter as tk
from tkinter import ttk, messagebox
import sympy as sp
import math
import matplotlib.pyplot as plt


class ParametersWindow(tk.Toplevel):
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
        lbl_births = ttk.Label(self, text="Nacimientos:", font=("Arial", 12, "bold"), background="lightgray", foreground="black")
        lbl_births.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        lbl_surprise = ttk.Label(self, text="Embarazos sorpresa:")
        lbl_surprise.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.txt_surprise = ttk.Entry(self, style='Custom.TEntry')
        self.txt_surprise.insert(tk.END, "20 * sp.sqrt(tiempo)")
        self.txt_surprise.grid(row=1, column=1, padx=5, pady=5)

        lbl_planned = ttk.Label(self, text="Embarazos planeados:")
        lbl_planned.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.txt_planned = ttk.Entry(self)
        self.txt_planned.insert(tk.END, "20 * tiempo**3")
        self.txt_planned.grid(row=2, column=1, padx=5, pady=5)

        # Subdivisión de muertes
        lbl_deaths = ttk.Label(self, text="Muertes:", font=("Arial", 12, "bold"), background="lightgray", foreground="black")
        lbl_deaths.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        lbl_accident = ttk.Label(self, text="Muerte por accidente:")
        lbl_accident.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        self.txt_accident = ttk.Entry(self)
        self.txt_accident.insert(tk.END, "20 * tiempo")
        self.txt_accident.grid(row=4, column=1, padx=5, pady=5)

        lbl_disease = ttk.Label(self, text="Muerte por enfermedad:")
        lbl_disease.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        self.txt_disease = ttk.Entry(self)
        self.txt_disease.insert(tk.END, "10 * tiempo**3")
        self.txt_disease.grid(row=5, column=1, padx=5, pady=5)

        lbl_theft = ttk.Label(self, text="Muerte por robo:")
        lbl_theft.grid(row=6, column=0, padx=5, pady=5, sticky="w")

        self.txt_theft = ttk.Entry(self)
        self.txt_theft.insert(tk.END, "50 * tiempo")
        self.txt_theft.grid(row=6, column=1, padx=5, pady=5)

        # Subdivisión de inmigrantes
        lbl_immigrants = ttk.Label(self, text="Inmigrantes:", font=("Arial", 12, "bold"), background="lightgray", foreground="black")
        lbl_immigrants.grid(row=7, column=0, padx=5, pady=5, sticky="w")

        lbl_xenophobia = ttk.Label(self, text="Xenofobia:")
        lbl_xenophobia.grid(row=8, column=0, padx=5, pady=5, sticky="w")

        self.txt_xenophobia = ttk.Entry(self)
        self.txt_xenophobia.insert(tk.END, "(15 * tiempo) / sp.sqrt(tiempo)")
        self.txt_xenophobia.grid(row=8, column=1, padx=5, pady=5)

        lbl_asylum = ttk.Label(self, text="Asilo:")
        lbl_asylum.grid(row=9, column=0, padx=5, pady=5, sticky="w")

        self.txt_asylum = ttk.Entry(self)
        self.txt_asylum.insert(tk.END, "tiempo")
        self.txt_asylum.grid(row=9, column=1, padx=5, pady=5)

        lbl_job_opportunity = ttk.Label(self, text="Oportunidad laboral:")
        lbl_job_opportunity.grid(row=10, column=0, padx=5, pady=5, sticky="w")

        self.txt_job_opportunity = ttk.Entry(self)
        self.txt_job_opportunity.insert(tk.END, "18 * tiempo")
        self.txt_job_opportunity.grid(row=10, column=1, padx=5, pady=5)

        btn_accept = ttk.Button(self, text="Aceptar", command=self.accept)
        btn_accept.grid(row=12, columnspan=2, padx=5, pady=5)

    def aceept(self):
        """
        Guarda los parámetros ingresados y cierra la ventana.
        """
        births = {
            'sorpresa': self.txt_surprise.get(),
            'planeados': self.txt_planned.get()
        }

        deaths = {
            'accidente': self.txt_accidente.get(),
            'enfermedad': self.txt_disease.get(),
            'robo': self.txt_theft.get()
        }

        inmigrants = {
            'xenofobia': self.txt_xenophobia.get(),
            'asilo': self.txt_asylum.get(),
            'laboral': self.txt_job_opportunity.get()
        }
        print(births)
        print(deaths)
        print(inmigrants)

        self.parent.update_parameters(births, deaths, inmigrants)
        self.destroy()




class Simulation(tk.Tk):
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
        lbl_population = ttk.Label(self, text="Población inicial:")
        lbl_population.grid(row=0, column=0, padx=5, pady=5)

        self.txt_population = ttk.Entry(self)
        self.txt_population.grid(row=0, column=1, padx=5, pady=5)

        lbl_duration = ttk.Label(self, text="Duración de la simulación (años):")
        lbl_duration.grid(row=1, column=0, padx=5, pady=5)

        self.txt_duration = ttk.Entry(self)
        self.txt_duration.grid(row=1, column=1, padx=5, pady=5)

        btn_parameters = ttk.Button(self, text="Configurar Parámetros", command=self.configure_parameters)
        btn_parameters.grid(row=2, columnspan=2, padx=5, pady=5)

        btn_simulate = ttk.Button(self, text="Simular", command=self.ejecutar_simulacion)
        btn_simulate.grid(row=3, columnspan=2, padx=5, pady=5)

    def configure_parameters(self):
        """
        Abre la ventana de configuración de parámetros.
        """
        parameters_window = ParametersWindow(self)
        parameters_window.grab_set()

    def update_parameters(self, births, deaths, inmigrants):
        """
        Actualiza los parámetros de la simulación.
        
        Args:
            nacimientos (dict): Parámetros relacionados con los nacimientos.
            muertes (dict): Parámetros relacionados con las muertes.
            inmigrantes (dict): Parámetros relacionados con los inmigrantes.
        """
        self.births = births
        self.deaths = deaths
        self.inmigrants = inmigrants

    def death_rate(self, tiempo, actual_population):
        """
        Calcula la tasa de muertes en un momento dado.

        Args:
            tiempo (float): El tiempo en el que se calcula la tasa de muertes.
            actual_population (int): La población actual en ese momento.

        Returns:
            float: La tasa total de muertes en el tiempo especificado.
        """
        death_by_accidents = eval(self.deaths['accidente'], {'tiempo': tiempo, 'poblacion': actual_population}, {'sp': sp})
        death_by_diseases = eval(self.deaths['enfermedad'], {'tiempo': tiempo, 'poblacion': actual_population}, {'sp': sp})
        death_by_theft = eval(self.deaths['robo'], {'tiempo': tiempo, 'poblacion': actual_population}, {'sp': sp})
        total_deaths = death_by_accidents + death_by_diseases + death_by_theft
        return total_deaths

    def integral_death_rate(self, start_time, end_time, poblacion):
        """
        Calcula la tasa integral de muertes durante un período de tiempo.

        Args:
            start_time (float): El inicio del período de tiempo.
            end_time (float): El final del período de tiempo.
            poblacion (int): La población durante el período de tiempo.

        Returns:
            int: La tasa integral de muertes durante el período de tiempo especificado.
        """
        tiempo = sp.symbols('tiempo')
        integral = sp.integrate(self.death_rate(tiempo, poblacion), (tiempo, start_time, end_time))
        return math.ceil(integral.evalf() / poblacion)

    def tasa_nacimientos(self, tiempo, actual_population):
        """
        Calcula la tasa de nacimientos en un momento dado.

        Args:
            tiempo (float): El tiempo en el que se calcula la tasa de nacimientos.
            actual_population (int): La población actual en ese momento.

        Returns:
            float: La tasa total de nacimientos en el tiempo especificado.
        """
        embarazos_sorpresa = eval(self.births['sorpresa'], {'tiempo': tiempo, 'poblacion': actual_population}, {'sp': sp})
        embarazos_planeados = eval(self.births['planeados'], {'tiempo': tiempo, 'poblacion': actual_population}, {'sp': sp})
        total_nacimientos = embarazos_sorpresa + embarazos_planeados
        return total_nacimientos

    def tasa_nacimientos_integral(self, start_time, end_time, poblacion):
        """
        Calcula la tasa integral de nacimientos durante un período de tiempo.

        Args:
            start_time (float): El inicio del período de tiempo.
            end_time (float): El final del período de tiempo.
            poblacion (int): La población durante el período de tiempo.

        Returns:
            int: La tasa integral de nacimientos durante el período de tiempo especificado.
        """
        tiempo = sp.symbols('tiempo')
        integral = sp.integrate(self.tasa_nacimientos(tiempo, poblacion), (tiempo, start_time, end_time))
        return math.ceil(integral.evalf() / poblacion)

    def tasa_inmigrantes(self, tiempo):
        """
        Calcula la tasa de inmigrantes en un momento dado.

        Args:
            tiempo (float): El tiempo en el que se calcula la tasa de inmigrantes.

        Returns:
            float: La tasa total de inmigrantes en el tiempo especificado.
        """
        xenofobia = eval(self.inmigrants['xenofobia'])
        asilo = eval(self.inmigrants['asilo'])
        oportunidad_laboral = eval(self.inmigrants['laboral'])
        total_inmigrantes = asilo + oportunidad_laboral - xenofobia
        return total_inmigrantes

    def tasa_inmigrantes_integral(self, start_time, end_time):
        """
        Calcula la tasa integral de inmigrantes durante un período de tiempo.

        Args:
            start_time (float): El inicio del período de tiempo.
            end_time (float): El final del período de tiempo.

        Returns:
            int: La tasa integral de inmigrantes durante el período de tiempo especificado.
        """
        tiempo = sp.symbols('tiempo')
        integral = sp.integrate(self.tasa_inmigrantes(tiempo), (tiempo, start_time, end_time))
        return math.ceil(integral.evalf())

    def ejecutar_simulacion(self):
        """
        Ejecuta la simulación de población.
        """
        poblacion_str = self.txt_population.get()
        if not poblacion_str or not poblacion_str.isdigit():
            # Mostrar un mensaje de error o tomar alguna otra acción apropiada si el campo está vacío
            messagebox.showerror("Error", "Por favor, ingrese un valor válido para la población inicial.")
            return
        duracion_str = self.txt_duration.get()
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
        deaths = []
        births = []
        inmigrants = []

        for t in range(1, tiempo_simulacion + 1):
            deaths.append(self.integral_death_rate(0, t, poblacion))
            births.append(self.tasa_nacimientos_integral(0, t, poblacion))
            inmigrants.append(self.tasa_inmigrantes_integral(0, t))
            print()
            poblacion_final = births[-1] + inmigrants[-1] - deaths[-1]
            poblacion += poblacion_final
            if poblacion < 0:
                messagebox.showerror("Error", "La población ha llegado a ser menor que cero. La simulación se detendrá. Ya no hay nada, ni nadie, soledad y desesperación, el fin del mundo :D. Lo han hecho mejor los humanos en mantenerse vivos, eso deja mucho que desear.")
                return
            poblacionList.append(poblacion)

            axs[0, 0].plot(range(t + 1), poblacionList, color='blue')
            axs[0, 1].plot(range(1, t + 1), deaths, color='red')
            axs[1, 0].plot(range(1, t + 1), births, color='green')
            axs[1, 1].plot(range(1, t + 1), inmigrants, color='orange')

            plt.pause(0.5)

        plt.figure()
        plt.plot(range(tiempo_simulacion + 1), poblacionList, label='Población', color='blue')
        plt.plot(range(1, tiempo_simulacion + 1), deaths, label='Muertes', color='red')
        plt.plot(range(1, tiempo_simulacion + 1), births, label='Nacimientos', color='green')
        plt.plot(range(1, tiempo_simulacion + 1), inmigrants, label='Inmigrantes', color='orange')
        plt.xlabel('Años')
        plt.ylabel('Cantidad')
        plt.title('Evolución de la población, muertes, nacimientos e inmigrantes')
        plt.legend()
        plt.grid(True)

        plt.show()


if __name__ == '__main__':
    app = Simulation()
    app.mainloop()
