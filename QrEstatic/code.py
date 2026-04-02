print("Test Version | Static Code -V")
# Imports
import qrcode
import os
import webbrowser

# Url a convertir
url = input("Ingresa la Url: ")

# Ruta donde guardar el PNG 
ruta_carpeta = os.path.join(os.path.expanduser("~"), "Desktop", "QR_FY") # Cambiar a ruta deseada !!
nombre_archivo = "qr.png"
ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)

# Crear la carpeta si no existe
os.makedirs(ruta_carpeta, exist_ok=True)

# Generar codigo QR
qr = qrcode.make(url)
qr.save(ruta_completa)  

# Mostrar Mensaje y Abrir imagen
print(f"QR Guardado en: {ruta_completa}")
webbrowser.open(ruta_completa)
input("Pulsa Enter para cerrar...")