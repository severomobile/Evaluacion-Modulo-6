#!/usr/bin/env python
"""
manage.py – Utilidad de línea de comandos de Django.

Uso frecuente:
  python manage.py runserver        → Inicia el servidor de desarrollo
  python manage.py startapp <name>  → Crea una nueva aplicación
  python manage.py migrate          → Aplica migraciones de base de datos
"""

import os
import sys


def main() -> None:
    """Punto de entrada principal para comandos administrativos."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alke_web_base.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. Verificá que esté instalado y que el "
            "entorno virtual esté activado."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
