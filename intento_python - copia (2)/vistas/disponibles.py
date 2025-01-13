# vistas/disponibles.py
import tkinter as tk
from tkinter import ttk
from conexion.DAO import actualizar_cita_desde_bd, solicitar_cita_desde_bd

def abrir_ventana_disponibles(numero_documento, X1, X2, X3, X4, X5):
    documento_comodin=777777777
    def tomar_cita():
        actualizar_cita_desde_bd(numero_documento, documento_comodin,X1, X4, X5)

    ventana_disponibles = tk.Toplevel()
    ventana_disponibles.title("Citas Disponibles")
    ventana_disponibles.geometry("1800x400")

    tk.Label(ventana_disponibles, text="Citas disponibles", font=("Helvetica", 16)).pack()

    # Crear Treeview para mostrar los resultados
    tree = ttk.Treeview(ventana_disponibles, columns=("Tipo Cita", "Médico", "Especialidad", "Fecha", "Hora"))
    tree.heading("Tipo Cita", text="Tipo Cita")
    tree.heading("Médico", text="Médico")
    tree.heading("Especialidad", text="Especialidad")
    tree.heading("Fecha", text="Fecha")
    tree.heading("Hora", text="Hora")

    tree.column("#0", width=0, stretch=tk.NO) 

    tree.insert("", "end", values=(X1, X2, X3, X4, X5))
    tree.pack(expand=True, fill=tk.BOTH, padx=50)  # Ajustar padx aquí

    # Configurar el ancho de las columnas
    for col in ("Tipo Cita", "Médico", "Especialidad", "Fecha", "Hora"):
        tree.column(col, width=80, anchor="center")  # Ajustar el ancho según sea necesario

    btn_aceptar = ttk.Button(ventana_disponibles, text="Aceptar", command=tomar_cita)
    btn_aceptar.pack(side=tk.BOTTOM, anchor=tk.SW, pady=10, padx=10)