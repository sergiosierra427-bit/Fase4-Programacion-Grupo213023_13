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
servicios = []
reservas = []

def ejecutar_simulacion():
    print("=== INICIO DE LA SIMULACIÓN DEL SISTEMA SOFTWARE FJ ===")
    
    # --- OPERACIÓN 1: Registro válido de un cliente ---
    try:
        print("\n--- Operación 1: Registrar cliente válido ---")
        # Tus atributos: nombre, identificacion, correo
        c1 = Cliente("Ana Pérez", "12345678", "ana@mail.com")
        clientes.append(c1)
        print(f"Cliente registrado con éxito: {c1.get_nombre()}")
    except ValidacionError as e:
        registrar_log(f"Error en Operación 1: {e}")
        print(f"Error controlado: {e}")
    else:
        registrar_log("Operación 1 completada exitosamente.")
    finally:
        print("Fin del bloque de la Operación 1.")

    # --- OPERACIÓN 2: Registro inválido de un cliente (Identificación no numérica) ---
    try:
        print("\n--- Operación 2: Registrar cliente con identificación inválida ---")
        c_inv = Cliente("Carlos", "ABC12345", "carlos@mail.com")
        clientes.append(c_inv)
    except ValidacionError as e:
        registrar_log(f"Excepción capturada en Operación 2: {e}")
        print(f"Excepción esperada manejada: {e}")
    else:
        print("Cliente agregado por error.")
    finally:
        print("Fin del bloque de la Operación 2.")

    # --- OPERACIÓN 3: Creación de servicio ReservaSala ---
    try:
        print("\n--- Operación 3: Crear servicio de Sala ---")
        sala1 = ReservaSala()
        servicios.append(sala1)
        print(f"Servicio creado: {sala1.mostrar_detalle()}")
    except Exception as e:
        registrar_log(f"Error en Operación 3: {e}")
        print(f"Error: {e}")
    finally:
        print("Fin Operación 3.")

    # --- OPERACIÓN 4: Creación de servicio AlquilerEquipo ---
    try:
        print("\n--- Operación 4: Crear servicio Alquiler de Equipo ---")
        equipo1 = AlquilerEquipo()
        servicios.append(equipo1)
        print(f"Servicio creado: {equipo1.mostrar_detalle()}")
    except Exception as e:
        registrar_log(f"Error en Operación 4: {e}")
    finally:
        print("Fin Operación 4.")

    # --- OPERACIÓN 5: Creación de servicio AsesoriaEspecializada ---
    try:
        print("\n--- Operación 5: Crear Asesoría Especializada ---")
        asesoria1 = AsesoriaEspecializada()
        servicios.append(asesoria1)
        print(f"Servicio creado: {asesoria1.mostrar_detalle()}")
    except Exception as e:
        registrar_log(f"Error en Operación 5: {e}")
    finally:
        print("Fin Operación 5.")

    # --- OPERACIÓN 6: Demostración de sobrecarga con cálculo de costos con impuesto y descuento ---
    try:
        print("\n--- Operación 6: Calcular costo con impuestos y descuentos ---")
        if servicios:
            # Usando parámetros opcionales definidos en tus métodos calcular_costo(impuesto, descuento)
            costo_personalizado = servicios[0].calcular_costo(impuesto=0.19, descuento=0.10)
            print(f"Costo de {servicios[0].nombre} con 19% IVA y 10% desc: ${costo_personalizado:,.0f}")
            registrar_log("Operación 6 de cálculo con parámetros completada.")
    except Exception as e:
        registrar_log(f"Error en Operación 6: {e}")
    finally:
        print("Fin Operación 6.")

    # --- OPERACIÓN 7: Reserva exitosa ---
    try:
        print("\n--- Operación 7: Realizar una reserva exitosa ---")
        if clientes and servicios:
            reserva1 = Reserva(cliente=clientes[0], servicio=servicios[0], fecha=datetime.now())
            reservas.append(reserva1)
            print(reserva1.mostrar_reserva())
            registrar_log("Operación 7: Reserva creada exitosamente.")
    except Exception as e:
        registrar_log(f"Error en Operación 7: {e}")
        print(f"Error: {e}")
    finally:
        print("Fin Operación 7.")

    # --- OPERACIÓN 8: Confirmación de reserva ---
    try:
        print("\n--- Operación 8: Confirmar reserva existente ---")
        if reservas:
            reservas[0].confirmar()
            print(f"Estado actual de la reserva: {reservas[0].estado}")
    except Exception as e:
        registrar_log(f"Error en Operación 8: {e}")
    finally:
        print("Fin Operación 8.")

    # --- OPERACIÓN 9: Cancelación de reserva ---
    try:
        print("\n--- Operación 9: Cancelar reserva ---")
        if reservas:
            reservas[0].cancelar()
            print(f"Estado tras cancelación: {reservas[0].estado}")
    except Exception as e:
        registrar_log(f"Error en Operación 9: {e}")
    finally:
        print("Fin Operación 9.")

    # --- OPERACIÓN 10: Intentar procesar una reserva cancelada (Forzando excepción) ---
    try:
        print("\n--- Operación 10: Intentar procesar reserva cancelada (Excepción) ---")
        if reservas:
            # Esto debe lanzar ReservaError porque la reserva está cancelada
            reservas[0].procesar()
    except ReservaError as e:
        registrar_log(f"Excepción controlada en Operación 10: {e}")
        print(f"Excepción capturada correctamente: {e}")
    else:
        print("Se procesó una reserva cancelada por error.")
    finally:
        print("Fin de la simulación de las 10 operaciones.")

if __name__ == "__main__":
    try:
        ejecutar_simulacion()
    except Exception as general_error:
        registrar_log(f"Error global en main: {general_error}")
        print(f"El sistema se mantuvo estable: {general_error}")
