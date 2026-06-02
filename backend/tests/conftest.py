import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from backend.main import app
from backend.app.database.mongodb import mongodb


@pytest.fixture(scope="session", autouse=True)
def mock_mongodb():
    """
    Mock global de MongoDB para evitar conexión real.
    """
    mock_db = MagicMock()

    # Simular colecciones
    mock_db.users = MagicMock()
    mock_db.academy = MagicMock()
    mock_db.finance = MagicMock()
    mock_db.health = MagicMock()
    mock_db.leisure = MagicMock()

    # Reemplazar get_database
    mongodb.get_database = lambda: mock_db

    yield mock_db


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client