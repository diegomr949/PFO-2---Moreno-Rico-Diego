from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
DB_NAME = 'database.db'

def inicializar_db():
    """Crea la tabla de usuarios si no existe."""
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            contrasena TEXT NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

@app.route('/registro', methods=['POST'])
def registro():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contrasena = datos.get('contraseña')
    
    if not usuario or not contrasena:
        return jsonify({"error": "Faltan datos (usuario o contraseña)"}), 400
        
    # Hasheo de la contraseña antes de guardarla (Requisito clave)
    hash_contrasena = generate_password_hash(contrasena)
    
    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)", (usuario, hash_contrasena))
        conexion.commit()
        return jsonify({"mensaje": f"Usuario '{usuario}' registrado con éxito"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "El usuario ya existe"}), 400
    finally:
        conexion.close()

@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contrasena = datos.get('contraseña')
    
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("SELECT contrasena FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()
    conexion.close()
    
    # Se verifica si el usuario existe y si la contraseña coincide con el hash
    if resultado and check_password_hash(resultado[0], contrasena):
        return jsonify({"mensaje": "Login exitoso", "estado": "autorizado"}), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

@app.route('/tareas', methods=['GET'])
def tareas():
    # Retorna un HTML simple de bienvenida como pide el enunciado
    html_bienvenida = """
    <!DOCTYPE html>
    <html lang="es">
    <head><title>Gestión de Tareas</title></head>
    <body>
        <h1>¡Bienvenido al sistema de Gestión de Tareas!</h1>
        <p>Aquí podrás ver y administrar tus tareas pendientes.</p>
    </body>
    </html>
    """
    return html_bienvenida, 200

if __name__ == '__main__':
    inicializar_db()
    print("[*] Servidor Flask inicializado. Base de datos lista.")
    app.run(port=5000, debug=True)