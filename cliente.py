import requests
import sys

URL_BASE = "http://127.0.0.1:5000"
sesion_iniciada = False

def registrar_usuario():
    print("\n--- REGISTRO DE USUARIO ---")
    usuario = input("Ingrese nuevo usuario: ")
    contrasena = input("Ingrese nueva contraseña: ")
    
    respuesta = requests.post(f"{URL_BASE}/registro", json={"usuario": usuario, "contraseña": contrasena})
    print(f"Respuesta del servidor: {respuesta.json()}")

def iniciar_sesion():
    global sesion_iniciada
    print("\n--- INICIO DE SESIÓN ---")
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    
    respuesta = requests.post(f"{URL_BASE}/login", json={"usuario": usuario, "contraseña": contrasena})
    datos = respuesta.json()
    print(f"Respuesta del servidor: {datos}")
    
    if respuesta.status_code == 200:
        sesion_iniciada = True
        print("[+] Acceso concedido.")

def ver_tareas():
    print("\n--- MIS TAREAS ---")
    if not sesion_iniciada:
        print("[-] Error: Debes iniciar sesión primero para ver las tareas.")
        return
        
    respuesta = requests.get(f"{URL_BASE}/tareas")
    print("\nHTML devuelto por el servidor:")
    print("--------------------------------------------------")
    print(respuesta.text)
    print("--------------------------------------------------")

def menu_principal():
    while True:
        print("\n=== MENÚ API GESTIÓN DE TAREAS ===")
        print("1. Registrarse (POST /registro)")
        print("2. Iniciar Sesión (POST /login)")
        print("3. Ver Tareas (GET /tareas)")
        print("4. Salir")
        
        opcion = input("Elegí una opción (1-4): ")
        
        try:
            if opcion == '1':
                registrar_usuario()
            elif opcion == '2':
                iniciar_sesion()
            elif opcion == '3':
                ver_tareas()
            elif opcion == '4':
                print("Saliendo del cliente...")
                sys.exit(0)
            else:
                print("Opción no válida.")
        except requests.exceptions.ConnectionError:
            print("[-] Error de conexión: Asegurate de que servidor.py esté corriendo en otra terminal.")

if __name__ == '__main__':
    menu_principal()