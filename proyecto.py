import tkinter as tk
from tkinter import messagebox
import random

# Función para solicitar un número válido de estaciones meteorológicas
def obtener_num_estaciones():
    """
    Esta función solicita al usuario el número de estaciones meteorológicas.
    Si la entrada no es un número entero válido o es menor o igual a cero,
    se muestra un mensaje de error.
    """
    try:
        num_estaciones = int(entry_num_estaciones.get())  # Intenta convertir la entrada a entero
        if num_estaciones <= 0:  # Si el número de estaciones es menor o igual a cero
            messagebox.showerror("Error", "Por favor, ingrese un número mayor que cero.")
        else:
            return num_estaciones  # Devuelve el número válido de estaciones
    except ValueError:
        messagebox.showerror("Error", "Entrada inválida. Debe ingresar un número entero.")
    return None  # Retorna None si hay un error en la entrada

# Función para obtener los nombres de las estaciones
def obtener_nombres_estaciones(num_estaciones):
    """
    Esta función obtiene los nombres de las estaciones meteorológicas desde un cuadro de texto.
    Verifica que la cantidad de nombres ingresados sea igual al número de estaciones
    y que no haya nombres vacíos.
    """
    nombres = text_nombres_estaciones.get("1.0", tk.END).strip().splitlines()  # Obtiene los nombres de las estaciones como una lista
    
    if len(nombres) != num_estaciones:  # Verifica que se haya ingresado el número correcto de nombres
        messagebox.showerror("Error", f"Debe ingresar exactamente {num_estaciones} nombres de estaciones.")
        return None
    
    # Verifica que no haya nombres vacíos
    for nombre in nombres:
        if not nombre.strip():  # Si el nombre está vacío o tiene solo espacios
            messagebox.showerror("Error", "El nombre de una estación no puede estar vacío.")
            return None
    
    return nombres  # Devuelve la lista de nombres de estaciones

# Función para cargar las temperaturas mensuales aleatorias
def cargar_temperaturas(num_estaciones):
    """
    Esta función genera una lista de temperaturas aleatorias para cada estación.
    Cada estación tendrá 12 temperaturas (una por mes), generadas entre -10°C y 40°C.
    """
    temperaturas = []
    for i in range(num_estaciones):
        temperaturas_estacion = [random.uniform(-10, 40) for _ in range(12)]  # Genera temperaturas aleatorias para cada estación
        temperaturas.append(temperaturas_estacion)  # Añade la lista de temperaturas de la estación a la lista total
    return temperaturas  # Devuelve la matriz de temperaturas

# Función para calcular la temperatura media, mínima y máxima de cada estación
def analizar_estaciones(temperaturas):
    """
    Esta función calcula la temperatura media, mínima y máxima para cada estación.
    Devuelve tres listas: medias, mínimas y máximas.
    """
    medias = []
    minimas = []
    maximas = []
    for estacion in temperaturas:
        medias.append(sum(estacion) / len(estacion))  # Calcula la media de las temperaturas de la estación
        minimas.append(min(estacion))  # Encuentra la temperatura mínima de la estación
        maximas.append(max(estacion))  # Encuentra la temperatura máxima de la estación
    return medias, minimas, maximas  # Devuelve las listas de medias, mínimas y máximas

# Función para encontrar la estación con la temperatura más alta y más baja
def estaciones_extremas(estaciones, temperaturas):
    """
    Esta función encuentra la estación con la temperatura más alta y la más baja
    durante todo el año.
    """
    max_temp = float('-inf')  # Inicializa la temperatura máxima con un valor muy bajo
    min_temp = float('inf')   # Inicializa la temperatura mínima con un valor muy alto
    estacion_max = ""
    estacion_min = ""

    for i, estacion in enumerate(estaciones):
        max_temp_estacion = max(temperaturas[i])  # Encuentra la temperatura máxima de la estación
        min_temp_estacion = min(temperaturas[i])  # Encuentra la temperatura mínima de la estación

        # Compara la temperatura máxima de esta estación con la más alta hasta el momento
        if max_temp_estacion > max_temp:
            max_temp = max_temp_estacion
            estacion_max = estacion  # Actualiza la estación con la temperatura más alta

        # Compara la temperatura mínima de esta estación con la más baja hasta el momento
        if min_temp_estacion < min_temp:
            min_temp = min_temp_estacion
            estacion_min = estacion  # Actualiza la estación con la temperatura más baja

    return estacion_max, max_temp, estacion_min, min_temp  # Devuelve las estaciones con las temperaturas extremas

# Función para calcular la temperatura media, mínima y máxima de cada mes
def analizar_meses(temperaturas):
    """
    Esta función calcula la temperatura media, mínima y máxima para cada mes del año
    tomando las temperaturas de todas las estaciones.
    Devuelve tres listas: medias_mensuales, mínimas_mensuales y máximas_mensuales.
    """
    medias_mensuales = []
    minimas_mensuales = []
    maximas_mensuales = []

    for mes in range(12):
        mes_temperaturas = [estacion[mes] for estacion in temperaturas]  # Obtiene las temperaturas de todas las estaciones para el mes
        medias_mensuales.append(sum(mes_temperaturas) / len(mes_temperaturas))  # Calcula la media para el mes
        minimas_mensuales.append(min(mes_temperaturas))  # Encuentra la temperatura mínima para el mes
        maximas_mensuales.append(max(mes_temperaturas))  # Encuentra la temperatura máxima para el mes

    return medias_mensuales, minimas_mensuales, maximas_mensuales  # Devuelve las listas con las estadísticas mensuales

# Función para generar el reporte completo
def generar_reporte(estaciones, temperaturas, medias, minimas, maximas, medias_mensuales, minimas_mensuales, maximas_mensuales, estacion_max, max_temp, estacion_min, min_temp):
    """
    Esta función genera un reporte completo con los análisis realizados:
    - Temperaturas medias, mínimas y máximas para cada estación.
    - Estaciones con las temperaturas extremas.
    - Temperaturas medias, mínimas y máximas por mes.
    El reporte es mostrado en el cuadro de texto `text_report`.
    """
    reporte = "Reporte de Estaciones Meteorológicas:\n"
    for i, estacion in enumerate(estaciones):
        reporte += f"\nEstación {estacion}:\n"
        reporte += f"Temperatura media: {medias[i]:.2f}°C\n"
        reporte += f"Temperatura mínima: {minimas[i]:.2f}°C\n"
        reporte += f"Temperatura máxima: {maximas[i]:.2f}°C\n"

    reporte += f"\nEstación con la temperatura más alta: {estacion_max} ({max_temp:.2f}°C)\n"
    reporte += f"Estación con la temperatura más baja: {estacion_min} ({min_temp:.2f}°C)\n"

    reporte += "\nTemperaturas medias, mínimas y máximas por mes:\n"
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    for i, mes in enumerate(meses):
        reporte += f"{mes}: Media = {medias_mensuales[i]:.2f}°C, Mínima = {minimas_mensuales[i]:.2f}°C, Máxima = {maximas_mensuales[i]:.2f}°C\n"

    # Mostrar el reporte en el cuadro de texto
    text_report.delete(1.0, tk.END)  # Limpia el cuadro de texto
    text_report.insert(tk.END, reporte)  # Inserta el reporte generado en el cuadro de texto

# Función principal para ejecutar el programa
def ejecutar_programa():
    """
    Esta es la función principal que coordina la ejecución del programa:
    - Obtiene el número de estaciones
    - Recoge los nombres de las estaciones
    - Carga las temperaturas
    - Realiza el análisis de las estaciones y meses
    - Genera el reporte completo.
    """
    num_estaciones = obtener_num_estaciones()  # Obtiene el número de estaciones
    if num_estaciones is None:
        return
    
    estaciones = obtener_nombres_estaciones(num_estaciones)  # Obtiene los nombres de las estaciones
    if estaciones is None:
        return
    
    temperaturas = cargar_temperaturas(num_estaciones)  # Carga las temperaturas

    medias, minimas, maximas = analizar_estaciones(temperaturas)  # Analiza las estaciones
    estacion_max, max_temp, estacion_min, min_temp = estaciones_extremas(estaciones, temperaturas)  # Analiza las estaciones con temperaturas extremas
    medias_mensuales, minimas_mensuales, maximas_mensuales = analizar_meses(temperaturas)  # Analiza las temperaturas por mes

    generar_reporte(estaciones, temperaturas, medias, minimas, maximas, medias_mensuales, minimas_mensuales, maximas_mensuales, estacion_max, max_temp, estacion_min, min_temp)  # Genera el reporte

# Configuración de la ventana principal
root = tk.Tk()
root.title("Estaciones Meteorológicas")

# Frame para la entrada del número de estaciones
frame_num_estaciones = tk.Frame(root)
frame_num_estaciones.pack(pady=10)

label_num_estaciones = tk.Label(frame_num_estaciones, text="Número de estaciones:")
label_num_estaciones.pack(side=tk.LEFT)
entry_num_estaciones = tk.Entry(frame_num_estaciones)
entry_num_estaciones.pack(side=tk.LEFT)

# Frame para ingresar los nombres de las estaciones
frame_nombres_estaciones = tk.Frame(root)
frame_nombres_estaciones.pack(pady=10)

label_nombres_estaciones = tk.Label(frame_nombres_estaciones, text="Nombres de las estaciones (uno por línea):")
label_nombres_estaciones.pack()

text_nombres_estaciones = tk.Text(frame_nombres_estaciones, height=5, width=30)
text_nombres_estaciones.pack()

# Botón para ejecutar el programa
btn_ejecutar = tk.Button(root, text="Ejecutar Análisis", command=ejecutar_programa)
btn_ejecutar.pack(pady=10)

# Cuadro de texto para mostrar el reporte
text_report = tk.Text(root, height=15, width=80)
text_report.pack(pady=10)

# Ejecutar la interfaz gráfica
root.mainloop()
