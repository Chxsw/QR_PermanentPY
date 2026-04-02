print("Test Version v1A [BD] | Dinamic Code -V")
print("-" * 30)
# Imports
import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        # XAMPP + Mysql
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='qrtest',
            port=3306
        )
        return conexion
    except Error as e:
        print(f"❌ Error DB: {e}")
        return None

def obtener_ultimo_id():
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT id_unico FROM enlaces_qr WHERE id_unico LIKE 'QrDinamicVA%' ORDER BY id_unico DESC LIMIT 1")
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return resultado[0] if resultado else None
    return None

def registrar_qr_db(id_unico, url_destino):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "INSERT INTO enlaces_qr (id_unico, url_destino) VALUES (%s, %s)"
        try:
            cursor.execute(query, (id_unico, url_destino))
            conexion.commit()
            return True
        except Error as e:
            print(f"¡Error! al insertar: {e}")
        finally:
            cursor.close()
            conexion.close()
    return False