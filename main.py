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
servicios = []
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
def crear_reserva():
    try:
        print("\n=== CREAR RESERVA ===")

        if len(clientes) == 0:
            raise ClienteError("No hay clientes registrados.")

        if len(servicios) == 0:
            raise ServicioError("No hay servicios registrados.")

        print("\nClientes registrados:")
        for i, cliente in enumerate(clientes):
            print(f"{i + 1}. {cliente.get_nombre()}")

        opc_cliente = int(input("Seleccione el cliente: ")) - 1
        cliente = clientes[opc_cliente]

        print("\nServicios registrados:")
        for i, servicio in enumerate(servicios):
            print(f"{i + 1}. {servicio.mostrar_detalle()}")

        opc_servicio = int(input("Seleccione el servicio: ")) - 1
        servicio = servicios[opc_servicio]

        fecha = datetime.now()

        reserva = Reserva(cliente, servicio, fecha)

        reservas.append(reserva)

        print("\nReserva creada correctamente.")
        print(reserva.mostrar_reserva())

    except (ClienteError, ServicioError, ReservaError, IndexError, ValueError) as e:
        registrar_log(str(e))
        print("Error:", e)
    except ServicioError as e:
        registrar_log(str(e))
        print("Error:", e)
        return None
def mostrar_reservas():

    if len(reservas) == 0:
        print("\nNo hay reservas registradas.")
        return

    print("\n===== RESERVAS =====")

    for reserva in reservas:
        print(reserva.mostrar_reserva())
        print("----------------------------")
