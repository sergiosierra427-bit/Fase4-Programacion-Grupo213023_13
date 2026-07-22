from datetime import datetime
from modelos.cliente import Cliente
from modelos.excepciones import (
    ClienteError,
    ReservaError,
    ServicioError,
    ValidacionError,
)
from modelos.logs import registrar_log
from modelos.reserva import Reserva
from modelos.servicio import AlquilerEquipo, AsesoriaEspecializada, ReservaSala

# Listas internas en memoria (sin bases de datos)[cite: 2]
clientes = []
servicios = [ReservaSala(), AlquilerEquipo(), AsesoriaEspecializada()]
reservas = []


def registrar_cliente_interactivo():
  print("\n--- REGISTRAR NUEVO CLIENTE ---")
  # Uso de try/except/else/finally exigido por la guía[cite: 2]
  try:
    nombre = input("Ingrese el nombre del cliente: ")
    identificacion = input("Ingrese la identificación (solo números): ")
    correo = input("Ingrese el correo electrónico: ")

    # Intentar crear el objeto Cliente
    cliente = Cliente(nombre, identificacion, correo)
    clientes.append(cliente)
    print(
        f"¡Éxito! Cliente '{cliente.get_nombre()}' registrado correctamente."
    )
  except ValidacionError as e:
    registrar_log(f"Error de validación al registrar cliente: {e}")
    print(f"[EXCEPCIÓN CONTROLADA - ValidacionError]: {e}")
  else:
    registrar_log("Cliente registrado exitosamente sin errores.")
    print("-> Bloque ELSE: Datos validados y guardados con éxito.")
  finally:
    print("-> Bloque FINALLY: Proceso de registro de cliente finalizado.")


def listar_clientes():
  print("\n--- LISTA DE CLIENTES ---")
  if not clientes:
    print("No hay clientes registrados aún.")
    return
  for idx, c in enumerate(clientes):
    print(
        f"{idx + 1}. Nombre: {c.get_nombre()} | ID: {c.get_identificacion()} |"
        f" Correo: {c.get_correo()}"
    )


def mostrar_servicios():
  print("\n--- SERVICIOS DISPONIBLES ---")
  for idx, s in enumerate(servicios):
    print(f"{idx + 1}. {s.mostrar_detalle()}")


def realizar_reserva_interactiva():
  print("\n--- REALIZAR NUEVA RESERVA ---")
  if not clientes:
    print(
        "[AVISO]: Debe registrar al menos un cliente antes de hacer una"
        " reserva."
    )
    return

  listar_clientes()
  try:
    c_idx = int(input("Seleccione el número del cliente: ")) - 1
    if c_idx < 0 or c_idx >= len(clientes):
      raise ReservaError("El número de cliente seleccionado no existe.")
    cliente_elegido = clientes[c_idx]

    mostrar_servicios()
    s_idx = int(input("Seleccione el número del servicio: ")) - 1
    if s_idx < 0 or s_idx >= len(servicios):
      raise ReservaError("El número de servicio seleccionado no existe.")
    servicio_elegido = servicios[s_idx]

    duracion = int(input("Ingrese la duración en horas: "))
    if duracion <= 0:
      raise ReservaError("La duración en horas debe ser mayor a cero.")

    # Creación de la reserva
    reserva = Reserva(
        cliente=cliente_elegido,
        servicio=servicio_elegido,
        fecha=datetime.now(),
        duracion_horas=duracion,
    )
    reservas.append(reserva)
    print("\n¡Reserva creada con éxito!")
    print(reserva.mostrar_reserva())
    registrar_log(
        f"Reserva creada para {cliente_elegido.get_nombre()} con el servicio"
        f" {servicio_elegido.nombre}"
    )

  except ValueError as ve:
    registrar_log(f"Error de formato numérico en reserva: {ve}")
    print("[ERROR]: Debe ingresar un valor numérico válido.")
  except (ReservaError, ValidacionError) as e:
    registrar_log(f"Error en reserva: {e}")
    print(f"[EXCEPCIÓN CONTROLADA]: {e}")


def gestionar_reservas():
  if not reservas:
    print("\nNo hay reservas creadas para gestionar.")
    return

  print("\n--- GESTIÓN DE RESERVAS ---")
  for idx, r in enumerate(reservas):
    print(
        f"{idx + 1}. Cliente: {r.cliente.get_nombre()} | Servicio:"
        f" {r.servicio.nombre} | Estado: {r.estado}"
    )

  try:
    r_idx = int(input("Seleccione el número de la reserva a gestionar: ")) - 1
    if r_idx < 0 or r_idx >= len(reservas):
      print("Reserva no encontrada.")
      return

    reserva = reservas[r_idx]
    print("1. Confirmar reserva")
    print("2. Cancelar reserva")
    print("3. Procesar reserva (Prueba de excepción si está cancelada)")
    opcion = input("Elija una opción de gestión: ")

    if opcion == "1":
      reserva.confirmar()
      print("¡Reserva confirmada con éxito!")
      registrar_log(f"Reserva de {reserva.cliente.get_nombre()} confirmada.")
    elif opcion == "2":
      reserva.cancelar()
      print("¡Reserva cancelada!")
      registrar_log(f"Reserva de {reserva.cliente.get_nombre()} cancelada.")
    elif opcion == "3":
      reserva.procesar()
      print("¡Reserva procesada con éxito!")
      registrar_log("Reserva procesada.")
    else:
      print("Opción no válida.")

  except ReservaError as re:
    registrar_log(f"Excepción controlada en gestión de reserva: {re}")
    print(f"[EXCEPCIÓN DE NEGOCIO]: {re}")
  except ValueError:
    print("[ERROR]: Entrada inválida.")


def probar_calculo_sobrecargado():
  print("\n--- PRUEBA DE MÉTODOS SOBRECARGADOS (COSTOS) ---")
  mostrar_servicios()
  try:
    s_idx = int(input("Seleccione el servicio para calcular costo: ")) - 1
    if s_idx < 0 or s_idx >= len(servicios):
      print("Servicio inválido.")
      return
    serv = servicios[s_idx]

    imp = float(
        input("Ingrese el porcentaje de impuesto (ej: 0.19 para 19%): ")
    )
    desc = float(
        input("Ingrese el porcentaje de descuento (ej: 0.10 para 10%): ")
    )

    costo_final = serv.calcular_costo(impuesto=imp, descuento=desc)
    print(
        f"\nEl costo calculado para {serv.nombre} con impuesto de {imp*100}% y"
        f" descuento de {desc*100}% es: ${costo_final:,.0f}"
    )
    registrar_log(
        f"Cálculo de costo personalizado ejecutado para {serv.nombre}."
    )
  except ValueError:
    print(
        "[ERROR]: Ingrese valores numéricos válidos para impuestos y"
        " descuentos."
    )


def listar_todas_las_reservas():
  print("\n--- LISTADO GENERAL DE RESERVAS Y ESTADOS ---")
  if not reservas:
    print("No hay reservas registradas en el sistema.")
    return

  for idx, r in enumerate(reservas, 1):
    print(
        f"{idx}. Cliente: {r.cliente.get_nombre()} | Servicio:"
        f" {r.servicio.nombre} | Estado: {r.estado}"
    )


def main():
  while True:
    print("\n========================================")
    print(" SISTEMA DE GESTIÓN SOFTWARE FJ - MENÚ ")
    print("========================================")
    print("1. Registrar Cliente (Con validación y try/except/else/finally)")
    print("2. Ver Lista de Clientes")
    print("3. Ver Servicios Disponibles")
    print("4. Realizar Reserva")
    print("5. Gestionar Reservas (Confirmar / Cancelar / Procesar)")
    print("6. Calcular Costo Personalizado (Métodos sobrecargados)")
    print("7. Ver Listado General de Reservas")
    print("8. Salir del Sistema")

    opcion = input("\nSeleccione una opción (1-8): ").strip()

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
      probar_calculo_sobrecargado()
    elif opcion == "7":
      listar_todas_las_reservas()
    elif opcion == "8":
      print("\nSaliendo del sistema Software FJ. ¡Hasta pronto!")
      registrar_log("Cierre normal del sistema.")
      break
    else:
      print(
          "[AVISO]: Opción no válida. Por favor digite un número entre 1 y 8."
      )


if __name__ == "__main__":
  try:
    main()
  except Exception as global_error:
    registrar_log(f"Error crítico global no controlado: {global_error}")
    print(f"Error inesperado en el sistema: {global_error}")
