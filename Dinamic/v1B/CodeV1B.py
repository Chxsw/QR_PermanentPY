print("Test Version v1B | Dinamic Code -V")
print("-" * 30)
# Imports
import qrcode
import os
import requests

# La API Obtenida, fue generada con una cuenta gratuita por lo que
# existe la posibilidad de que al mejorar la cuenta, algunas opciones
# funcionen correctamente y/o mejor de lo que esta codificado (en el presente script)
API_TOKEN = "--Api--" # tinyurl.com | Registrarse + generar Api


def crear_en_nube(url_final, id_sugerido):
    headers = {"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"}
    # Identificador general f-qr-id_sugerido || Id_sugerido = id incremental
    alias_unico = f"v-qr-{id_sugerido.lower()}"
    payload = {"url": url_final, "domain": "tinyurl.com", "alias": alias_unico}
    try:
        r = requests.post("https://api.tinyurl.com/create", json=payload, headers=headers)
        if r.status_code == 200:
            return r.json()['data']['tiny_url']
        else:
            payload.pop("alias")
            r = requests.post("https://api.tinyurl.com/create", json=payload, headers=headers)
            return r.json()['data']['tiny_url']
    except: return None

def actualizar_en_nube(id_id, nueva_url):
    alias_completo = f"v-qr-{id_id.lower()}"
    headers = {"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"}
    # Intentamos la ruta de actualización estándar
    url_api = f"https://api.tinyurl.com/change/tinyurl.com/{alias_completo}"
    try:
        r = requests.patch(url_api, json={"url": nueva_url}, headers=headers)
        return r.status_code == 200
    except: return False

def eliminar_en_nube(id_id):
    # Se intenta archivar el codigo qr | Eliminar
    # es decir se da de baja de forma "online"
    # y ya no deberia de funcionar
    alias_completo = f"v-qr-{id_id.lower()}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    url_api = "https://api.tinyurl.com/archive"
    payload = {"domain": "tinyurl.com", "alias": alias_completo}
    
    try:
        # TinyURL a veces requiere POST para archivar
        r = requests.post(url_api, json=payload, headers=headers)
        if r.status_code == 200:
            return True
        else:
            print(f"\nError de TinyURL ({r.status_code}): {r.json().get('errors', 'Acción no permitida')}")
            return False
    except Exception as e:
        print(f"Error de conexión con la nube: {e}")
        return False
    


def generar_imagen_qr(url_nube, id_gen):
    ruta_carpeta = os.path.join(os.path.expanduser("~"), "Desktop", "QR_FY")
    ruta_completa = os.path.join(ruta_carpeta, f"{id_gen}.png")
    os.makedirs(ruta_carpeta, exist_ok=True)
    qrcode.make(url_nube).save(ruta_completa)
    return ruta_completa