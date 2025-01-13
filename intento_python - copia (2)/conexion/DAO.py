# conexion/DAO.py
from tkinter import messagebox
import psycopg2
from datetime import datetime, time

def conectar_bd():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            port=5432,
            user="postgres",
            password="1234",
            database="intento2"
        )
        print("Conexión a la base de datos exitosa.")
        return conexion
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def cerrar_conexion(conexion):
    if conexion:
        conexion.close()
        print("Conexión cerrada.")

def cargar_especialidades_desde_bd():
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT n_nombre FROM Especialidad")
            especialidades = [fila[0] for fila in cursor.fetchall()]
            return especialidades
        
    except Exception as e:
        print(f"Error al cargar especialidades desde la base de datos: {e}")

def cargar_sedes_desde_bd():
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT k_sede, n_nombre FROM Sede;")
            sedes = [fila[0] for fila in cursor.fetchall()]
            return sedes

    except Exception as e:
        print(f"Error al cargar sedes desde la base de datos: {e}")
        return []

def cargar_nombre_tipos_de_cita_desde_bd():
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT n_nombre FROM Tipo_de_cita;")
            tipos_de_cita = [fila[0] for fila in cursor.fetchall()]
            return tipos_de_cita

    except Exception as e:
        print(f"Error al cargar tipos de cita desde la base de datos: {e}")
        return []

def verificar_usuario(tipo_documento, numero_documento):
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Usuario WHERE k_tipodocumento = %s AND k_numerodocumento = %s",
                           (tipo_documento, numero_documento))
            usuario = cursor.fetchone()  

            if usuario:
                cursor.execute("SELECT k_tipodocumento FROM Medico WHERE k_tipodocumento = %s AND k_numerodocumento = %s",
                               (tipo_documento, numero_documento))
                medico = cursor.fetchone()
                
                cursor.execute("SELECT k_tipodocumento FROM Afiliado_Beneficiario WHERE k_tipodocumento = %s AND k_numerodocumento = %s",
                               (tipo_documento, numero_documento))
                afiliado_beneficiario = cursor.fetchone()

                if medico:
                    return "Medico"
                elif afiliado_beneficiario:
                    return "Afiliado/Beneficiario"

    except Exception as e:
        print(f"Error al verificar usuario en la base de datos: {e}")
        return None


def registrar_bd_medico(tipo_documento, numero_documento,nombre,sexo, fecha_nacimiento, telefono, celular, correo, registro_medico):
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()

            cursor.execute("INSERT INTO Usuario VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                            (tipo_documento, numero_documento, nombre, sexo, fecha_nacimiento, telefono, celular, correo))

            cursor.execute("INSERT INTO Medico VALUES (%s, %s, %s)",
                            (tipo_documento, numero_documento, registro_medico))

            conexion.commit()
            messagebox.showinfo("Información","Médico registrado con éxito.")
    
    except Exception as e:
        print(f"Error al registrar el médico en la base de datos: {e}")
        return "Error"

def registrar_bd_afiliado(tipo_documento, numero_documento,nombre,sexo, fecha_nacimiento, telefono, celular, correo, categoria, tipo_afiliacion, tipo_documento_afiliado, numero_documento_afilliado):
    estado="Activo"
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()

            cursor.execute("INSERT INTO Usuario VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                            (tipo_documento, numero_documento, nombre, sexo, fecha_nacimiento, telefono, celular, correo))

            cursor.execute("INSERT INTO afiliado_beneficiario VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (tipo_documento, numero_documento, tipo_afiliacion, estado, tipo_documento_afiliado, numero_documento_afilliado, categoria))

            conexion.commit()
            messagebox.showinfo("Información","Afiliado registrado con éxito.")
    
    except Exception as e:
        print(f"Error al registrar el Afiliado en la base de datos: {e}")
        return "Error"

def verificar_existencia_afiliado(tipo_documento_afiliado, numero_documento_afiliado):
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Afiliado_Beneficiario WHERE k_tipodocumento = %s AND k_numerodocumento = %s",
                           (tipo_documento_afiliado, numero_documento_afiliado))
            afiliado = cursor.fetchone()

            if afiliado:
                return "Exito"
            else:
                return None

    except Exception as e:
        print(f"Error al verificar afiliado en la base de datos: {e}")
        return None
    
def registrar_bd_beneficiario(tipo_documento, numero_documento,nombre,sexo, fecha_nacimiento, telefono, celular, correo, categoria, tipo_afiliacion, tipos_documento_afiliado, numero_documento_afiliado):
    estado="Activo"
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()

            cursor.execute("INSERT INTO Usuario VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                            (tipo_documento, numero_documento, nombre, sexo, fecha_nacimiento, telefono, celular, correo))

            cursor.execute("INSERT INTO afiliado_beneficiario VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (tipo_documento, numero_documento, tipo_afiliacion, estado, tipos_documento_afiliado, numero_documento_afiliado, categoria))

            conexion.commit()
            messagebox.showinfo("Información","Beneficiario registrado con éxito.")
    
    except Exception as e:
        print(f"Error al registrar el Beneficiario en la base de datos: {e}")
        return "Error"


def registrar_bd_agenda(tipos_documento, numero_documento, agenda, mes, año):
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()

            cursor.execute("INSERT INTO Agenda VALUES (%s, %s, %s, %s, %s)",
                            (tipos_documento, numero_documento, agenda, mes, año))
            
            conexion.commit()
            messagebox.showinfo("Información", "Agenda registrada con éxito.")
    
    except Exception as e:
        print(f"db_a_Error al registrar la agenda en la base de datos: {e}")
        return "Error"
    
def registrar_bd_cita(id_cita, tipos_cita, hora_inicio_str, hora_final_str, fecha_obj, disponibilidad, tipos_documento_predeterminado, numero_documento_predeterminado, agenda, tipos_documento, numero_documento):
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()

            cursor.execute("INSERT INTO cita VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                            (id_cita, tipos_cita, hora_inicio_str, hora_final_str, fecha_obj, disponibilidad, tipos_documento_predeterminado, numero_documento_predeterminado, agenda, tipos_documento, numero_documento))
            
            conexion.commit()
            print("Datos subido a citas")
    
    except Exception as e:
        print(f"db_c_Error al registrar la agenda en la base de datos: {e}")
        return "Error"
    

def consultar_citas_paciente(numero_documento,fecha_consulta_obj):
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('SELECT cita.k_idcita, cita.h_inicial, cita.h_final, cita.f_cita, cita.k_pacienteNumeroDocumento, usuario.n_nombre FROM cita JOIN usuario ON cita.k_medicotipodocumento = usuario.k_tipodocumento AND cita.k_mediconumerodocumento = usuario.k_numerodocumento WHERE cita.k_pacienteNumeroDocumento = %s AND cita.f_cita = %s;',
                           (numero_documento,fecha_consulta_obj))
            consultar_cita = cursor.fetchone()

            if consultar_cita:

                cita_dict = {
                    "Codigo de la cita": consultar_cita[0],
                    "Hora de inicio": consultar_cita[1],
                    "Fecha de la cita": consultar_cita[3],
                    "Numero de documento paciente": consultar_cita[4],
                    "Nombre del doctor": consultar_cita[5]
                }
                info_texto = "\n".join([f"{key}: {value}" for key, value in sorted(cita_dict.items())])
                messagebox.showinfo("Información de la Cita", info_texto)
            else:
                messagebox.showinfo("Información", "No tiene citas")

    except Exception as e:
        print(f"Error al verificar afiliado en la base de datos: {e}")
        return None
    
def cancelar_citas_paciente(numero_documento, fecha_consulta_obj, hora_consulta_obj):
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()

            hora_consulta_str = hora_consulta_obj.strftime('%H:%M:%S')

            cursor.execute('DELETE FROM cita WHERE cita.k_pacientenumerodocumento = %s AND cita.f_cita = %s AND cita.h_inicial = %s;',
                           (numero_documento, fecha_consulta_obj, hora_consulta_str))
            conexion.commit()
            messagebox.showinfo(f"Informacion",f"Se elimino correctamente su cita de la fecha: {fecha_consulta_obj}")

    except Exception as e:
        print(f"Error al verificar afiliado en la base de datos: {e}")
        return None
    
def medico_especialidad_asignacion(numero_documento, fecha_consulta_obj, hora_consulta_obj):
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()

            hora_consulta_str = hora_consulta_obj.strftime('%H:%M:%S')

            cursor.execute('DELETE FROM cita WHERE cita.k_pacientenumerodocumento = %s AND cita.f_cita = %s AND cita.h_inicial = %s;',
                           (numero_documento, fecha_consulta_obj, hora_consulta_str))
            conexion.commit()
            messagebox.showinfo(f"Informacion",f"Se elimino correctamente su cita de la fecha: {fecha_consulta_obj}")

    except Exception as e:
        print(f"Error al verificar afiliado en la base de datos: {e}")
        return None
    
def cargar_sedes_desde_bd():
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT n_nombre FROM sede")
            sede = [fila[0] for fila in cursor.fetchall()]
            return sede
        
    except Exception as e:
        print(f"Error al cargar especialidades desde la base de datos: {e}")


def consultar_sedes_insertar(especialidad_medico_asignacion,tipo_documento, numero_documento, consultorio, sede_asignacion, horario_aleatorio):
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()

            cursor.execute("INSERT INTO especialidad_medico_consultorio VALUES (%s, %s, %s, %s, %s, %s)",
                            (especialidad_medico_asignacion,tipo_documento, numero_documento, consultorio, sede_asignacion, horario_aleatorio))
            
            conexion.commit()
            print("Datos subido a citas")
    
    except Exception as e:
        print(f"db_c_Error al registrar la agenda en la base de datos: {e}")
        return "Error"


def solicitar_cita_desde_bd(especialidades, tipo_cita, estado_cita):
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()

            cursor.execute("SELECT tipo_de_cita.n_nombre, usuario.n_nombre, especialidad.n_nombre, cita.f_cita, cita.h_inicial FROM cita FULL OUTER JOIN tipo_de_cita on cita.k_tipodecita = tipo_de_cita.k_tipodecita FULL OUTER JOIN especialidad_medico_consultorio ON cita.k_mediconumerodocumento = especialidad_medico_consultorio.k_numerodocumento FULL OUTER JOIN usuario ON cita.k_mediconumerodocumento = usuario.k_numerodocumento JOIN especialidad on especialidad.k_especialidad=especialidad_medico_consultorio.k_especialidad WHERE especialidad_medico_consultorio.k_especialidad=%s  AND cita.k_tipodecita= %s AND cita.n_estado = %s",
                            (especialidades, tipo_cita, estado_cita))
            solicitar_datos = cursor.fetchone()

            if solicitar_datos:
                X1=solicitar_datos[0]
                X2=solicitar_datos[1]
                X3=solicitar_datos[2]
                X4=solicitar_datos[3]
                X5=solicitar_datos[4]
            return X1, X2, X3, X4, X5 

        
    except Exception as e:
        print(f"scdb Error al registrar la agenda en la base de datos: {e}")
        return "Error"
    
def actualizar_cita_desde_bd(numero_documento, documento_comodin,X1, X4, X5):
    if X1=="Proriotaria":
        X1=1
    if X1=="Primera vez":
        X1=2
    if X1=="Control":
        X1=3
    if X1=="Lectura exámenes":
        X1=4
    try:
        conexion = conectar_bd()
        if conexion:
            cursor = conexion.cursor()

            cursor.execute("UPDATE cita SET k_pacientenumerodocumento = %s WHERE cita.k_pacientenumerodocumento = %s AND cita.k_tipodecita=%s AND cita.f_cita=%s AND cita.h_inicial = %s",
                            (numero_documento, documento_comodin, X1,X4, X5))
            conexion.commit()
            messagebox.showinfo(f"Informacion",f"Cita asignada")
        
    except Exception as e:
        print(f"scdb Error al registrar la agenda en la base de datos: {e}")
        return "Error"
    