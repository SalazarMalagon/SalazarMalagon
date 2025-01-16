# vista/solicitar_cita.py
import tkinter as tk
from tkinter import ttk

from conexion.DAO import cargar_nombre_tipos_de_cita_desde_bd, cargar_especialidades_desde_bd, solicitar_cita_desde_bd
from vistas.disponibles import abrir_ventana_disponibles

def abrir_ventana_solicitar_cita(tipos_documento, numero_documento):
    def solicitar_citas_bd():
        especialidades=combobox_especialidad.get()
        if especialidades=="Cardiología":
            especialidades=1
        if especialidades=="Dermatología":
            especialidades=2
        if especialidades=="Gastroenterología":
            especialidades=3
        if especialidades=="Neurología":
            especialidades=4
        if especialidades=="Oftalmología":
            especialidades=5
        if especialidades=="Ortopedia":
            especialidades=6
        if especialidades=="Pediatría":
            especialidades=7
        if especialidades=="Psiquiatría":
            especialidades=8
        if especialidades=="Radiología":
            especialidades=9
        if especialidades=="Urología":
            especialidades=10
        tipo_cita=combobox_tipo_cita.get()

        if tipo_cita=="Proriotaria":
            tipo_cita=1
        if tipo_cita=="Primera vez":
            tipo_cita=2
        if tipo_cita=="Control":
            tipo_cita=3
        if tipo_cita=="Lectura exámenes":
            tipo_cita=4

        solicitar="Disponible"

        solicitar_cita_desde_bd(especialidades,tipo_cita, solicitar)

        X1, X2, X3, X4, X5 = solicitar_cita_desde_bd(especialidades, tipo_cita, solicitar)

        abrir_ventana_disponibles(numero_documento, X1, X2, X3, X4, X5)

    ventana_solicitar = tk.Toplevel()
    ventana_solicitar.title("EPS Formulacion")
    ventana_solicitar.geometry("550x300")

    tk.Label(ventana_solicitar, text="¿Que deseas realizar?", font=("Helvetica", 16)).pack(pady=10)
    
    frame_especialidad = tk.Frame(ventana_solicitar)
    frame_especialidad.pack(pady=5)
    tk.Label(frame_especialidad, text="Especialidad:").pack(side=tk.LEFT, padx=5)
    especialidades = cargar_especialidades_desde_bd()
    combobox_especialidad = ttk.Combobox(frame_especialidad, values=especialidades)
    combobox_especialidad.pack(side=tk.LEFT, padx=5)

    frame_tipo_cita = tk.Frame(ventana_solicitar)
    frame_tipo_cita.pack(pady=5)
    tk.Label(frame_tipo_cita, text="Tipo de cita:").pack(side=tk.LEFT, padx=5)
    tipo_cita= cargar_nombre_tipos_de_cita_desde_bd()
    combobox_tipo_cita = ttk.Combobox(frame_tipo_cita, values=tipo_cita)
    combobox_tipo_cita.pack(side=tk.LEFT, padx=5)

    btn_solicitar_citas = tk.Button(ventana_solicitar, text="Solicitar cita", command=solicitar_citas_bd)
    btn_solicitar_citas.pack(pady=10)   

    btn_cerrar = tk.Button(ventana_solicitar, text="Cerrar", command=ventana_solicitar.destroy)
    btn_cerrar.pack(side=tk.BOTTOM, anchor=tk.SW, pady=10, padx=10)