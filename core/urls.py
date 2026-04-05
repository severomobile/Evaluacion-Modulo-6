"""
urls.py – Enrutamiento de la aplicación 'core'.

Buena práctica: cada app gestiona sus propias rutas.
El proyecto las incluye vía include() en su urls.py raíz.

Uso de app_name para namespacing: permite referenciar URLs
como 'core:home' en lugar de solo 'home', evitando colisiones
cuando el proyecto escala con múltiples apps.
"""

from django.urls import path
from . import views

# Namespace de la aplicación (útil para {% url 'core:home' %} en templates)
app_name = "core"

urlpatterns = [
    # Ruta raíz → Vista home
    path("", views.home, name="home"),

    # Ruta /acerca-de/ → Vista about
    path("acerca-de/", views.about, name="about"),

    # Ruta /contacto/ → Vista contacto
    path("contacto/", views.contacto, name="contacto"),
]
