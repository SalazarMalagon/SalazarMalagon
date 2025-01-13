# vistas/agenda.py
import random
import re
import tkinter as tk
from tkinter import ttk
import uuid
import datetime

from conexion.DAO import cargar_especialidades_desde_bd, registrar_bd_agenda, registrar_bd_cita


def abrir_ventana_agenda(tipos_documento, numero_documento):

    def validar_fecha(fecha):
        patron = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        return bool(patron.match(fecha))

    def validar_hora(hora):
        patron_hora = re.compile(r'^\d{2}:\d{2}:\d{2}$')
        return bool(patron_hora.match(hora))
    
    def validar_y_abrir_ventana():
        tipos_documento_predeterminado="CC"
        numero_documento_predeterminado=777777777
        disponibilidad="Disponible"
        id_cita = uuid.uuid4().int & (1 << 32) - 1
        id_cita = id_cita % 100000

        fecha = entry_fecha.get()
        hora_inicio = entry_hora_inicio.get()
        hora_final = entry_hora_final.get()

        if not validar_fecha(fecha):
            tk.messagebox.showerror("Error", "Formato de fecha incorrecto. Debe ser YYYY-MM-DD.")
            return
        if not validar_hora(hora_inicio):
            tk.messagebox.showerror("Error", "Formato de hora de inicio incorrecto. Debe ser HH:MM:SS.")
            return
        if not validar_hora(hora_final):
            tk.messagebox.showerror("Error", "Formato de hora final incorrecto. Debe ser HH:MM:SS.")
            return
        
        fecha_obj = datetime.datetime.strptime(fecha, '%Y-%m-%d')
        hora_inicio_obj = datetime.datetime.strptime(hora_inicio, '%H:%M:%S').time()
        hora_final_obj = datetime.datetime.strptime(hora_final, '%H:%M:%S').time()
        hora_inicio_str = hora_inicio_obj.strftime('%H:%M')
        hora_final_str = hora_final_obj.strftime('%H:%M')


        año, mes, dia = fecha.split("-")
        if mes == "01":
            mes=1
        if mes == "02":
            mes=2
        if mes == "03":
            mes=3
        if mes == "04":
            mes=4
        if mes == "05":
            mes=5
        if mes == "06":
            mes=6
        if mes == "07":
            mes=7
        if mes == "08":
            mes=8
        if mes == "09":
            mes=9
        if mes == "10":
            mes=10
        if mes == "11":
            mes=11
        if mes == "12":
            mes=12

        tipos_cita=combobox_tipo_cita.get()
        if tipos_cita=="Prioritaria":
            tipos_cita= 1
        if tipos_cita=="Primera vez":
            tipos_cita= 2
        if tipos_cita=="Control":
            tipos_cita= 3
        if tipos_cita=="Lectura exámenes":
            tipos_cita= 4

        año=int(año)
        print("Año:", año)
        print("Mes:", mes)
        print("Día:", dia)
        agenda = uuid.uuid4().int & (1 << 32) - 1
        agenda = agenda % 100000


        registrar_bd_agenda(tipos_documento, numero_documento, agenda, mes, año)
        registrar_bd_cita(id_cita, tipos_cita, hora_inicio_str, hora_final_str, fecha_obj, disponibilidad, tipos_documento_predeterminado, numero_documento_predeterminado, agenda, tipos_documento, numero_documento)

        print(f"{tipos_documento}{numero_documento}Abrir ventana con fecha: {fecha}, hora de inicio: {hora_inicio} y hora final: {hora_final}")

    ventana_agenda = tk.Toplevel()
    ventana_agenda.title("EPS Formulacion")
    ventana_agenda.geometry("550x300")

    tk.Label(ventana_agenda, text="Agenda", font=("Helvetica", 16)).pack(pady=10)

    frame_fecha = tk.Frame(ventana_agenda)
    frame_fecha.pack(pady=5)
    tk.Label(frame_fecha, text="Fecha (YYYY-MM-DD):").pack(side=tk.LEFT, padx=5)
    entry_fecha = tk.Entry(frame_fecha)
    entry_fecha.pack(side=tk.LEFT, padx=5)

    frame_especialidad = tk.Frame(ventana_agenda)
    frame_especialidad.pack(pady=5)
    tk.Label(frame_especialidad, text="Especialidad:").pack(side=tk.LEFT, padx=5)
    especialidades = cargar_especialidades_desde_bd()
    combobox_especialidad = ttk.Combobox(frame_especialidad, values=especialidades)
    combobox_especialidad.pack(side=tk.LEFT, padx=5)

    frame_tipo_cita = tk.Frame(ventana_agenda)
    frame_tipo_cita.pack(pady=5)
    tk.Label(frame_tipo_cita, text="Tipo de cita:").pack(side=tk.LEFT, padx=5)
    tipos_cita = ["Prioritaria", "Primera vez", "Control", "Lectura exámenes"]
    combobox_tipo_cita = ttk.Combobox(frame_tipo_cita, values=tipos_cita)
    combobox_tipo_cita.pack(side=tk.LEFT, padx=5)

    frame_hora_inicio = tk.Frame(ventana_agenda)
    frame_hora_inicio.pack(pady=5)
    tk.Label(frame_hora_inicio, text="Hora de inicio (HH:MM:SS):").pack(side=tk.LEFT, padx=5)
    entry_hora_inicio = tk.Entry(frame_hora_inicio)
    entry_hora_inicio.pack(side=tk.LEFT, padx=5)

    frame_hora_final = tk.Frame(ventana_agenda)
    frame_hora_final.pack(pady=5)
    tk.Label(frame_hora_final, text="Hora final (HH:MM:SS):").pack(side=tk.LEFT, padx=5)
    entry_hora_final = tk.Entry(frame_hora_final)
    entry_hora_final.pack(side=tk.LEFT, padx=5)

    btn_abrir_ventana = tk.Button(ventana_agenda, text="Añadir Agenda", command=validar_y_abrir_ventana)
    btn_abrir_ventana.pack(pady=10)

    btn_cerrar = tk.Button(ventana_agenda, text="Cerrar", command=ventana_agenda.destroy)
    btn_cerrar.pack(side=tk.BOTTOM, anchor=tk.SW, pady=10, padx=10)