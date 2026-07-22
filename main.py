from datetime import datetime
from modelos.cliente import Cliente
from modelos.servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from modelos.reserva import Reserva
from modelos.logs import registrar_log  # O la función encargada de escribir en el archivo de log
from modelos.excepciones import (
    ValidacionError,
    ClienteError,
    ServicioError,
    ReservaError
)

# Listas internas para la gestión en memoria (sin bases de datos)
clientes = []
servicios = []
reservas = []

def ejecutar_simulacion():
    print("=== INICIO DE LA SIMULACIÓN DEL SISTEMA SOFTWARE FJ ===")
    
    # Se deben simular al menos 10 operaciones (éxitos y fallos controlados)
    
    # --- OPERACIÓN 1: Registro válido de un cliente ---
    try:
        print("\n--- Operación 1: Registrar cliente válido ---")
        # Bloque try para capturar errores de validación de datos personales
        c1 = Cliente("12345678", "Ana Pérez", "ana@mail.com", "3001234567")
        clientes.append(c1)
        print(f"Cliente registrado con éxito: {c1.nombre}")
    except (ValidacionError, ClienteError) as e:
        registrar_log(f"Error en Operación 1: {e}")
        print(f"Error controlado: {e}")
    else:
        registrar_log("Operación 1 completada exitosamente.")
    finally:
        print("Fin del bloque de la Operación 1.")

    # --- OPERACIÓN 2: Registro inválido de un cliente (prueba de excepción) ---
    try:
        print("\n--- Operación 2: Registrar cliente con datos inválidos ---")
        # Datos erróneos (ej. cédula muy corta o correo sin @) para forzar excepción
        c_inv = Cliente("123", "Carlos", "correo-invalido", "abc")
        clientes.append(c_inv)
    except (ValidacionError, ClienteError) as e:
        registrar_log(f"Excepción capturada correctamente en Operación 2: {e}")
        print(f"Excepción esperada manejada: {e}")
    else:
        print("Cliente agregado por error.")
    finally:
        print("Fin del bloque de la Operación 2.")

    # --- OPERACIÓN 3: Creación correcta de un servicio (Ej. Sala) ---
    try:
        print("\n--- Operación 3: Crear servicio de Sala válido ---")
        sala1 = ReservaSala(id_servicio="S001", costo_base=100.0, capacidad=10)
        servicios.append(sala1)
        print(f"Servicio creado: {sala1.descripcion()}")
    except ServicioError as e:
        registrar_log(f"Error en Operación 3: {e}")
        print(f"Error: {e}")
    finally:
        print("Fin Operación 3.")

    # --- OPERACIÓN 4: Creación incorrecta de un servicio (Parámetros inválidos) ---
    try:
        print("\n--- Operación 4: Crear servicio con costo negativo ---")
        sala_inv = ReservaSala(id_servicio="S002", costo_base=-50.0, capacidad=0)
        servicios.append(sala_inv)
    except ServicioError as e:
        registrar_log(f"Excepción esperada en Operación 4: {e}")
        print(f"Excepción controlada en servicio: {e}")
    finally:
        print("Fin Operación 4.")

    # --- OPERACIÓN 5: Creación de Alquiler de Equipo ---
    try:
        print("\n--- Operación 5: Crear servicio de Alquiler de Equipo ---")
        equipo1 = AlquilerEquipo(id_servicio="E001", costo_base=50.0, tipo_equipo="Portátil")
        servicios.append(equipo1)
        print(f"Servicio creado: {equipo1.descripcion()}")
    except ServicioError as e:
        registrar_log(f"Error en Operación 5: {e}")
    finally:
        print("Fin Operación 5.")

    # --- OPERACIÓN 6: Creación de Asesoría Especializada ---
    try:
        print("\n--- Operación 6: Crear Asesoría Especializada ---")
        asesoria1 = AsesoriaEspecializada(id_servicio="A001", costo_base=200.0, area="Arquitectura de Software")
        servicios.append(asesoria1)
        print(f"Servicio creado: {asesoria1.descripcion()}")
    except ServicioError as e:
        registrar_log(f"Error en Operación 6: {e}")
    finally:
        print("Fin Operación 6.")

    # --- OPERACIÓN 7: Reserva exitosa (integrando cliente y servicio) ---
    try:
        print("\n--- Operación 7: Realizar una reserva exitosa ---")
        if clientes and servicios:
            # Usando métodos sobrecargados de cálculo de costos (ej. con parámetros opcionales o descuentos)
            reserva1 = Reserva(id_reserva="R001", cliente=clientes[0], servicio=servicios[0], duracion_horas=3)
            # Demostración de métodos sobrecargados de costos si aplican
            costo_total = servicios[0].calcular_costo(3, descuento=0.1) 
            reservas.append(reserva1)
            print(f"Reserva creada con éxito. Costo calculado con descuento: {costo_total}")
    except (ReservaError, ServicioError) as e:
        registrar_log(f"Error en Operación 7: {e}")
        print(f"Error: {e}")
    finally:
        print("Fin Operación 7.")

    # --- OPERACIÓN 8: Reserva fallida (Servicio no disponible o parámetros erróneos) ---
    try:
        print("\n--- Operación 8: Intentar reserva con datos incorrectos ---")
        # Intentar reservar usando un objeto nulo o duración negativa
        reserva_fallida = Reserva(id_reserva="R002", cliente=clientes[0], servicio=servicios[0], duracion_horas=-5)
    except ReservaError as e:
        registrar_log(f"Excepción capturada en Operación 8 (Reserva fallida controlada): {e}")
        print(f"Reserva fallida controlada correctamente: {e}")
    finally:
        print("Fin Operación 8.")

    # --- OPERACIÓN 9: Procesamiento / Confirmación de Reserva ---
    try:
        print("\n--- Operación 9: Confirmar reserva existente ---")
        if reservas:
            reservas[0].confirmar()
            print("Reserva confirmada exitosamente.")
    except ReservaError as e:
        registrar_log(f"Error al confirmar reserva en Operación 9: {e}")
        print(f"Error: {e}")
    finally:
        print("Fin Operación 9.")

    # --- OPERACIÓN 10: Cancelación de Reserva con encadenamiento de excepciones ---
    try:
        print("\n--- Operación 10: Cancelación de una reserva ---")
        if reservas:
            reservas[0].cancelar()
            print("Reserva cancelada correctamente.")
    except Exception as e:
        # Ejemplo de encadenamiento de excepciones (raise ... from ...) si ocurre un fallo crítico
        registrar_log(f"Error crítico en Operación 10: {e}")
        raise ReservaError("Fallo crítico en el flujo de cancelación") from e
    finally:
        print("Fin de la simulación de las 10 operaciones.")

if __name__ == "__main__":
    try:
        ejecutar_simulacion()
    except Exception as general_error:
        registrar_log(f"Error global no controlado en main: {general_error}")
        print(f"El sistema se mantuvo estable a pesar de un error global: {general_error}")
