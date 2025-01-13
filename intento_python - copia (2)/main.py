# main.py
from vistas.inicio import crear_ventana
from conexion.DAO import conectar_bd, cerrar_conexion

def main():
    conexion_bd = conectar_bd()

    if conexion_bd:
        print("Conexión a la base de datos exitosa.")
    else:
        print("No se pudo establecer la conexión a la base de datos. Saliendo.")
        return

    ventana = crear_ventana()

    ventana.mainloop()

    cerrar_conexion(conexion_bd)

if __name__ == "__main__":
    main()
