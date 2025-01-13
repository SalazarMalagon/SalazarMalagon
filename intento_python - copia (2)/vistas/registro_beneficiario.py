# vistas/registro_beneficiario.py
import tkinter as tk
from tkinter import ttk
import re
from tkinter import messagebox

from conexion.DAO import registrar_bd_beneficiario, verificar_existencia_afiliado, verificar_usuario

def abrir_ventana_registro_beneficiario ():
    def validar_fecha(fecha):
        patron = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        return bool(patron.match(fecha))
    
    def registrar_beneficiario():
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
        
        tipo_afiliacion="Beneficiario"
        tipos_documento_afiliado=combobox_tipo_documento_afiliado.get()
        if tipos_documento_afiliado=="Cedula de ciudadania":
            tipos_documento_afiliado="CC"
        if tipos_documento_afiliado=="Cedula de extranjeria":
            tipos_documento_afiliado="CE"
        if tipos_documento_afiliado=="Pasaporte":
            tipos_documento_afiliado="PT"
        if tipos_documento_afiliado=="Tarjeta de identidad":
            tipos_documento_afiliado="TI"
        numero_documento_afiliado = entry_numero_documento_afiliado.get()

        fecha_nacimiento = entry_fecha_nacimiento.get()
        if not validar_fecha(fecha_nacimiento):
            messagebox.showerror("Error", "Formato de fecha incorrecto. Debe ser YYYY-MM-DD.")
            return
        
        resultado = verificar_existencia_afiliado(tipos_documento_afiliado, numero_documento_afiliado)
        if resultado == "Exito":
            messagebox.showinfo("Información", "Afiliado encontrado en la base de datos.")
        else:
            messagebox.showinfo("Información", "Afiliado no encontrado en la base de datos.")
       
        if verificar_usuario(tipo_documento, numero_documento):
            messagebox.showinfo("Información", "Este Beneficiari ya está registrado.")
        else:
            registrar_bd_beneficiario(tipo_documento, numero_documento,nombre,sexo, fecha_nacimiento, telefono, celular, correo, categoria, tipo_afiliacion, tipos_documento_afiliado, numero_documento_afiliado)
            if registrar_bd_beneficiario=="Error":
                messagebox.showerror("No fue posible registrar al Afiliado")
        print(f"Registrando Medico: Tipo de documento={tipo_documento}, Numero de documento={numero_documento}, Nombre={nombre}, Sexo={sexo}, Fecha de Nacimiento={fecha_nacimiento}, Teléfono={telefono}, Celular={celular}, Correo={correo}")

    ventana_registro_beneficiario = tk.Toplevel()
    ventana_registro_beneficiario.title("Registrar Beneficiario")
    ventana_registro_beneficiario.geometry("400x500")

    tk.Label(ventana_registro_beneficiario, text="Registrar Beneficiario", font=("Helvetica", 16)).pack(pady=10)

    # Tipo de documento
    frame_tipo_documento = tk.Frame(ventana_registro_beneficiario)
    frame_tipo_documento.pack(pady=5)
    tk.Label(frame_tipo_documento, text="Tipo de documento:").pack(side=tk.LEFT)
    tipos_documento = ["Cedula de ciudadania", "Cedula de extranjeria", "Pasaporte", "Tarjeta de identidad"]
    combobox_tipo_documento = ttk.Combobox(frame_tipo_documento, values=tipos_documento)
    combobox_tipo_documento.pack(side=tk.LEFT)

    # Numero de documento
    frame_numero_documento = tk.Frame(ventana_registro_beneficiario)
    frame_numero_documento.pack(pady=5)
    tk.Label(frame_numero_documento, text="Numero de documento:").pack(side=tk.LEFT)
    entry_numero_documento = tk.Entry(frame_numero_documento)
    entry_numero_documento.pack(side=tk.LEFT)

    # Nombre completo
    frame_nombre = tk.Frame(ventana_registro_beneficiario)
    frame_nombre.pack(pady=5)
    tk.Label(frame_nombre, text="Nombre completo:").pack(side=tk.LEFT)
    entry_nombre = tk.Entry(frame_nombre)
    entry_nombre.pack(side=tk.LEFT)

    # Sexo
    frame_sexo = tk.Frame(ventana_registro_beneficiario)
    frame_sexo.pack(pady=5)
    tk.Label(frame_sexo, text="Sexo:").pack(side=tk.LEFT)
    sexos = ["F", "M"]
    combobox_sexo = ttk.Combobox(frame_sexo, values=sexos)
    combobox_sexo.pack(side=tk.LEFT)

    # Fecha de nacimiento
    frame_fecha_nacimiento = tk.Frame(ventana_registro_beneficiario)
    frame_fecha_nacimiento.pack(pady=5)
    tk.Label(frame_fecha_nacimiento, text="Fecha de nacimiento YYYY-MM-DD:").pack(side=tk.LEFT)
    entry_fecha_nacimiento = tk.Entry(frame_fecha_nacimiento)
    entry_fecha_nacimiento.pack(side=tk.LEFT)

    # Teléfono
    frame_telefono = tk.Frame(ventana_registro_beneficiario)
    frame_telefono.pack(pady=5)
    tk.Label(frame_telefono, text="Teléfono:").pack(side=tk.LEFT)
    entry_telefono = tk.Entry(frame_telefono)
    entry_telefono.pack(side=tk.LEFT)

    # Celular
    frame_celular = tk.Frame(ventana_registro_beneficiario)
    frame_celular.pack(pady=5)
    tk.Label(frame_celular, text="Celular:").pack(side=tk.LEFT)
    entry_celular = tk.Entry(frame_celular)
    entry_celular.pack(side=tk.LEFT)

    # Correo
    frame_correo = tk.Frame(ventana_registro_beneficiario)
    frame_correo.pack(pady=5)
    tk.Label(frame_correo, text="Correo:").pack(side=tk.LEFT)
    entry_correo = tk.Entry(frame_correo)
    entry_correo.pack(side=tk.LEFT)

    # Categoría
    frame_categoria = tk.Frame(ventana_registro_beneficiario)
    frame_categoria.pack(pady=5)
    tk.Label(frame_categoria, text="Categoría:").pack(side=tk.LEFT)
    categorias = ["A", "B", "C"]
    combobox_categoria = ttk.Combobox(frame_categoria, values=categorias)
    combobox_categoria.pack(side=tk.LEFT)

    tk.Label(ventana_registro_beneficiario, text="Afiliado", font=("Helvetica", 16)).pack(pady=10)

    frame_tipo_documento_afiliado = tk.Frame(ventana_registro_beneficiario)
    frame_tipo_documento_afiliado.pack(pady=5)
    tk.Label(frame_tipo_documento_afiliado, text="Tipo de documento:").pack(side=tk.LEFT)
    tipos_documento_afiliado = ["Cedula de ciudadania", "Cedula de extranjeria", "Pasaporte", "Tarjeta de identidad"]
    combobox_tipo_documento_afiliado = ttk.Combobox(frame_tipo_documento_afiliado, values=tipos_documento_afiliado)
    combobox_tipo_documento_afiliado.pack(side=tk.LEFT)

    frame_numero_documento_afiliado = tk.Frame(ventana_registro_beneficiario)
    frame_numero_documento_afiliado.pack(pady=5)
    tk.Label(frame_numero_documento_afiliado, text="Numero de documento:").pack(side=tk.LEFT)
    entry_numero_documento_afiliado = tk.Entry(frame_numero_documento_afiliado)
    entry_numero_documento_afiliado.pack(side=tk.LEFT)

    # Botón de registrar
    btn_registrar = tk.Button(ventana_registro_beneficiario, text="Registrar", command=registrar_beneficiario)
    btn_registrar.pack(pady=10)

    # Botón para regresar
    btn_regresar = tk.Button(ventana_registro_beneficiario, text="Regresar", command=ventana_registro_beneficiario.destroy)
    btn_regresar.pack(side=tk.BOTTOM, anchor=tk.SW, pady=10, padx=10)