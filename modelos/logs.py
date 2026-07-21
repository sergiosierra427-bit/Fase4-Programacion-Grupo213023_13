"""
Módulo para registrar eventos y errores del sistema.
"""

from datetime import datetime


def registrar_log(mensaje):
    """
    Guarda un mensaje en el archivo errores.txt
    """
    with open("errores.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{datetime.now()}] {mensaje}\n")
