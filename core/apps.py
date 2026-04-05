"""
apps.py – Configuración de la aplicación 'core'.

Django usa esta clase para identificar y registrar la app en el proyecto.
El atributo 'name' debe coincidir exactamente con el nombre del paquete.
"""

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Configuración principal de la app core."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
    verbose_name = "Core – Alke Web Base"
