"""
Clase Reserva
"""

from datetime import datetime


class Reserva:

    def __init__(self, cliente, servicio, fecha):
        self.cliente = cliente
        self.servicio = servicio
        self.fecha = fecha

    def mostrar_reserva(self):
        return (
            f"\nCliente: {self.cliente.get_nombre()}"
            f"\nServicio: {self.servicio.mostrar_detalle()}"
            f"\nFecha: {self.fecha.strftime('%d/%m/%Y %H:%M')}"
        )
