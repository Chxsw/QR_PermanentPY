print("Test Version v1B [Menu Display] | Dinamic Code -V")
print("-" * 30)
# Imports
import os
import webbrowser
import ConexionBDD as db
import CodeV1B as logic

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        limpiar()
        print("========================================")
        print("    GESTOR HÍBRIDO V1B - PROYECTO      ")
        print("========================================")
        print("1.- Actualizar un Código QR (URL)")
        print("2.- Ingresar una nueva URL (Nuevo QR)")
        print("3.- ELIMINAR un Código QR")
        print("4.- Salir")
        print("----------------------------------------")
        opc = input("Seleccione una opción: ")

        # --- OPCIÓN 1: ACTUALIZAR ---
        if opc == "1":
            limpiar()
            registros = db.listar_qrs_locales()
            if not registros:
                print("No hay QRs en la base de datos.")
            else:
                print(f"{'ID':<15} | {'URL ACTUAL'}")
                print("-" * 55)
                for r in registros:
                    print(f"{r[0]:<15} | {r[1]}")
                
                id_mod = input("\nID a modificar: ").strip()
                new_url = input("Nueva URL de destino: ").strip()
                
                print("\n🔄 Sincronizando con la nube...")
                if logic.actualizar_en_nube(id_mod, new_url):
                    if db.update_db_local(id_mod, new_url):
                        print(f"¡Éxito! {id_mod} actualizado.")
                    else:
                        print("¡Error! Se actualizó en la nube pero falló el MySQL.")
                else:
                    print("¡Error! La Nube (TinyURL) no permitió el cambio.")
            input("\nPresione Enter para volver...")

        # --- OPCIÓN 2: CREAR NUEVO ---
        elif opc == "2":
            limpiar()
            print("--- CREACIÓN DE NUEVO QR HÍBRIDO ---")
            ultimo = db.obtener_ultimo_id_v2()
            
            if ultimo:
                try:
                    num = int(ultimo.replace("QrDinamicVB", ""))
                    id_gen = f"QrDinamicVB{num + 1:02d}"
                except: id_gen = "QrDinamicVB00"
            else:
                id_gen = "QrDinamicVB00"
            
            print(f"ID asignado: {id_gen}")
            alias = input(f"Nombre/Alias para el proyecto: ")
            url_f = input("URL de destino final: ")
            
            print("\n --Creando en la nube--")
            url_nube = logic.crear_en_nube(url_f, id_gen)
            
            if url_nube and db.registrar_qr_v2(id_gen, alias, url_f):
                ruta = logic.generar_imagen_qr(url_nube, id_gen)
                print(f"\n¡¡QR Generado!!: {ruta}")
                webbrowser.open(ruta)
            else:
                print("\n¡Error! al crear el QR. Revisa conexión o API Token.")
            input("\nPresione Enter para volver...")

        # --- OPCIÓN 3: ELIMINAR (CON FORZADO LOCAL) ---
        elif opc == "3":
            limpiar()
            registros = db.listar_qrs_locales()
            if not registros:
                print("No hay QRs en la base de datos.")
            else:
                print(f"{'ID':<15} | {'URL ACTUAL'}")
                print("-" * 55)
                for r in registros:
                    print(f"{r[0]:<15} | {r[1]}")

                id_del = input("\nID a ELIMINAR: ").strip()
                confirmar = input(f"¿Confirmar eliminación de {id_del}? (s/n): ")
                
                if confirmar.lower() == 's':
                    print("\n --Intentando eliminar de la Nube--")
                    
                    if logic.eliminar_en_nube(id_del):
                        if db.eliminar_qr_local(id_del):
                            print(f" ¡ÉXITO!: {id_del} eliminado de ambos sitios.")
                        else:
                            print(f" ¡Error! Se eliminó de la Nube pero no del MySQL local.")
                    else:
                        print(f"FALLO EN LA NUBE: El QR sigue activo en internet.")
                        print("-" * 40)
                        forzado = input(f"¿Deseas FORZAR EL BORRADO LOCAL de {id_del}? (s/n): ")
                        
                        if forzado.lower() == 's':
                            if db.eliminar_qr_local(id_del):
                                print(f"Borrado Local Forzado exitoso.")
                            else:
                                print(f"¡Erro! crítico al borrar localmente.")
            input("\nPresione Enter para volver...")

        # --- OPCIÓN 4: SALIR ---
        elif opc == "4":
            print("Cerrando sistema...")
            break
        
        else:
            print("Opción no válida.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    menu()