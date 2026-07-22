from datetime import datetime
from modelos.cliente import Cliente
from modelos.servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from modelos.reserva import Reserva
from modelos.logs import registrar_log
from modelos.excepciones import (
    ValidacionError,
    ClienteError,
    ServicioError,
    ReservaError
)

# Listas internas para la gestión en memoria
clientes = []
servicios = [
    ReservaSala(),
    AlquilerEquipo(),
    AsesoriaEspecializada()
]
reservas = []

def registrar_cliente_interactivo():
    print("\n--- REGISTRO DE NUEVO CLIENTE ---")
    try:
        nombre = input("Ingrese el nombre del cliente: ")
        identificacion = input("Ingrese la identificación (solo números): ")
        correo = input("Ingrese el correo electrónico: ")
        
        # Bloque try/except para validar datos ingresados
        cliente = Cliente(nombre, identificacion, correo)
        clientes.append(cliente)
        print(f"¡Cliente registrado con éxito: {cliente.get_nombre()}!")
        registrar_log(f"Cliente registrado interactivamente: {cliente.get_nombre()}")
        
    except ValidacionError as e:
        registrar_log(f"Error de validación al registrar cliente: {e}")
        print(f"[ERROR DE VALIDACIÓN]: {e}")
    except Exception as e:
        registrar_log(f"Error inesperado al registrar cliente: {e}")
        print(f"[ERROR]: {e}")

def listar_clientes():
    print("\n--- LISTA DE CLIENTES REGISTRADOS ---")
    if not clientes:
        print("No hay clientes registrados.")
        return
    for i, c in enumerate(clientes):
        print(f"{i + 1}. {c}")

def mostrar_servicios():
    print("\n--- SERVICIOS DISPONIBLES ---")
    for i, s in enumerate(servicios):
        print(f"{i + 1}. {s.mostrar_detalle()}")

def realizar_reserva_interactiva():
    print("\n--- REALIZAR NUEVA RESERVA ---")
    if not clientes:
        print("Debe registrar al menos un cliente antes de hacer una reserva.")
        return
    
    listar_clientes()
    try:
        c_idx = int(input("Seleccione el número del cliente: ")) - 1
        if c_idx < 0 or c_idx >= len(clientes):
            raise ReservaError("Índice de cliente inválido.")
        
        cliente_seleccionado = clientes[c_idx]
        
        mostrar_servicios()
        s_idx = int(input("Seleccione el número del servicio: ")) - 1
        if s_idx < 0 or s_idx >= len(servicios):
            raise ReservaError("Índice de servicio inválido.")
            
        servicio_seleccionado = servicios[s_idx]
        
        # Fecha actual o personalizada
        fecha_reserva = datetime.now()
        
        reserva = Reserva(cliente_seleccionado, servicio_seleccionado, fecha_reserva)
        reservas.append(reserva)
        print("¡Reserva creada exitosamente!")
        print(reserva.mostrar_reserva())
        registrar_log(f"Reserva creada para el cliente {cliente_seleccionado.get_nombre()}")
        
    except ValueError:
        registrar_log("Error de formato: Se esperaba un número entero en la selección.")
        print("[ERROR]: Debe ingresar un número válido.")
    except (ReservaError, ValidacionError) as e:
        registrar_log(f"Error en reserva: {e}")
        print(f"[ERROR EN RESERVA]: {e}")

def gestionar_reservas():
    if not reservas:
        print("\nNo hay reservas creadas para gestionar.")
        return
        
    print("\n--- GESTIÓN DE RESERVAS ---")
    for i, r in enumerate(reservas):
        print(f"{i + 1}. Cliente: {r.cliente.get_nombre()} | Servicio: {r.servicio.nombre} | Estado: {r.estado}")
        
    try:
        r_idx = int(input("Seleccione el número de la reserva a gestionar: ")) - 1
        if r_idx < 0 or r_idx >= len(reservas):
            print("Reserva no encontrada.")
            return
            
        reserva = reservas[r_idx]
        print("1. Confirmar reserva")
        print("2. Cancelar reserva")
        print("3. Procesar reserva (Prueba de excepción si está cancelada)")
        opcion = input("Elija una acción: ")
        
        if opcion == "1":
            reserva.confirmar()
            print("Reserva confirmada.")
            registrar_log(f"Reserva {r_idx + 1} confirmada.")
        elif opcion == "2":
            reserva.cancelar()
            print("Reserva cancelada.")
            registrar_log(f"Reserva {r_idx + 1} cancelada.")
        elif opcion == "3":
            reserva.procesar()
            print("Reserva procesada con éxito.")
        else:
            print("Opción inválida.")
            
    except ReservaError as e:
        registrar_log(f"Excepción controlada al gestionar reserva: {e}")
        print(f"[EXCEPCIÓN CONTROLADA]: {e}")
    except ValueError:
        print("[ERROR]: Entrada inválida.")

def main():
    while True:
        print("\n================")
        print(" SISTEMA SOFTWARE FJ ")
        print("================")
        print("1. Registrar Cliente")
        print("2. Ver Clientes Registrados")
        print("3. Ver Servicios Disponibles")
        print("4. Realizar Reserva")
        print("5. Gestionar Reservas (Confirmar/Cancelar/Procesar)")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_cliente_interactivo()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            mostrar_servicios()
        elif opcion == "4":
            realizar_reserva_interactiva()
        elif opcion == "5":
                    gestionar_reservas()
        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
