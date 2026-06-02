import pytest
from fastapi.testclient import TestClient
import mongomock
from backend.main import app
from backend.app.database.mongodb import mongodb

@pytest.fixture(scope="session", autouse=True)
def mock_mongodb():
    """
    Este fixture simula la base de datos MongoDB en memoria usando mongomock.
    Evita que las pruebas escriban en tu base de datos real.
    """
    # Si tu clase 'mongodb' expone el cliente interno (por ejemplo, mongodb.client),
    # podemos reemplazarlo por el cliente simulado de mongomock.
    # Nota: Si este mock te da problemas más adelante, ajustaremos según cómo esté programado app/database/mongodb.py
    mock_client = mongomock.MongoClient()
    
    # Intentamos inyectar el cliente simulado en tu objeto de base de datos
    original_client = getattr(mongodb, 'client', None)
    mongodb.client = mock_client
    
    yield mock_client
    
    # Al terminar los tests, restauramos el estado original si es necesario
    if original_client:
        mongodb.client = original_client

@pytest.fixture(scope="module")
def client():
    """
    Crea un TestClient de FastAPI que simula peticiones HTTP.
    Se destruye al terminar las pruebas del módulo.
    """
    # Usamos el TestClient nativo de FastAPI con un bloque 'with' 
    # para que se ejecute el código dentro de tu 'lifespan' (startup y shutdown)
    with TestClient(app) as test_client:
        yield test_client
