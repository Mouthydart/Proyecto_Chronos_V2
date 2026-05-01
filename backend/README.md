# Chronos Backend API

Backend para la aplicación Chronos construido con FastAPI y MongoDB.

## 🚀 Características

- **Autenticación JWT** para usuarios
- **CRUD completo** para 4 áreas de vida:
  - 📚 Academia/Estudios
  - 🏥 Salud
  - 💰 Finanzas  
  - 🎮 Tiempo Libre
- **Base de datos MongoDB**
- **CORS configurado** para frontend Vue.js

## 📋 Requisitos

- Python 3.8+
- MongoDB (local o MongoDB Atlas)
- Entorno virtual activado

## 🛠️ Instalación

1. Crear y activar entorno virtual:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar variables de entorno en `.env`:
```env
MONGODB_URI=mongodb://localhost:27017/chronos_db
SECRET_KEY=tu_secreto_super_seguro_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 🚀 Ejecutar Servidor

```bash
python main.py
```

El servidor correrá en: **http://localhost:8000**

## 📚 Documentación API

Una vez iniciado el servidor, visita:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔗 Endpoints Principales

### Autenticación
- `POST /api/auth/register` - Registrar usuario
- `POST /api/auth/login` - Iniciar sesión

### Áreas de Vida (requieren autenticación)
- `GET /api/academy` - Listar registros académicos
- `POST /api/academy` - Crear registro académico
- `PUT /api/academy/{id}` - Actualizar registro
- `DELETE /api/academy/{id}` - Eliminar registro

Mismos endpoints para:
- `/api/health` - Salud
- `/api/finance` - Finanzas  
- `/api/leisure` - Tiempo Libre

## 🔐 Autenticación

Usa JWT Bearer Token. Incluye el token en el header:
```
Authorization: Bearer <tu_token>
```

## 📊 Estructura de Datos

### Academia
- title, description, subject
- priority (alta/media/baja)
- due_date, status

### Salud  
- title, description, category
- category (ejercicio/nutricion/medicacion/consulta/mental)
- priority, due_date, status

### Finanzas
- title, description, type, amount
- type (ingreso/gasto/ahorro/inversion)
- category (salario/comida/transporte/etc)
- priority, due_date, status

### Tiempo Libre
- title, description, category
- category (deportes/lectura/videojuegos/social/viajes/otros)
- priority, due_date, status
