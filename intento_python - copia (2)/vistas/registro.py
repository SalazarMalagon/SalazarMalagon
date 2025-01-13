# vistas/registro.py
import tkinter as tk
from vistas.registro_afiliado import abrir_ventana_registro_afiliado
from vistas.registro_beneficiario import abrir_ventana_registro_beneficiario
from vistas.registro_medico import abrir_ventana_registro_medico

def abrir_ventana_registro():
    ventana_registro = tk.Toplevel()
    ventana_registro.title("EPS Formulacion - Registro")
    ventana_registro.geometry("550x150")

    tk.Label(ventana_registro, text="Iniciar sesión", font=("Helvetica", 16)).pack()

    btn_medico = tk.Button(ventana_registro, text="enfermero", command=abrir_ventana_registro_medico)
    btn_medico.pack(pady=5)

    btn_afiliado = tk.Button(ventana_registro, text="Afiliado", command=abrir_ventana_registro_afiliado)
    btn_afiliado.pack(pady=5)

    btn_afiliado = tk.Button(ventana_registro, text="Beneficiario", command=abrir_ventana_registro_beneficiario)
    btn_afiliado.pack(pady=5)

    btn_regresar = tk.Button(ventana_registro, text="Regresar", command=ventana_registro.destroy)
    btn_regresar.pack(side=tk.BOTTOM, anchor=tk.SW, pady=10, padx=10)

    def registrar_usuario(tipo_usuario):
        print(f"Registrando usuario como {tipo_usuario}")