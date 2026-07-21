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

    def __init__(self):
        super().__init__("Corte de Cabello", 30000)

    def mostrar_detalle(self):
        return f"{self.nombre} - ${self.precio}"


class Manicure(Servicio):

    def __init__(self):
        super().__init__("Manicure", 45000)

    def mostrar_detalle(self):
        return f"{self.nombre} - ${self.precio}"


class BarberiaPremium(Servicio):

    def __init__(self):
        super().__init__("Barbería Premium", 60000)

    def mostrar_detalle(self):
        return f"{self.nombre} - ${self.precio}"
