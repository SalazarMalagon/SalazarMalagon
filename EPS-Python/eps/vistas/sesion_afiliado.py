# vistas/sesion_medico.py
import tkinter as tk
from vistas.cancelar import abrir_ventana_cancelar
from vistas.consultar import abrir_ventana_consultar

from vistas.solicitar_cita import abrir_ventana_solicitar_cita

def abrir_ventana_sesion_afiliado(tipos_documento, numero_documento):

    def consulta():
        abrir_ventana_consultar(tipos_documento, numero_documento)

    def cancelar():
        abrir_ventana_cancelar(tipos_documento, numero_documento)

    def solicitar():
        abrir_ventana_solicitar_cita(tipos_documento, numero_documento)

    ventana_sesion_afiliado = tk.Toplevel()
    ventana_sesion_afiliado.title("EPS Formulacion")
    ventana_sesion_afiliado.geometry("550x300")

    tk.Label(ventana_sesion_afiliado, text="¿Que deseas realizar?", font=("Helvetica", 16)).pack(pady=10)
    
    btn_solicitar = tk.Button(ventana_sesion_afiliado, text="Solicitar cita", command=solicitar)
    btn_solicitar.pack(pady=10)

    btn_consultar = tk.Button(ventana_sesion_afiliado, text="Consultar cita", command=consulta)
    btn_consultar.pack(pady=10)

    btn_cancelar = tk.Button(ventana_sesion_afiliado, text="Cancelar cita", command=cancelar)
    btn_cancelar.pack(pady=10)