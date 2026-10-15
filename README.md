# PFO 2: Sistema de Gestión de Tareas con API y Base de Datos

## Descripción
Este proyecto implementa una API REST utilizando Flask y SQLite para la gestión de usuarios y tareas. Incluye autenticación básica con contraseñas hasheadas y un cliente de consola para interactuar con los endpoints.

## Requisitos Previos
- Python 3.x instalado.
- Instalar las dependencias requeridas ejecutando en la consola:
  `pip install flask werkzeug requests`

## Instrucciones de Ejecución y Pruebas
1. **Clonar el repositorio** y abrir la carpeta del proyecto en la terminal.
2. **Iniciar el Servidor API:**
   Abre una terminal y ejecuta:
   `python servidor.py`
   *(Esto creará automáticamente el archivo `database.db` y levantará el servicio local en el puerto 5000).*
3. **Iniciar el Cliente:**
   Abre una **segunda terminal** (sin cerrar la del servidor) y ejecuta:
   `python cliente.py`
4. **Probar el sistema:**
   Sigue el menú interactivo en la consola del cliente para:
   - Registrar un nuevo usuario (POST `/registro`).
   - Iniciar sesión con esas credenciales (POST `/login`).
   - Consultar el endpoint protegido para ver las tareas (GET `/tareas`).

## Respuestas Conceptuales
**¿Por qué hashear contraseñas?**
Almacenar contraseñas en texto plano expone las credenciales si la base de datos es vulnerada. Aplicar un hash criptográfico unidireccional convierte la clave en una cadena ilegible e irreversible, permitiendo al servidor validar la identidad comparando los hashes sin conocer ni exponer nunca la contraseña original.

**Ventajas de usar SQLite en este proyecto:**
SQLite es un motor de base de datos transaccional autocontenido en un simple archivo local. No requiere instalar, configurar ni mantener servicios adicionales en el sistema operativo, lo que facilita enormemente la portabilidad del código, agiliza el desarrollo y cumple perfectamente con la necesidad de persistencia requerida para esta API.
