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
def registrar_cliente():
    try:
        print("\n=== REGISTRO DE CLIENTE ===")

        nombre = input("Nombre: ")
        identificacion = input("Identificación: ")
        correo = input("Correo: ")

        cliente = Cliente(nombre, identificacion, correo)

        clientes.append(cliente)

        print("\nCliente registrado correctamente.")

    except ValidacionError as e:
        registrar_log(str(e))
        print("Error:", e)
def registrar_servicio():
    try:
        print("\n=== REGISTRO DE SERVICIO ===")

        print("1. Corte de Cabello")
        print("2. Manicure")
        print("3. Barbería Premium")

        opcion = input("Seleccione un servicio: ")

        if opcion == "1":
            servicio = CorteCabello()

        elif opcion == "2":
            servicio = Manicure()

        elif opcion == "3":
            servicio = BarberiaPremium()

        else:
            raise ServicioError("Servicio no válido.")

        print("\nServicio registrado correctamente.")
        print(servicio)

        return servicio

    except ServicioError as e:
        registrar_log(str(e))
        print("Error:", e)
        return None
