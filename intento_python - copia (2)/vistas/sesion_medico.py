# vistas/sesion_medico.py
import tkinter as tk

from vistas.agenda import abrir_ventana_agenda

def abrir_ventana_sesion_medico(tipos_documento, numero_documento):

    def llamar_agenda():
        abrir_ventana_agenda(tipos_documento, numero_documento)

    ventana_sesion_medico = tk.Toplevel()
    ventana_sesion_medico.title("EPS Formulacion")
    ventana_sesion_medico.geometry("550x300")

    tk.Label(ventana_sesion_medico, text="¿Que deseas realizar?", font=("Helvetica", 16)).pack(pady=10)
    
    btn_agenda = tk.Button(ventana_sesion_medico, text="Crear Agenda", command=llamar_agenda)
    btn_agenda.pack(pady=10)