"""
Clases de Servicios
"""

from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def mostrar_detalle(self):
        pass


class CorteCabello(Servicio):

    def mostrar_detalle(self):
        return f"Corte de Cabello - ${self.precio}"


class Manicure(Servicio):

    def mostrar_detalle(self):
        return f"Manicure - ${self.precio}"


class BarberiaPremium(Servicio):

    def mostrar_detalle(self):
        return f"Barbería Premium - ${self.precio}"
