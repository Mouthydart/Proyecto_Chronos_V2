import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from backend.main import app
from backend.app.database.mongodb import mongodb


@pytest.fixture(scope="session", autouse=True)
def mock_mongodb():
    mock_db = MagicMock()

    mock_users = MagicMock()

    # 👇 SIMULA USUARIO REAL
    mock_users.find_one.return_value = {
        "email": "test@test.com",
        "hashed_password": "$2b$12$KIXfakehashvaluehere"
    }

    mock_db.users = mock_users

    mongodb.get_database = lambda: mock_db

    yield mock_db


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client