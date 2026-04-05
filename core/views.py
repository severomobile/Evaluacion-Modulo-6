"""
views.py – Vistas de la aplicación 'core'.

Cada vista es una función que:
  1. Recibe un objeto HttpRequest.
  2. Ejecuta la lógica de negocio.
  3. Retorna un HttpResponse (generalmente renderizando un template).

Principios aplicados:
  - Single Responsibility: cada vista tiene una única responsabilidad.
  - Contextos tipados como dicts para legibilidad.
  - Uso de render() como helper principal de Django.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# ---------------------------------------------------------------------------
# Datos de ejemplo (en un proyecto real vendrían de la base de datos)
# ---------------------------------------------------------------------------
SERVICIOS = [
    {
        "titulo": "Desarrollo Web",
        "descripcion": "Construcción de aplicaciones web modernas con Django.",
        "icono": "🌐",
    },
    {
        "titulo": "APIs REST",
        "descripcion": "Diseño e implementación de APIs robustas y escalables.",
        "icono": "🔗",
    },
    {
        "titulo": "Consultoría",
        "descripcion": "Asesoramiento técnico en arquitectura de software.",
        "icono": "💡",
    },
]

EQUIPO = [
    {"nombre": "Ana García",    "rol": "Lead Developer",    "emoji": "👩‍💻"},
    {"nombre": "Carlos López",  "rol": "Backend Engineer",  "emoji": "👨‍💻"},
    {"nombre": "Sofía Martínez","rol": "UX Designer",       "emoji": "🎨"},
]


# ---------------------------------------------------------------------------
# Vistas
# ---------------------------------------------------------------------------

def home(request: HttpRequest) -> HttpResponse:
    """
    Vista principal (Homepage).

    Renderiza la página de inicio con la lista de servicios disponibles.
    Cualquier dato dinámico se inyecta al template a través del contexto.
    """
    context = {
        "titulo_pagina": "Inicio",
        "bienvenida": "Bienvenido a Alke Web Base",
        "descripcion": (
            "Una aplicación web construida con Django, "
            "demostrando los fundamentos del framework."
        ),
        "servicios": SERVICIOS,
    }
    return render(request, "core/home.html", context)


def about(request: HttpRequest) -> HttpResponse:
    """
    Vista 'Acerca de'.

    Muestra información sobre la empresa y el equipo de desarrollo.
    """
    context = {
        "titulo_pagina": "Acerca de",
        "subtitulo": "Conocé nuestro equipo",
        "descripcion_empresa": (
            "Alke Solutions es una empresa de desarrollo de software "
            "dedicada a construir soluciones web de alta calidad."
        ),
        "equipo": EQUIPO,
        "tecnologias": ["Python", "Django", "HTML5", "CSS3"],
    }
    return render(request, "core/about.html", context)


def contacto(request: HttpRequest) -> HttpResponse:
    """
    Vista 'Contacto'.

    Página de contacto con información estática.
    En módulos futuros se integrará con formularios y modelos.
    """
    context = {
        "titulo_pagina": "Contacto",
        "email": "contacto@alkesolutions.com",
        "telefono": "+54 11 1234-5678",
        "direccion": "Buenos Aires, Argentina",
    }
    return render(request, "core/contacto.html", context)
