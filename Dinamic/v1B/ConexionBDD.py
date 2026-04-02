print("Test Version v1B [BD] | Dinamic Code -V")
print("-" * 30)
# Imports
import mysql.connector
from mysql.connector import Error

# Conexion a la base de datos local
# XAMPP + MySql
# Resguardo Local + TinyUrl
def obtener_conexion():
    try:
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='qrtest02',
            port=3306
        )
    except Error as e:
        print(f"¡Error! DB: {e}")
        return None

def obtener_ultimo_id_v2():
    db = obtener_conexion()
    if db:
        cursor = db.cursor()
        cursor.execute("SELECT id_unico FROM enlaces_qrV2 WHERE id_unico LIKE 'QrDinamicVB%' ORDER BY id_unico DESC LIMIT 1")
        res = cursor.fetchone()
        cursor.close()
        db.close()
        return res[0] if res else None
    return None

def registrar_qr_v2(id_id, alias, url_final):
    db = obtener_conexion()
    if db:
        try:
            cursor = db.cursor()
            query = "INSERT INTO enlaces_qrV2 (id_unico, alias_proyecto, url_destino) VALUES (%s, %s, %s)"
            cursor.execute(query, (id_id, alias, url_final))
            db.commit()
            cursor.close()
            db.close()
            return True
        except Error as e:
            print(f"¡Error! al insertar: {e}")
    return False

def listar_qrs_locales():
    db = obtener_conexion()
    if db:
        cursor = db.cursor()
        cursor.execute("SELECT id_unico, url_destino FROM enlaces_qrV2")
        registros = cursor.fetchall()
        db.close()
        return registros
    return []

def update_db_local(id_id, nueva_url):
    db = obtener_conexion()
    if db:
        cursor = db.cursor()
        cursor.execute("UPDATE enlaces_qrV2 SET url_destino = %s WHERE id_unico = %s", (nueva_url, id_id))
        db.commit()
        db.close()
        return True
    return False

def eliminar_qr_local(id_id):
    db = obtener_conexion()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute("DELETE FROM enlaces_qrV2 WHERE id_unico = %s", (id_id,))
            db.commit()
            cursor.close()
            db.close()
            return True
        except Exception as e:
            print(f"¡Error! al eliminar localmente: {e}")
    return False