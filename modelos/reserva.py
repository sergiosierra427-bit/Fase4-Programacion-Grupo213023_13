"""
Clase Reserva
"""

from modelos.excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio, fecha, duracion_horas):
        self.cliente = cliente
        self.servicio = servicio
        self.fecha = fecha
        self.duracion_horas = duracion_horas
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):
        if self.estado == "Cancelada":
            raise ReservaError("No se puede procesar una reserva cancelada.")
        self.estado = "Procesada"

    def mostrar_reserva(self):
        # Calculamos el costo multiplicando por la duración si aplica o usando el método
        costo_total = self.servicio.calcular_costo() * self.duracion_horas
        return (
            f"\nCliente: {self.cliente.get_nombre()}"
            f"\nServicio: {self.servicio.nombre}"
            f"\nDuración: {self.duracion_horas} hora(s)"
            f"\nCosto Total: ${costo_total:,.0f}"
            f"\nEstado: {self.estado}"
            f"\nFecha: {self.fecha.strftime('%d/%m/%Y %H:%M')}"
        )
