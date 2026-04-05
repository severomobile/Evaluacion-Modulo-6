"""
urls.py – Enrutamiento raíz del proyecto.

Patrón recomendado: el proyecto delega las rutas de cada app
mediante include(), manteniendo este archivo limpio y escalable.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Panel de administración de Django (disponible en /admin/)
    path("admin/", admin.site.urls),

    # Delegamos TODAS las rutas de la app 'core' al archivo core/urls.py.
    # Al usar "" como prefijo, las URLs de core quedan en la raíz del sitio.
    path("", include("core.urls")),
]
