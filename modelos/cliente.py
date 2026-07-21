"""
Clase Cliente
"""

from modelos.excepciones import ValidacionError


class Cliente:

    def __init__(self, nombre, identificacion, correo):
        self.set_nombre(nombre)
        self.set_identificacion(identificacion)
        self.set_correo(correo)

    def set_nombre(self, nombre):
        if not nombre.strip():
            raise ValidacionError("El nombre no puede estar vacío.")
        self.__nombre = nombre

    def set_identificacion(self, identificacion):
        if not str(identificacion).isdigit():
            raise ValidacionError("La identificación debe contener solo números.")
        self.__identificacion = identificacion

    def set_correo(self, correo):
        if "@" not in correo:
            raise ValidacionError("Correo electrónico inválido.")
        self.__correo = correo

    def get_nombre(self):
        return self.__nombre

    def get_identificacion(self):
        return self.__identificacion

    def get_correo(self):
        return self.__correo

    def __str__(self):
        return f"Cliente: {self.__nombre} - {self.__identificacion}"
