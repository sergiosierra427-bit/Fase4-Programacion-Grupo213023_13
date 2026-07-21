"""
Clase Reserva
"""

from modelos.excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio, fecha):
        self.cliente = cliente
        self.servicio = servicio
        self.fecha = fecha
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):

        if self.estado == "Cancelada":
            raise ReservaError(
                "No se puede procesar una reserva cancelada."
            )

        self.estado = "Procesada"

    def mostrar_reserva(self):

        return (
            f"\nCliente: {self.cliente.get_nombre()}"
            f"\nServicio: {self.servicio.nombre}"
            f"\nCosto: ${self.servicio.calcular_costo():,.0f}"
            f"\nEstado: {self.estado}"
            f"\nFecha: {self.fecha.strftime('%d/%m/%Y %H:%M')}"
        )
