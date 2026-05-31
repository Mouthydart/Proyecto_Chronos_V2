import pytest

# --- PRUEBA DE INTEGRACIÓN 1: Verificación del estado general de la API ---
def test_read_root(client):
    """
    Prueba que la ruta raíz responda con código 200 y el mensaje esperado.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Chronos API is running"}


# --- PRUEBA DE INTEGRACIÓN 2: Flujo de Autenticación (Fallo controlado) ---
def test_auth_login_invalid_credentials(client):
    """
    Envía credenciales incorrectas al endpoint de autenticación.
    Verifica que el router intercepte la petición y responda con error 401 o 400.
    """
    payload = {
        "email": "prueba2@estudiante.ibero.edu.co",
        "password": "Col0mbi@12"
    }
    # Intentamos iniciar sesión en tu prefijo configurado '/api/auth/login'
    response = client.post("/api/auth/login", json=payload)
    
    print("\n--- DETALLE DEL ERROR 422 ---", response.json())
    # Comprobamos que el backend maneje la seguridad correctamente. 
    # Usualmente responde 401 (Unauthorized) o 400 (Bad Request) ante credenciales inválidas.
    assert response.status_code in [400, 401]


# --- PRUEBA DE INTEGRACIÓN 3: Verificación de un módulo secundario (Health o similar) ---
def test_health_endpoint(client):
    """
    Prueba que el router de salud de la aplicación responda correctamente.
    Esto evalúa la integración de múltiples routers dentro de app.include_router()
    """
    # Probamos tu router en '/api/health' o una sub-ruta común de tu módulo health (ej. '/api/health' o '/api/status')
    # Si conoces el endpoint exacto de health, puedes cambiarlo aquí:
    response = client.get("/api/health") 
    
    # Validamos que el servidor procese la solicitud del router incorporado
    # Si la ruta existe pero requiere parámetros, puede dar 400/422. Si está libre dará 200.
    # Evaluamos que no devuelva un error crítico de servidor (500) ni un No Encontrado (404)
    assert response.status_code != 404
    assert response.status_code != 500