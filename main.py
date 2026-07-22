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
        print("Error de validación:", e)


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
        registrar_log(f"Servicio registrado: {servicio.nombre}")

    except ServicioError as e:
        registrar_log(str(e))
        print("Error de servicio:", e)


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
            print(f"{i + 1}. {servicio.nombre} (${servicio.calcular_costo():,.0f})")

        opcion_servicio = int(input("Seleccione un servicio: ")) - 1
        if opcion_servicio < 0 or opcion_servicio >= len(servicios):
            raise ServicioError("Servicio no válido.")

        servicio = servicios[opcion_servicio]
        fecha = datetime.now()

        reserva = Reserva(cliente, servicio, fecha)
        reservas.append(reserva)

        print("\nReserva creada correctamente.")
        print(reserva.mostrar_reserva())
        registrar_log(f"Reserva creada para {cliente.get_nombre()}")

    except (ClienteError, ServicioError, ReservaError, IndexError, ValueError) as e:
        registrar_log(str(e))
        print("Error en reserva:", e)


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
        print(f"{servicio.nombre} - ${servicio.calcular_costo():,.0f}")


def mostrar_reservas():
    if len(reservas) == 0:
        print("\nNo hay reservas registradas.")
        return
    print("\n===== RESERVAS =====")
    for reserva in reservas:
        print(reserva.mostrar_reserva())
        print("-----------------------------------")


def ejecutar_simulacion_10_operaciones():
    print("\n==================================================")
    print(" SIMULACIÓN AUTOMÁTICA DE LAS 10 OPERACIONES DE LA GUÍA")
    print("==================================================")
    
    global clientes, servicios, reservas
    clientes.clear()
    servicios.clear()
    reservas.clear()

    # 1. Cliente válido
    print("\n--- [Operación 1] Registro de Cliente Válido ---")
    try:
        c1 = Cliente("Carlos Pérez", "1098765432", "carlos@unad.edu.co")
        clientes.append(c1)
        print("Éxito al registrar:", c1)
        registrar_log("Simulación: Cliente válido registrado exitosamente")
    except Exception as e:
        print("Error inesperado:", e)

    # 2. Cliente inválido (identificación con letras o formato erróneo)
    print("\n--- [Operación 2] Registro de Cliente Inválido (Debe fallar) ---")
    try:
        print("Intentando registrar cliente con ID alfabética 'ABC123'...")
        c_invalido = Cliente("Ana Gómez", "ABC123", "ana@unad.edu.co")
        clientes.append(c_invalido)
    except ValidacionError as e:
        print("Excepción capturada con éxito:", e)
        registrar_log(f"Simulación controlada - Excepción de validación de cliente: {e}")

    # 3. Cliente válido (Segundo cliente)
    print("\n--- [Operación 3] Registro de Segundo Cliente Válido ---")
    try:
        c2 = Cliente("María Rodríguez", "1012345678", "maria@unad.edu.co")
        clientes.append(c2)
        print("Éxito al registrar:", c2)
        registrar_log("Simulación: Segundo cliente válido registrado exitosamente")
    except Exception as e:
        print("Error inesperado:", e)

    # 4. Servicio válido 1
    print("\n--- [Operación 4] Registro de Servicio Válido (Reserva de Sala) ---")
    try:
        s1 = ReservaSala()
        servicios.append(s1)
        print("Éxito al registrar servicio:", s1.mostrar_detalle())
        registrar_log("Simulación: Servicio de sala registrado")
    except Exception as e:
        print("Error inesperado:", e)

    # 5. Servicio válido 2
    print("\n--- [Operación 5] Registro de Servicio Válido (Alquiler de Equipo) ---")
    try:
        s2 = AlquilerEquipo()
        servicios.append(s2)
        print("Éxito al registrar servicio:", s2.mostrar_detalle())
        registrar_log("Simulación: Alquiler de equipo registrado")
    except Exception as e:
        print("Error inesperado:", e)

    # 6. Servicio inválido
    print("\n--- [Operación 6] Registro de Servicio Inválido (Debe fallar) ---")
    try:
        print("Intentando seleccionar un código de servicio inexistente ('99')...")
        codigo_falso = "99"
        if codigo_falso not in ["1", "2", "3"]:
            raise ServicioError("El código de servicio ingresado no existe.")
    except ServicioError as e:
        print("Excepción capturada con éxito:", e)
        registrar_log(f"Simulación controlada - Excepción de servicio: {e}")

    # 7. Reserva válida 1
    print("\n--- [Operación 7] Creación de Reserva Válida #1 ---")
    try:
        r1 = Reserva(clientes[0], servicios[0], datetime.now())
        r1.confirmar()
        reservas.append(r1)
        print("Éxito al crear reserva:")
        print(r1.mostrar_reserva())
        registrar_log("Simulación: Reserva 1 creada y confirmada correctamente")
    except Exception as e:
        print("Error inesperado:", e)

    # 8. Reserva válida 2
    print("\n--- [Operación 8] Creación de Reserva Válida #2 ---")
    try:
        r2 = Reserva(clientes[1], servicios[1], datetime.now())
        r2.confirmar()
        reservas.append(r2)
        print("Éxito al crear reserva:")
        print(r2.mostrar_reserva())
        registrar_log("Simulación: Reserva 2 creada y confirmada correctamente")
    except Exception as e:
        print("Error inesperado:", e)

    # 9. Reserva inválida (Índice de cliente fuera de rango)
    print("\n--- [Operación 9] Creación de Reserva Inválida (Debe fallar) ---")
    try:
        print("Intentando crear reserva con un índice de cliente inexistente (99)...")
        indice_inexistente = 99
        if indice_inexistente >= len(clientes):
            raise ClienteError("El cliente seleccionado no se encuentra registrado.")
    except ClienteError as e:
        print("Excepción capturada con éxito:", e)
        registrar_log(f"Simulación controlada - Excepción de reserva/cliente: {e}")

    # 10. Procesar reserva cancelada (Operación de negocio inválida)
    print("\n--- [Operación 10] Procesar Reserva Cancelada (Debe fallar) ---")
    try:
        r_falla = Reserva(clientes[0], servicios[0], datetime.now())
        r_falla.cancelar()
        print(f"Estado actual de la reserva: {r_falla.estado}")
        print("Intentando procesar una reserva que ya fue cancelada...")
        r_falla.procesar()
    except ReservaError as e:
        print("Excepción de negocio capturada con éxito:", e)
        registrar_log(f"Simulación controlada - Excepción de estado de reserva: {e}")
    
    print("\n==================================================")
    print(" ¡SIMULACIÓN DE LAS 10 OPERACIONES COMPLETADA! ")
    print(" Revisa el archivo 'errores.txt' para verificar los logs.")
    print("==================================================\n")


def menu():
    while True:
        print("\n====================================")
        print("         SOFTWARE FJ")
        print("====================================")
        print("1. Registrar cliente")
        print("2. Registrar servicio")
        print("3. Crear reserva")
        print("4. Mostrar clientes")
        print("5. Mostrar servicios")
        print("6. Mostrar reservas")
        print("7. Ejecutar Simulación de 10 Operaciones")
        print("8. Salir")

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
            ejecutar_simulacion_10_operaciones()
        elif opcion == "8":
            print("\nGracias por utilizar Software FJ.")
            break
        else:
            print("\nOpción no válida.")


if __name__ == "__main__":
    menu()
