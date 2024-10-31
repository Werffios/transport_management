# Sistema de Gestión de Transporte

## Descripción del Proyecto

El Sistema de Gestión de Transporte es una aplicación web desarrollada con Django que permite gestionar rutas, vehículos y la asignación de vehículos a rutas específicas. El proyecto sigue las mejores prácticas de Django y de la industria, con una estructura modular y organizada que facilita su comprensión, mantenimiento y escalabilidad. Hemos mejorado el diseño de la interfaz de usuario actualizando el archivo CSS, proporcionando una apariencia más moderna y agradable sin necesidad de modificar los archivos HTML existentes.

### Características Principales

- **Gestión de Rutas**: Crear, editar, listar y eliminar rutas con información detallada.
- **Gestión de Vehículos**: Administrar vehículos con detalles como número de placa, estado y tipo.
- **Asignación de Vehículos**: Asignar vehículos a rutas según reglas de negocio predefinidas.
- **Registro de Asignaciones**: Visualizar y filtrar el historial de asignaciones realizadas.

### Estructura del Proyecto

\```
transport_management/
├── manage.py
├── README.md
├── requirements.txt
├── transport_management/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── __init__.py
│   ├── routes/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── templates/
│   │   │   └── routes/
│   │   │       ├── route_confirm_delete.html
│   │   │       ├── route_form.html
│   │   │       └── route_list.html
│   │   └── migrations/
│   ├── vehicles/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── templates/
│   │   │   └── vehicles/
│   │   │       ├── vehicle_confirm_delete.html
│   │   │       ├── vehicle_form.html
│   │   │       └── vehicle_list.html
│   │   └── migrations/
│   └── assignments/
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── forms.py
│       ├── views.py
│       ├── urls.py
│       ├── templates/
│       │   └── assignments/
│       │       ├── assign_vehicle.html
│       │       ├── assignment_log_list.html
│       │       └── assignment_success.html
│       └── migrations/
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── scripts.js
└── templates/
    └── base.html
\```

## Requisitos Previos
- Python 3.6 o superior
- Pip
- Virtualenv (opcional pero recomendado)

## Instalación y Ejecución
1. **Clonar el Repositorio**
    ```bash
    git clone https://github.com/tu_usuario/transport_management.git
    cd transport_management
    ```
2. **Crear y Activar un Entorno Virtual**
    ```bash
    # Crear el entorno virtual
    python -m venv env

    # Activar el entorno virtual
    source env/bin/activate  # En Windows: env\Scripts\activate
    ```
3. **Instalar Dependencias**
    ```bash
    pip install -r requirements.txt
    ```
4. **Aplicar Migraciones de Base de Datos**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5. **Crear un Superusuario**
    ```bash
    python manage.py createsuperuser
    ```
    Sigue las instrucciones en la terminal para crear un nombre de usuario y contraseña.

6. **Ejecutar el Servidor de Desarrollo**
    ```bash
    python manage.py runserver
    ```
    La aplicación estará disponible en [http://localhost:8000/](http://localhost:8000/).

## Uso de la Aplicación
### Acceder al Panel de Administración
Visita [http://localhost:8000/admin/](http://localhost:8000/admin/) e inicia sesión con el superusuario creado para acceder al panel de administración de Django.

### Navegar por la Aplicación
- **Rutas**: [http://localhost:8000/routes/](http://localhost:8000/routes/)
- **Vehículos**: [http://localhost:8000/vehicles/](http://localhost:8000/vehicles/)
- **Asignar Vehículo a Ruta**: [http://localhost:8000/assignments/assign/](http://localhost:8000/assignments/assign/)
- **Registro de Asignaciones**: [http://localhost:8000/assignments/logs/](http://localhost:8000/assignments/logs/)

## Arquitectura del Proyecto
La aplicación está dividida en tres aplicaciones principales dentro del directorio `apps/`:

- **routes**: Maneja todo lo relacionado con las rutas.
- **vehicles**: Maneja todo lo relacionado con los vehículos.
- **assignments**: Maneja la lógica de asignación y el registro de asignaciones.

Cada aplicación contiene sus propios:
- **Modelos (`models.py`)**: Definiciones de las estructuras de datos.
- **Vistas (`views.py`)**: Lógica de la interfaz de usuario y operaciones CRUD.
- **URLs (`urls.py`)**: Enrutamiento específico de la aplicación.
- **Plantillas (`templates/`)**: Archivos HTML para la representación visual.
- **Migraciones (`migrations/`)**: Control de cambios en los modelos.

Las plantillas están organizadas por aplicación y extienden de una plantilla base común ubicada en `templates/base.html`. Los archivos estáticos, como hojas de estilo y scripts, se encuentran en el directorio `static/`.

## Mejoras en el Diseño (CSS)
El archivo de estilos CSS (`static/css/styles.css`) ha sido mejorado para ofrecer una interfaz más atractiva y moderna. Las mejoras incluyen:
- **Tipografías Modernas**: Uso de fuentes como 'Roboto' para mejorar la legibilidad.
- **Paleta de Colores**: Colores armoniosos y profesionales para una mejor experiencia visual.
- **Diseño Responsivo**: Adaptación de la interfaz para diferentes tamaños de pantalla.
- **Estilos para Formularios y Tablas**: Apariencia refinada para elementos interactivos sin modificar el HTML.

## Funcionalidades Clave
### Gestión de Rutas
- **Crear Ruta**: Añadir nuevas rutas con detalles como nombre, origen, destino, distancia y tipo.
- **Editar Ruta**: Modificar información existente de una ruta.
- **Eliminar Ruta**: Eliminar rutas que ya no sean necesarias.
- **Listar Rutas**: Ver todas las rutas registradas en el sistema.

### Gestión de Vehículos
- **Crear Vehículo**: Registrar nuevos vehículos con detalles específicos.
- **Editar Vehículo**: Actualizar información de vehículos existentes.
- **Eliminar Vehículo**: Quitar vehículos del sistema.
- **Listar Vehículos**: Visualizar todos los vehículos registrados.

### Asignación de Vehículos a Rutas
- **Asignar Vehículo**: Asignar un vehículo disponible a una ruta siguiendo reglas de negocio.
- **Validación**: Asegurar que el tipo de vehículo coincide con el tipo de ruta.
- **Registro de Asignaciones**: Mantener un historial de todas las asignaciones realizadas.

### Registro de Asignaciones
- **Listar Asignaciones**: Ver el historial completo de asignaciones.
- **Filtrar por Matrícula**: Buscar asignaciones específicas mediante el número de placa del vehículo.

## Reglas de Negocio para Asignaciones
La asignación de vehículos a rutas se basa en las siguientes reglas:
- **PAVEMENT**: Solo vehículos de tipo BUS.
- **POTHOLES**: Solo vehículos de tipo TRUCK.
- **DIRT**: Solo vehículos de tipo CAR.
- **TRAIL**: Solo vehículos de tipo SUV.

Si se intenta asignar un vehículo a una ruta que no cumple con estas reglas, el sistema mostrará un mensaje de error.

## Contribución
Las contribuciones al proyecto son bienvenidas. Puedes hacerlo a través de pull requests o abriendo issues para reportar errores y sugerir mejoras.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto