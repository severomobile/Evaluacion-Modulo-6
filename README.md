# Alke Web Base 🚀

Proyecto de evaluación del **Módulo 6 – Desarrollo Web con Django: Fundamentos**


---

## Descripción

Aplicación web básica construida con Django que demuestra:

- Configuración de un proyecto Django desde cero
- Creación y registro de una aplicación (`core`)
- Sistema de enrutamiento a dos niveles (proyecto + app)
- Vistas basadas en funciones con contextos dinámicos
- Templates HTML con herencia de plantilla base (`base.html`)
- Archivos estáticos con CSS personalizado y variables CSS

---

## Stack tecnológico

| Tecnología | Versión |
|------------|---------|
| Python     | 3.10+   |
| Django     | 4.2+    |
| HTML       | 5       |
| CSS        | 3       |

---

## Estructura del proyecto

```
alke_web_base/
│
├── manage.py                    # Utilidad de gestión de Django
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Este archivo
│
├── alke_web_base/               # Paquete de configuración del proyecto
│   ├── __init__.py
│   ├── settings.py              # Configuración general
│   ├── urls.py                  # Enrutamiento raíz
│   └── wsgi.py                  # Punto de entrada WSGI
│
└── core/                        # Aplicación principal
    ├── __init__.py
    ├── apps.py                  # Configuración de la app
    ├── views.py                 # Lógica de las vistas
    ├── urls.py                  # Rutas de la app
    │
    ├── templates/
    │   └── core/
    │       ├── base.html        # Template padre (layout global)
    │       ├── home.html        # Página de inicio
    │       ├── about.html       # Página Acerca de
    │       └── contacto.html    # Página de contacto
    │
    └── static/
        └── core/
            └── css/
                └── styles.css   # Estilos globales
```

---

## Instalación y configuración

### 1. Clonar o descomprimir el proyecto

```bash
# Si se descargó como .zip:
unzip alke_web_base.zip
cd alke_web_base
```

### 2. Crear y activar el entorno virtual

```bash
# Crear el entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en macOS / Linux
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones (base de datos)

```bash
python manage.py migrate
```

### 5. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

Abrí el navegador en: **http://127.0.0.1:8000/**

---

## Páginas disponibles

| Ruta          | Vista       | Descripción               |
|---------------|-------------|---------------------------|
| `/`           | `home`      | Página principal          |
| `/acerca-de/` | `about`     | Información del equipo    |
| `/contacto/`  | `contacto`  | Datos de contacto         |
| `/admin/`     | Admin panel | Panel de administración   |

---

## Flujo de funcionamiento de Django (MTU)

```
Browser  →  urls.py (proyecto)  →  urls.py (core app)
         →  views.py (función)
         →  template HTML + contexto
         →  HttpResponse  →  Browser
```

1. El navegador hace una petición HTTP a una URL.
2. Django consulta `alke_web_base/urls.py` y delega a `core/urls.py`.
3. La ruta matcheada llama a la función de vista correspondiente.
4. La vista construye un **contexto** (diccionario con datos).
5. `render()` combina el template HTML con el contexto.
6. Django devuelve el HTML generado al navegador.

---

## Crear un superusuario (admin)

```bash
python manage.py createsuperuser
```

Luego accede a http://127.0.0.1:8000/admin/

---

## Capturas de pantalla 📸

Las capturas del proyecto en ejecución se encuentran en la carpeta [`/capturas`](./capturas).

| Página | Archivo |
|--------|---------|
| Inicio | [ver captura](./capturas/home.png) |
| Acerca de | [ver captura](./capturas/about.png) |
| Contacto | [ver captura](./capturas/contacto.png) |