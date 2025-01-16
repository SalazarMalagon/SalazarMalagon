# vistas/registro_afiliado.py
import tkinter as tk
from tkinter import ttk
import re
from tkinter import messagebox

from conexion.DAO import registrar_bd_afiliado, verificar_usuario

def abrir_ventana_registro_afiliado ():
    def validar_fecha(fecha):
        patron = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        return bool(patron.match(fecha))
    
    def registrar_afiliado():
        tipo_documento = combobox_tipo_documento.get()

        if tipo_documento=="Cedula de ciudadania":
            tipo_documento="CC"
        if tipo_documento=="Cedula de extranjeria":
            tipo_documento="CE"
        if tipo_documento=="Pasaporte":
            tipo_documento="PT"
        if tipo_documento=="Tarjeta de identidad":
            tipo_documento="TI"
            
        numero_documento = entry_numero_documento.get()
        nombre = entry_nombre.get()
        sexo = combobox_sexo.get()
        telefono = entry_telefono.get()
        celular = entry_celular.get()
        correo = entry_correo.get()
        categoria = combobox_categoria.get()
        if categoria=="A":
            categoria=1
        if categoria=="B":
            categoria=2
        if categoria=="C":
            categoria=3
            
        tipo_afiliacion="Afiliado"
        tipo_documento_afiliado= None
        numero_documento_afilliado= None

        fecha_nacimiento = entry_fecha_nacimiento.get()
        if not validar_fecha(fecha_nacimiento):
            messagebox.showerror("Error", "Formato de fecha incorrecto. Debe ser YYYY-MM-DD.")
            return

        if verificar_usuario(tipo_documento, numero_documento):
            messagebox.showinfo("Información", "Este afiliado ya está registrado.")
        else:
            registrar_bd_afiliado(tipo_documento, numero_documento,nombre,sexo, fecha_nacimiento, telefono, celular, correo, categoria, tipo_afiliacion, tipo_documento_afiliado, numero_documento_afilliado)
            if registrar_bd_afiliado=="Error":
                messagebox.showerror("No fue posible registrar al Afiliado")

        print(f"Registrando Afiliado: Tipo de documento={tipo_documento}, Numero de documento={numero_documento}, Nombre={nombre}, Sexo={sexo}, Fecha de Nacimiento={fecha_nacimiento}, Teléfono={telefono}, Celular={celular}, Correo={correo}")

    ventana_registro_afiliado = tk.Toplevel()
    ventana_registro_afiliado.title("Registrar Afiliado")
    ventana_registro_afiliado.geometry("400x500")

    tk.Label(ventana_registro_afiliado, text="Registrar Afiliado", font=("Helvetica", 16)).pack(pady=10)

    # Tipo de documento
    frame_tipo_documento = tk.Frame(ventana_registro_afiliado)
    frame_tipo_documento.pack(pady=5)
    tk.Label(frame_tipo_documento, text="Tipo de documento:").pack(side=tk.LEFT)
    tipos_documento = ["Cedula de ciudadania", "Cedula de extranjeria", "Pasaporte", "Tarjeta de identidad"]
    combobox_tipo_documento = ttk.Combobox(frame_tipo_documento, values=tipos_documento)
    combobox_tipo_documento.pack(side=tk.LEFT)

    # Numero de documento
    frame_numero_documento = tk.Frame(ventana_registro_afiliado)
    frame_numero_documento.pack(pady=5)
    tk.Label(frame_numero_documento, text="Numero de documento:").pack(side=tk.LEFT)
    entry_numero_documento = tk.Entry(frame_numero_documento)
    entry_numero_documento.pack(side=tk.LEFT)

    # Nombre completo
    frame_nombre = tk.Frame(ventana_registro_afiliado)
    frame_nombre.pack(pady=5)
    tk.Label(frame_nombre, text="Nombre completo:").pack(side=tk.LEFT)
    entry_nombre = tk.Entry(frame_nombre)
    entry_nombre.pack(side=tk.LEFT)

    # Sexo
    frame_sexo = tk.Frame(ventana_registro_afiliado)
    frame_sexo.pack(pady=5)
    tk.Label(frame_sexo, text="Sexo:").pack(side=tk.LEFT)
    sexos = ["F", "M"]
    combobox_sexo = ttk.Combobox(frame_sexo, values=sexos)
    combobox_sexo.pack(side=tk.LEFT)

    # Fecha de nacimiento
    frame_fecha_nacimiento = tk.Frame(ventana_registro_afiliado)
    frame_fecha_nacimiento.pack(pady=5)
    tk.Label(frame_fecha_nacimiento, text="Fecha de nacimiento YYYY-MM-DD:").pack(side=tk.LEFT)
    entry_fecha_nacimiento = tk.Entry(frame_fecha_nacimiento)
    entry_fecha_nacimiento.pack(side=tk.LEFT)

    # Teléfono
    frame_telefono = tk.Frame(ventana_registro_afiliado)
    frame_telefono.pack(pady=5)
    tk.Label(frame_telefono, text="Teléfono:").pack(side=tk.LEFT)
    entry_telefono = tk.Entry(frame_telefono)
    entry_telefono.pack(side=tk.LEFT)

    # Celular
    frame_celular = tk.Frame(ventana_registro_afiliado)
    frame_celular.pack(pady=5)
    tk.Label(frame_celular, text="Celular:").pack(side=tk.LEFT)
    entry_celular = tk.Entry(frame_celular)
    entry_celular.pack(side=tk.LEFT)

    # Correo
    frame_correo = tk.Frame(ventana_registro_afiliado)
    frame_correo.pack(pady=5)
    tk.Label(frame_correo, text="Correo:").pack(side=tk.LEFT)
    entry_correo = tk.Entry(frame_correo)
    entry_correo.pack(side=tk.LEFT)

    # Categoría
    frame_categoria = tk.Frame(ventana_registro_afiliado)
    frame_categoria.pack(pady=5)
    tk.Label(frame_categoria, text="Categoría:").pack(side=tk.LEFT)
    categorias = ["A", "B", "C"]
    combobox_categoria = ttk.Combobox(frame_categoria, values=categorias)
    combobox_categoria.pack(side=tk.LEFT)

    # Botón de registrar
    btn_registrar = tk.Button(ventana_registro_afiliado, text="Registrar", command=registrar_afiliado)
    btn_registrar.pack(pady=10)

    # Botón para regresar
    btn_regresar = tk.Button(ventana_registro_afiliado, text="Regresar", command=ventana_registro_afiliado.destroy)
    btn_regresar.pack(side=tk.BOTTOM, anchor=tk.SW, pady=10, padx=10)