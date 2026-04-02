print("Test Version v1A | Dinamic Code -V")
print("-" * 30)
# Imports
import qrcode
import os
import webbrowser
import socket
from ConexionBD import obtener_ultimo_id, registrar_qr_db

# Función para detectar tu IP local
def obtener_ip_local():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

#  Generar ID incremental
ultimo_id = obtener_ultimo_id()
if ultimo_id:
    numero = int(ultimo_id.replace("QrDinamicVA", ""))
    id_generado = f"QrDinamicVA{numero + 1:02d}"
else:
    id_generado = "QrDinamicVA00"

print(f"ID Autogenerado: {id_generado}")
url_destino = input("Ingresa la URL de destino final: ")

#  Crear puente local
mi_ip = obtener_ip_local()
url_puente = f"http://{mi_ip}:5000/go/{id_generado}"

#  Registrar en MySQL y generar imagen
if registrar_qr_db(id_generado, url_destino):
    ruta_carpeta = os.path.join(os.path.expanduser("~"), "Desktop", "QR_FY")
    ruta_completa = os.path.join(ruta_carpeta, f"{id_generado}.png")
    os.makedirs(ruta_carpeta, exist_ok=True)

    # El QR ahora contiene la IP de tu PC, no un dominio externo
    qr = qrcode.make(url_puente)
    qr.save(ruta_completa)
    print(f"El QR apunta localmente a: {url_puente}")
    webbrowser.open(ruta_completa)
else:
    print("¡Error! al registrar en Base de Datos.")

input("\nEnter para finalizar!")