"""
Excepciones personalizadas del Sistema Gestión Software FJ
"""

class ClienteError(Exception):
    """Error relacionado con los clientes."""
    pass


class ServicioError(Exception):
    """Error relacionado con los servicios."""
    pass


class ReservaError(Exception):
    """Error relacionado con las reservas."""
    pass


class ValidacionError(Exception):
    """Error de validación de datos."""
    pass
