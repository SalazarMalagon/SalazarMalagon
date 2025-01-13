# vistas/consultar.py
import re
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from conexion.DAO import consultar_citas_paciente

def abrir_ventana_consultar(tipos_documento, numero_documento):

    def verificar_formato_fecha():
        fecha_ingresada = entry_fecha.get()
        patron = r'^\d{4}-\d{2}-\d{2}$'
        
        if not re.match(patron, fecha_ingresada):
            messagebox.showerror("Error", "Formato de fecha incorrecto. Debe ser YYYY-MM-DD.")
        else:
            buscar_cita()
            


    def buscar_cita():
        fecha_consulta_str = entry_fecha.get()
        fecha_consulta_obj = datetime.strptime(fecha_consulta_str, '%Y-%m-%d').date()

        consultar_citas_paciente(numero_documento,fecha_consulta_obj)
    

    ventana_consultar = tk.Toplevel()
    ventana_consultar.title("EPS Formulacion")
    ventana_consultar.geometry("550x200")

    tk.Label(ventana_consultar, text="Consultar cita", font=("Helvetica", 16)).pack(pady=10)

    frame_fecha = tk.Frame(ventana_consultar)
    frame_fecha.pack(pady=5)
    tk.Label(frame_fecha, text="Fecha (YYYY-MM-DD):").pack(side=tk.LEFT, padx=5)
    entry_fecha = tk.Entry(frame_fecha)
    entry_fecha.pack(side=tk.LEFT, padx=5)

    # Botón para buscar cita
    btn_buscar = tk.Button(ventana_consultar, text="Buscar", command=verificar_formato_fecha)
    btn_buscar.pack(pady=10)

    # Botón para regresar
    btn_regresar = tk.Button(ventana_consultar, text="Regresar", command=ventana_consultar.destroy)
    btn_regresar.pack(side=tk.BOTTOM, anchor=tk.SW, pady=10, padx=10)
