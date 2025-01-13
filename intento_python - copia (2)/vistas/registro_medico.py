# vistas/registro_medico.py
import tkinter as tk
from tkinter import ttk
import re
from tkinter import messagebox
import random

from conexion.DAO import cargar_especialidades_desde_bd, cargar_sedes_desde_bd, consultar_sedes_insertar, registrar_bd_medico, verificar_usuario

def abrir_ventana_registro_medico():
    numero_aleatorio = random.randint(10000, 99999)
    num_consultorio_sede_ale=random.randint(1, 5)

    def validar_fecha(fecha):
        patron = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        return bool(patron.match(fecha))

    def registrar_medico():
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
        registro_medico = 'M' + str(numero_aleatorio)

        fecha_nacimiento = entry_fecha_nacimiento.get()
        if not validar_fecha(fecha_nacimiento):
            messagebox.showerror("Error", "Formato de fecha incorrecto. Debe ser YYYY-MM-DD.")
            return

        if verificar_usuario(tipo_documento, numero_documento):
            messagebox.showinfo("Información", "El médico ya está registrado.")
        else:
            registrar_bd_medico(tipo_documento, numero_documento,nombre,sexo, fecha_nacimiento, telefono, celular, correo, registro_medico)
            if registrar_bd_medico=="Error":
                messagebox.showerror("No fue posible registrar al Médico")

        especialidad_medico_asignacion=combobox_especialidad_medico_asignacion.get()
        if especialidad_medico_asignacion=="Cardiología":
            especialidad_medico_asignacion=1
        if especialidad_medico_asignacion=="Dermatología":
            especialidad_medico_asignacion=2
        if especialidad_medico_asignacion=="Gastroenterología":
            especialidad_medico_asignacion=3
        if especialidad_medico_asignacion=="Neurología":
            especialidad_medico_asignacion=4
        if especialidad_medico_asignacion=="Oftalmología":
            especialidad_medico_asignacion=5
        if especialidad_medico_asignacion=="Ortopedia":
            especialidad_medico_asignacion=6
        if especialidad_medico_asignacion=="Pediatría":
            especialidad_medico_asignacion=7
        if especialidad_medico_asignacion=="Psiquiatría":
            especialidad_medico_asignacion=8
        if especialidad_medico_asignacion=="Radiología":
            especialidad_medico_asignacion=9
        if especialidad_medico_asignacion=="Urología":
            especialidad_medico_asignacion=10

        sede_asignacion=combobox_sede_asignacion.get()
        if sede_asignacion=="Sede A":
            sede_asignacion=1
            consultorio_ale='10' + str(num_consultorio_sede_ale)
            consultorio= int(consultorio_ale)
        if sede_asignacion=="Sede B":
            sede_asignacion=2
            consultorio_ale='20' + str(num_consultorio_sede_ale)
            consultorio= int(consultorio_ale)
        if sede_asignacion=="Sede C":
            sede_asignacion=3
            consultorio_ale='30' + str(num_consultorio_sede_ale)
            consultorio= int(consultorio_ale)
        if sede_asignacion=="Sede D":
            sede_asignacion=4
            consultorio_ale='40' + str(num_consultorio_sede_ale)
            consultorio= int(consultorio_ale)
        if sede_asignacion=="Sede E":
            sede_asignacion=5
            consultorio_ale='50' + str(num_consultorio_sede_ale)
            consultorio= int(consultorio_ale)
        if sede_asignacion=="Sede F":
            sede_asignacion=6
            consultorio_ale='60' + str(num_consultorio_sede_ale)
            consultorio= int(consultorio_ale)
        if sede_asignacion=="Sede G":
            sede_asignacion=7
            consultorio_ale='70' + str(num_consultorio_sede_ale)
            consultorio= int(consultorio_ale)
        if sede_asignacion=="Sede H":
            sede_asignacion=8
            consultorio_ale='80' + str(num_consultorio_sede_ale)
            consultorio= int(consultorio_ale)
        if sede_asignacion=="Sede I":
            sede_asignacion=9
            consultorio_ale='90' + str(num_consultorio_sede_ale)
            consultorio= int(consultorio_ale)
        if sede_asignacion=="Sede J":
            sede_asignacion=10
            consultorio_ale='100' + str(num_consultorio_sede_ale)
            consultorio= int(consultorio_ale)
        horario_tarde_manana=["Mañana","Tarde"]
        horario_aleatorio=random.choice(horario_tarde_manana)
        consultar_sedes_insertar(especialidad_medico_asignacion,tipo_documento, numero_documento, consultorio, sede_asignacion, horario_aleatorio)
        
        print(f"Registrando Medico: Tipo de documento={tipo_documento}, Numero de documento={numero_documento}, Nombre={nombre}, Sexo={sexo}, Fecha de Nacimiento={fecha_nacimiento}, Teléfono={telefono}, Celular={celular}, Correo={correo}")

    ventana_registro_medico = tk.Toplevel()
    ventana_registro_medico.title("Registrar Enfermero")
    ventana_registro_medico.geometry("400x500")

    tk.Label(ventana_registro_medico, text="Registrar Enfermero", font=("Helvetica", 16)).pack(pady=10)

    # Tipo de documento
    frame_tipo_documento = tk.Frame(ventana_registro_medico)
    frame_tipo_documento.pack(pady=5)
    tk.Label(frame_tipo_documento, text="Tipo de documento:").pack(side=tk.LEFT)
    tipos_documento = ["Cedula de ciudadania", "Cedula de extranjeria", "Pasaporte", "Tarjeta de identidad"]
    combobox_tipo_documento = ttk.Combobox(frame_tipo_documento, values=tipos_documento)
    combobox_tipo_documento.pack(side=tk.LEFT)

    # Numero de documento
    frame_numero_documento = tk.Frame(ventana_registro_medico)
    frame_numero_documento.pack(pady=5)
    tk.Label(frame_numero_documento, text="Numero de documento:").pack(side=tk.LEFT)
    entry_numero_documento = tk.Entry(frame_numero_documento)
    entry_numero_documento.pack(side=tk.LEFT)

    # Nombre completo
    frame_nombre = tk.Frame(ventana_registro_medico)
    frame_nombre.pack(pady=5)
    tk.Label(frame_nombre, text="Nombre completo:").pack(side=tk.LEFT)
    entry_nombre = tk.Entry(frame_nombre)
    entry_nombre.pack(side=tk.LEFT)

    # Sexo
    frame_sexo = tk.Frame(ventana_registro_medico)
    frame_sexo.pack(pady=5)
    tk.Label(frame_sexo, text="Sexo:").pack(side=tk.LEFT)
    sexos = ["F", "M"]
    combobox_sexo = ttk.Combobox(frame_sexo, values=sexos)
    combobox_sexo.pack(side=tk.LEFT)

    # Fecha de nacimiento
    frame_fecha_nacimiento = tk.Frame(ventana_registro_medico)
    frame_fecha_nacimiento.pack(pady=5)
    tk.Label(frame_fecha_nacimiento, text="Fecha de nacimiento YYYY-MM-DD:").pack(side=tk.LEFT)
    entry_fecha_nacimiento = tk.Entry(frame_fecha_nacimiento)
    entry_fecha_nacimiento.pack(side=tk.LEFT)

    # Teléfono
    frame_telefono = tk.Frame(ventana_registro_medico)
    frame_telefono.pack(pady=5)
    tk.Label(frame_telefono, text="Teléfono:").pack(side=tk.LEFT)
    entry_telefono = tk.Entry(frame_telefono)
    entry_telefono.pack(side=tk.LEFT)

    # Celular
    frame_celular = tk.Frame(ventana_registro_medico)
    frame_celular.pack(pady=5)
    tk.Label(frame_celular, text="Celular:").pack(side=tk.LEFT)
    entry_celular = tk.Entry(frame_celular)
    entry_celular.pack(side=tk.LEFT)

    # Correo
    frame_correo = tk.Frame(ventana_registro_medico)
    frame_correo.pack(pady=5)
    tk.Label(frame_correo, text="Correo:").pack(side=tk.LEFT)
    entry_correo = tk.Entry(frame_correo)
    entry_correo.pack(side=tk.LEFT)

    # Especialidad
    frame_especialidad_medico_asignacion = tk.Frame(ventana_registro_medico)
    frame_especialidad_medico_asignacion.pack(pady=5)
    tk.Label(frame_especialidad_medico_asignacion, text="Especialidad:").pack(side=tk.LEFT, padx=5)
    especialidades = cargar_especialidades_desde_bd()
    combobox_especialidad_medico_asignacion = ttk.Combobox(frame_especialidad_medico_asignacion, values=especialidades)
    combobox_especialidad_medico_asignacion.pack(side=tk.LEFT, padx=5)

    #Sede
    frame_sede_asignacion = tk.Frame(ventana_registro_medico)
    frame_sede_asignacion.pack(pady=5)
    tk.Label(frame_sede_asignacion, text="Sede:").pack(side=tk.LEFT, padx=5)
    sede = cargar_sedes_desde_bd()
    combobox_sede_asignacion = ttk.Combobox(frame_sede_asignacion, values=sede)
    combobox_sede_asignacion.pack(side=tk.LEFT, padx=5)
    
    # Botón de registrar
    btn_registrar = tk.Button(ventana_registro_medico, text="Registrar", command=registrar_medico)
    btn_registrar.pack(pady=10)

    # Botón para regresar
    btn_regresar = tk.Button(ventana_registro_medico, text="Regresar", command=ventana_registro_medico.destroy)
    btn_regresar.pack(side=tk.BOTTOM, anchor=tk.SW, pady=10, padx=10)