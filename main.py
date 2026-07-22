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

# Listas internas obligatorias (sin base de datos)
clientes = []
servicios = []
reservas = []

def ejecutar_simulacion_10_operaciones():
    print("==================================================")
    print(" INICIO DE SIMULACIÓN: 10 OPERACIONES SOFTWARE FJ ")
    print("==================================================")
    
    # -------------------------------------------------------------------------
    # OPERACIÓN 1: Registro VÁLIDO de un cliente (Uso de try/except/else/finally)
    # -------------------------------------------------------------------------
    print("\n[Op 1] Intentando registrar un cliente válido...")
    try:
        c1 = Cliente("Ana Pérez", "12345678", "ana.perez@mail.com")
        clientes.append(c1)
        print(f"-> Éxito: Cliente {c1.get_nombre()} registrado.")
    except ValidacionError as e:
        registrar_log(f"Op 1 Error: {e}")
        print(f"-> Error capturado: {e}")
    else:
        registrar_log("Op 1: Cliente registrado exitosamente sin excepciones.")
        print("-> Bloque ELSE: Validación superada correctamente.")
    finally:
        print("-> Bloque FINALLY: Operación 1 finalizada.")

    # -------------------------------------------------------------------------
    # OPERACIÓN 2: Registro INVÁLIDO de un cliente (Prueba de excepción de datos)
    # -------------------------------------------------------------------------
    print("\n[Op 2] Intentando registrar cliente con identificación inválida (letras)...")
    try:
        c_invalido = Cliente("Carlos Ruiz", "ABC98765", "carlos@mail.com")
        clientes.append(c_invalido)
    except ValidacionError as e:
        registrar_log(f"Op 2 Excepción esperada controlada: {e}")
        print(f"-> Excepción controlada con éxito: {e}")
    finally:
        print("-> Bloque FINALLY: Operación 2 finalizada.")

    # -------------------------------------------------------------------------
    # OPERACIÓN 3: Creación correcta del servicio 'ReservaSala'
    # -------------------------------------------------------------------------
    print("\n[Op 3] Creando servicio especializado: ReservaSala...")
    try:
        sala = ReservaSala()
        servicios.append(sala)
        print(f"-> Éxito: {sala.mostrar_detalle()}")
        registrar_log("Op 3: ReservaSala creada correctamente.")
    except Exception as e:
        registrar_log(f"Op 3 Error: {e}")
        print(f"-> Error: {e}")
    finally:
        print("-> Bloque FINALLY: Operación 3 finalizada.")

    # -------------------------------------------------------------------------
    # OPERACIÓN 4: Creación correcta del servicio 'AlquilerEquipo'
    # -------------------------------------------------------------------------
    print("\n[Op 4] Creando servicio especializado: AlquilerEquipo...")
    try:
        equipo = AlquilerEquipo()
        servicios.append(equipo)
        print(f"-> Éxito: {equipo.mostrar_detalle()}")
        registrar_log("Op 4: AlquilerEquipo creado correctamente.")
    except Exception as e:
        registrar_log(f"Op 4 Error: {e}")
    finally:
        print("-> Bloque FINALLY: Operación 4 finalizada.")

    # -------------------------------------------------------------------------
    # OPERACIÓN 5: Creación correcta del servicio 'AsesoriaEspecializada'
    # -------------------------------------------------------------------------
    print("\n[Op 5] Creando servicio especializado: AsesoriaEspecializada...")
    try:
        asesoria = AsesoriaEspecializada()
        servicios.append(asesoria)
        print(f"-> Éxito: {asesoria.mostrar_detalle()}")
        registrar_log("Op 5: AsesoriaEspecializada creada correctamente.")
    except Exception as e:
        registrar_log(f"Op 5 Error: {e}")
    finally:
        print("-> Bloque FINALLY: Operación 5 finalizada.")

    # -------------------------------------------------------------------------
    # OPERACIÓN 6: Demostración de métodos sobrecargados (Cálculo con impuestos/descuentos)
    # -------------------------------------------------------------------------
    print("\n[Op 6] Aplicando métodos sobrecargados de costos (Impuestos y Descuentos)...")
    try:
        if servicios:
            # Polimorfismo y parámetros opcionales
            costo_impuesto = servicios[0].calcular_costo(impuesto=0.19)
            costo_completo = servicios[0].calcular_costo(impuesto=0.19, descuento=0.10)
            print(f"-> Costo base Sala: ${servicios[0].precio:,.0f}")
            print(f"-> Costo con 19% IVA: ${costo_impuesto:,.0f}")
            print(f"-> Costo con 19% IVA y 10% Desc: ${costo_completo:,.0f}")
            registrar_log("Op 6: Cálculo de costos con parámetros opcionales exitoso.")
    except Exception as e:
        registrar_log(f"Op 6 Error: {e}")
        print(f"-> Error: {e}")
    finally:
        print("-> Bloque FINALLY: Operación 6 finalizada.")

    # -------------------------------------------------------------------------
    # OPERACIÓN 7: Creación de una Reserva VÁLIDA (Integra cliente, servicio, duración)
    # -------------------------------------------------------------------------
    print("\n[Op 7] Creando una reserva exitosa...")
    try:
        if clientes and servicios:
            reserva1 = Reserva(cliente=clientes[0], servicio=servicios[0], fecha=datetime.now(), duracion_horas=2)
            reservas.append(reserva1)
            print(reserva1.mostrar_reserva())
            registrar_log("Op 7: Reserva creada exitosamente.")
    except Exception as e:
        registrar_log(f"Op 7 Error: {e}")
        print(f"-> Error: {e}")
    finally:
        print("-> Bloque FINALLY: Operación 7 finalizada.")

    # -------------------------------------------------------------------------
    # OPERACIÓN 8: Confirmación de la reserva
    # -------------------------------------------------------------------------
    print("\n[Op 8] Confirmando la reserva existente...")
    try:
        if reservas:
            reservas[0].confirmar()
            print(f"-> Estado actualizado de la reserva: {reservas[0].estado}")
            registrar_log("Op 8: Reserva confirmada exitosamente.")
    except Exception as e:
        registrar_log(f"Op 8 Error: {e}")
    finally:
        print("-> Bloque FINALLY: Operación 8 finalizada.")

    # -------------------------------------------------------------------------
    # OPERACIÓN 9: Cancelación de la reserva
    # -------------------------------------------------------------------------
    print("\n[Op 9] Cancelando la reserva...")
    try:
        if reservas:
            reservas[0].cancelar()
            print(f"-> Estado actualizado de la reserva: {reservas[0].estado}")
            registrar_log("Op 9: Reserva cancelada exitosamente.")
    except Exception as e:
        registrar_log(f"Op 9 Error: {e}")
    finally:
        print("-> Bloque FINALLY: Operación 9 finalizada.")

    # -------------------------------------------------------------------------
    # OPERACIÓN 10: Intento fallido de procesar reserva cancelada (Encadenamiento y manejo de excepciones)
    # -------------------------------------------------------------------------
    print("\n[Op 10] Intentando procesar una reserva cancelada (Debe generar ReservaError)...")
    try:
        if reservas:
            reservas[0].procesar()
    except ReservaError as re:
        # Demostración de encadenamiento de excepciones exigido por la guía
        registrar_log(f"Op 10 Excepción controlada: {re}")
        print(f"-> Excepción de negocio capturada correctamente: {re}")
        raise ValueError("Fallo crítico controlado en el flujo de operaciones") from re
    except ValueError as ve:
        registrar_log(f"Op 10 Encadenamiento de excepción exitoso: {ve}")
        print(f"-> Excepción encadenada manejada de forma estable: {ve}")
    finally:
        print("-> Bloque FINALLY: Operación 10 finalizada.")

    print("\n==================================================")
    print(" ¡SIMULACIÓN DE LAS 10 OPERACIONES FINALIZADA CON ÉXITO! ")
    print(" Revisa el archivo 'errores.txt' para verificar los registros de logs.")
    print("==================================================")

if __name__ == "__main__":
    try:
        ejecutar_simulacion_10_operaciones()
    except Exception as global_error:
        registrar_log(f"Error global no atrapado: {global_error}")
        print(f"El sistema se mantuvo estable ante el error global: {global_error}")
