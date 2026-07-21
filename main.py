from datetime import datetime

from modelos.cliente import Cliente
from modelos.servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
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
        print("\n===== REGISTRO DE CLIENTE =====")

        nombre = input("Nombre: ")
        identificacion = input("Identificación: ")
        correo = input("Correo: ")

        cliente = Cliente(nombre, identificacion, correo)
        clientes.append(cliente)

        print("\nCliente registrado correctamente.")
        print(cliente)

        registrar_log("Cliente registrado correctamente")

    except ValidacionError as e:
        registrar_log(str(e))
        print("Error:", e)


def registrar_servicio():
    try:

        print("\n===== REGISTRO DE SERVICIO =====")

        print("1. Reserva de Sala")
        print("2. Alquiler de Equipo")
        print("3. Asesoría Especializada")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            servicio = ReservaSala()

        elif opcion == "2":
            servicio = AlquilerEquipo()

        elif opcion == "3":
            servicio = AsesoriaEspecializada()

        else:
            raise ServicioError("Servicio no válido.")

        servicios.append(servicio)

        print("\nServicio registrado correctamente.")
        print(servicio.mostrar_detalle())

        registrar_log(
            f"Servicio registrado: {servicio.nombre}"
        )

    except ServicioError as e:

        registrar_log(str(e))
        print("Error:", e)


def crear_reserva():

    try:

        if len(clientes) == 0:
            raise ClienteError("No hay clientes registrados.")

        if len(servicios) == 0:
            raise ServicioError("No hay servicios registrados.")

        print("\n===== CLIENTES =====")

        for i, cliente in enumerate(clientes):
            print(f"{i + 1}. {cliente.get_nombre()}")

        opcion_cliente = int(input("Seleccione un cliente: ")) - 1

        if opcion_cliente < 0 or opcion_cliente >= len(clientes):
            raise ClienteError("Cliente no válido.")

        cliente = clientes[opcion_cliente]

        print("\n===== SERVICIOS =====")

        for i, servicio in enumerate(servicios):
            print(
                f"{i + 1}. "
                f"{servicio.nombre} "
                f"(${servicio.calcular_costo():,.0f})"
            )

        opcion_servicio = int(input("Seleccione un servicio: ")) - 1

        if opcion_servicio < 0 or opcion_servicio >= len(servicios):
            raise ServicioError("Servicio no válido.")

        servicio = servicios[opcion_servicio]

        fecha = datetime.now()

        reserva = Reserva(
            cliente,
            servicio,
            fecha
        )

        reservas.append(reserva)

        print("\nReserva creada correctamente.")
        print(reserva.mostrar_reserva())

        registrar_log(
            f"Reserva creada para {cliente.get_nombre()}"
        )

    except (
        ClienteError,
        ServicioError,
        ReservaError,
        IndexError,
        ValueError,
    ) as e:

        registrar_log(str(e))
        print("Error:", e)


def mostrar_clientes():

    if len(clientes) == 0:
        print("\nNo hay clientes registrados.")
        return

    print("\n===== CLIENTES =====")

    for cliente in clientes:
        print(cliente)


def mostrar_servicios():

    if len(servicios) == 0:
        print("\nNo hay servicios registrados.")
        return

    print("\n===== SERVICIOS =====")

    for servicio in servicios:

        print(
            f"{servicio.nombre}"
            f" - ${servicio.calcular_costo():,.0f}"
        )


def mostrar_reservas():

    if len(reservas) == 0:
        print("\nNo hay reservas registradas.")
        return

    print("\n===== RESERVAS =====")

    for reserva in reservas:
        print(reserva.mostrar_reserva())
        print("-----------------------------------")


def menu():

    while True:

        print("\n====================================")
        print("          SOFTWARE FJ")
        print("====================================")
        print("1. Registrar cliente")
        print("2. Registrar servicio")
        print("3. Crear reserva")
        print("4. Mostrar clientes")
        print("5. Mostrar servicios")
        print("6. Mostrar reservas")
        print("7. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_cliente()

        elif opcion == "2":
            registrar_servicio()

        elif opcion == "3":
            crear_reserva()

        elif opcion == "4":
            mostrar_clientes()

        elif opcion == "5":
            mostrar_servicios()

        elif opcion == "6":
            mostrar_reservas()

        elif opcion == "7":
            print("\nGracias por utilizar Software FJ.")
            break

        else:
            print("\nOpción no válida.")


if __name__ == "__main__":
    menu()
