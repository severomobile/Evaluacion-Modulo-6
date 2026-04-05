"""
settings.py – Configuración central del proyecto Django.

Sigue las buenas prácticas de separación de responsabilidades:
  - Rutas construidas con BASE_DIR para portabilidad
  - INSTALLED_APPS declaradas explícitamente
  - Configuración de templates y archivos estáticos centralizada
"""

from pathlib import Path

# ---------------------------------------------------------------------------
# Rutas base
# ---------------------------------------------------------------------------
# BASE_DIR apunta a la raíz del proyecto (donde vive manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------------------------
# Seguridad
# ---------------------------------------------------------------------------
# ADVERTENCIA: en producción esta clave debe mantenerse en secreto y fuera
# del control de versiones (usa variables de entorno o .env).
SECRET_KEY = "django-insecure-alke-web-base-module6-changeme-in-production"

# DEBUG = True solo para desarrollo local. Nunca en producción.
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# ---------------------------------------------------------------------------
# Aplicaciones instaladas
# ---------------------------------------------------------------------------
INSTALLED_APPS = [
    # Apps internas de Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Aplicación creada para este proyecto
    "core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Módulo raíz de URLs del proyecto
ROOT_URLCONF = "alke_web_base.urls"


# ---------------------------------------------------------------------------
# Configuración de templates
# ---------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Django buscará templates dentro de cada app (en su carpeta templates/)
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "alke_web_base.wsgi.application"


# ---------------------------------------------------------------------------
# Base de datos
# ---------------------------------------------------------------------------
# SQLite es suficiente para desarrollo. No se utiliza en este módulo.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ---------------------------------------------------------------------------
# Internacionalización
# ---------------------------------------------------------------------------
LANGUAGE_CODE = "es-ar"
TIME_ZONE = "America/Argentina/Buenos_Aires"
USE_I18N = True
USE_TZ = True


# ---------------------------------------------------------------------------
# Archivos estáticos (CSS, JS, imágenes)
# ---------------------------------------------------------------------------
# URL pública bajo la que se sirven los estáticos en desarrollo
STATIC_URL = "static/"

# Clave primaria por defecto para nuevos modelos
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
