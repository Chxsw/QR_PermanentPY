print("Test Version v1A [Flask] | Dinamic Code -V")
print("-" * 30)

from flask import Flask, redirect
from ConexionBD import obtener_conexion

app = Flask(__name__)

@app.route('/go/<id_qr>')
def redireccionar(id_qr):
    print(f"📱 Escaneo detectado para: {id_qr}")
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT url_destino FROM enlaces_qr WHERE id_unico = %s", (id_qr,))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()

        if resultado:
            return redirect(resultado[0])
    
    return "ID no encontrado", 404

if __name__ == '__main__':
    # host='0.0.0.0' es lo que permite que el celular entre a tu PC
    print("\n--- Servidor Puente Activo ---")
    app.run(host='0.0.0.0', port=5000)