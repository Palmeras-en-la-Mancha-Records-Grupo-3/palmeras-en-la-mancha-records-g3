# Palmeras en la Mancha Records - Backend (Grupo 3)

Este es el backend del proyecto **palmeras-en-la-mancha-records-g3**, desarrollado en **Python** utilizando **FastAPI**. El sistema implementa una arquitectura modular limpia y utiliza **Alembic** para el control de versiones y migraciones de la base de datos de forma genérica.

## 🛠️ Tecnologías Utilizadas

* **Python 3.x**: Lenguaje de programación principal.
* **FastAPI**: Framework web asíncrono de alto rendimiento para la construcción de la API.
* **Alembic**: Herramienta de migraciones de base de datos para SQLAlchemy.
* **Pydantic**: Validación de datos y esquemas.

## 📂 Estructura del Proyecto

```text
├── alembic/                  # Configuraciones y scripts de migración de Alembic
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── backend/
│   ├── config/               # Configuraciones globales y variables de entorno
│   ├── controller/           # Lógica de negocio y controladores de las rutas
│   ├── database/             # Conexión y sesión de la base de datos
│   ├── model/                # Modelos ORM (SQLAlchemy)
│   ├── routes/               # Definición de endpoints (genres, format, branches, etc.)
│   ├── schema/               # Esquemas de validación Pydantic (Request/Response)
│   └── main.py               # Punto de entrada de la aplicación FastAPI
├── .gitignore
├── alembic.ini               # Archivo de configuración maestro de Alembic
└── requirements.txt          # Dependencias del proyecto
```

## 🚀 Instalación y Configuración Local

### 1. Clonar el repositorio e ingresar a la carpeta
```bash
git clone <url-del-repositorio>
cd palmeras-en-la-mancha-records-g3
```

### 2. Crear y activar un entorno virtual
* **En Windows:**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
* **En macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar las Variables de Entorno
Crea un archivo `.env` en la raíz del proyecto para definir la conexión de tu base de datos y configuraciones:
```ini
DATABASE_URL=postgresql://usuario:password@localhost:5432/palmeras_records
# O tu cadena de conexión correspondiente
```

### 5. Ejecutar las Migraciones de Base de Datos
Para actualizar tu base de datos local al último estado con Alembic:
```bash
alembic upgrade head
```

### 6. Iniciar el Servidor de Desarrollo
Ejecuta el backend con recarga automática usando Uvicorn:
```bash
uvicorn backend.main:app --reload
```
* La API estará disponible en: `http://127.0.0.1:8000`
* Documentación interactiva (Swagger UI): `http://127.0.0`