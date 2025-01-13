# vistas/cancelar.py
from datetime import datetime, time

import tkinter as tk
from tkinter import messagebox
import re

from conexion.DAO import cancelar_citas_paciente


def abrir_ventana_cancelar(tipos_documento, numero_documento):
    def verificar_formato_fecha():
        fecha_ingresada = entry_fecha.get()
        hora_ingresada = entry_hora_inicio.get()

        patron_fecha = r'^\d{4}-\d{2}-\d{2}$'
        patron_hora = r'^\d{2}:\d{2}:\d{2}$'

        if not re.match(patron_fecha, fecha_ingresada):
            messagebox.showerror("Error", "Formato de fecha incorrecto. Debe ser YYYY-MM-DD.")
            return

        if not re.match(patron_hora, hora_ingresada):
            messagebox.showerror("Error", "Formato de hora incorrecto. Debe ser HH:MM:SS.")
            return

        cancelar(fecha_ingresada, hora_ingresada)

    def cancelar(fecha_consulta_str, hora_ingresada_str):
        fecha_consulta_obj = datetime.strptime(fecha_consulta_str, '%Y-%m-%d').date()

        hora_consulta_obj = datetime.strptime(hora_ingresada_str, '%H:%M:%S').time()

        cancelar_citas_paciente(numero_documento, fecha_consulta_obj, hora_consulta_obj)

    ventana_cancelar = tk.Toplevel()
    ventana_cancelar.title("EPS Formulacion")
    ventana_cancelar.geometry("550x200")

    tk.Label(ventana_cancelar, text="Cancelar Cita", font=("Helvetica", 16)).pack(pady=10)
    
    frame_fecha = tk.Frame(ventana_cancelar)
    frame_fecha.pack(pady=5)
    tk.Label(frame_fecha, text="Fecha de la cita (YYYY-MM-DD):").pack(side=tk.LEFT, padx=5)
    entry_fecha = tk.Entry(frame_fecha)
    entry_fecha.pack(side=tk.LEFT, padx=5)

    frame_hora_inicio = tk.Frame(ventana_cancelar)
    frame_hora_inicio.pack(pady=5)
    tk.Label(frame_hora_inicio, text="Hora de inicio (HH:MM:SS):").pack(side=tk.LEFT, padx=5)
    entry_hora_inicio = tk.Entry(frame_hora_inicio)
    entry_hora_inicio.pack(side=tk.LEFT, padx=5)

    # Botón para cancelar cita
    btn_cancelar = tk.Button(ventana_cancelar, text="Cancelar", command=verificar_formato_fecha)
    btn_cancelar.pack(pady=10)

    # Botón para regresar
    btn_regresar = tk.Button(ventana_cancelar, text="Regresar", command=ventana_cancelar.destroy)
    btn_regresar.pack(side=tk.BOTTOM, anchor=tk.SW, pady=10, padx=10)