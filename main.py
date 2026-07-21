from datetime import datetime

from modelos.cliente import Cliente
from modelos.servicio import (
    CorteCabello,
    Manicure,
    BarberiaPremium
)
from modelos.reserva import Reserva
from modelos.logs import registrar_log
from modelos.excepciones import (
    ValidacionError,
    ClienteError,
    ServicioError,
    ReservaError
)

clientes = []
reservas = []
