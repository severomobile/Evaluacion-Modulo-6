"""
wsgi.py – Punto de entrada WSGI para servidores en producción.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alke_web_base.settings")
application = get_wsgi_application()
