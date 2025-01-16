# vistas/inicio.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from conexion.DAO import verificar_usuario
from vistas.registro import abrir_ventana_registro
from vistas.sesion_afiliado import abrir_ventana_sesion_afiliado
from vistas.sesion_medico import abrir_ventana_sesion_medico


def crear_ventana():
    def inicio():
        tipos_documento = combobox_documento.get()
        if tipos_documento=="Cedula de ciudadania":
            tipos_documento="CC"
        if tipos_documento=="Cedula de extranjeria":
            tipos_documento="CE"
        if tipos_documento=="Pasaporte":
            tipos_documento="PT"
        if tipos_documento=="Tarjeta de identidad":
            tipos_documento="TI"
        
        numero_documento=entry_numero_documento.get()           
        tipos_usuario = combobox_usuario.get()

        tipo_usuario_verificacion = verificar_usuario(tipos_documento, numero_documento)
        if tipos_usuario == tipo_usuario_verificacion:
            print(f"Usuario encontrado. Iniciando sesión como {tipos_usuario}.")
            if tipos_usuario == "Medico":
                abrir_ventana_sesion_medico(tipos_documento, numero_documento)
            elif tipos_usuario == "Afiliado/Beneficiario":
                abrir_ventana_sesion_afiliado(tipos_documento, numero_documento)
        else:
            print("Usuario no encontrado.")
            messagebox.showerror("Error", "No ha sido posible encontrar su cuenta \nverifique todos los campos sean correcto")
            

        print(f"Documento{tipos_documento} usuario{tipos_usuario} numero{numero_documento}")
        


    ventana = tk.Tk()
    ventana.title("EPS Formulacion")
    ventana.geometry("550x300")

    frame_encabezado = tk.Frame(ventana)
    frame_encabezado.pack(pady=10) 

    tk.Label(frame_encabezado, text="Iniciar sesión", font=("Helvetica", 16)).pack()

    frame_documento = tk.Frame(ventana)
    frame_documento.pack(pady=10)

    tk.Label(frame_documento, text="Tipo de documento:").pack(side=tk.LEFT, padx=5) 
    tipos_documento = ["Cedula de ciudadania", "Cedula de extranjeria", "Pasaporte", "Tarjeta de identidad"]
    combobox_documento = ttk.Combobox(frame_documento, values=tipos_documento)
    combobox_documento.pack(side=tk.LEFT, padx=5)

    frame_usuario = tk.Frame(ventana)
    frame_usuario.pack(pady=10)

    tk.Label(frame_usuario, text="Tipo de usuario:").pack(side=tk.LEFT, padx=5)
    tipos_usuario = ["Medico", "Afiliado/Beneficiario"]
    combobox_usuario = ttk.Combobox(frame_usuario, values=tipos_usuario)
    combobox_usuario.pack(side=tk.LEFT, padx=5)

    frame_numero_documento = tk.Frame(ventana)
    frame_numero_documento.pack(pady=10)

    tk.Label(frame_numero_documento, text="Número de documento:").pack(side=tk.LEFT, padx=5)
    entry_numero_documento = tk.Entry(frame_numero_documento)
    entry_numero_documento.pack(side=tk.LEFT, padx=5)

    btn_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión", command=inicio)
    btn_iniciar_sesion.pack(pady=10)

    # Botón de registrar
    btn_registrar = tk.Button(ventana, text="Registrar", command=abrir_ventana_registro)
    btn_registrar.pack(pady=10)

    # Botón para salir
    btn_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
    btn_salir.pack(side=tk.BOTTOM, anchor=tk.SW, pady=10, padx=10)

    return ventana

