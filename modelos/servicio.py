"""
Clases de Servicios
"""

from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def mostrar_detalle(self):
        pass


class ReservaSala(Servicio):

    def __init__(self):
        super().__init__("Reserva de Sala", 50000)

    def calcular_costo(self, impuesto=0, descuento=0):
        total = self.precio
        total += total * impuesto
        total -= total * descuento
        return total

    def mostrar_detalle(self):
        return f"{self.nombre} - ${self.calcular_costo():,.0f}"


class AlquilerEquipo(Servicio):

    def __init__(self):
        super().__init__("Alquiler de Equipo", 80000)

    def calcular_costo(self, impuesto=0, descuento=0):
        total = self.precio
        total += total * impuesto
        total -= total * descuento
        return total

    def mostrar_detalle(self):
        return f"{self.nombre} - ${self.calcular_costo():,.0f}"


class AsesoriaEspecializada(Servicio):

    def __init__(self):
        super().__init__("Asesoría Especializada", 120000)

    def calcular_costo(self, impuesto=0, descuento=0):
        total = self.precio
        total += total * impuesto
        total -= total * descuento
        return total

    def mostrar_detalle(self):
        return f"{self.nombre} - ${self.calcular_costo():,.0f}"
