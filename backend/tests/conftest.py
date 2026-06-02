import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from backend.main import app
from backend.app.database.mongodb import mongodb
from backend.app.auth.auth import get_password_hash  # 👈 IMPORTANTE


@pytest.fixture(scope="session", autouse=True)
def mock_mongodb():
    mock_db = MagicMock()

    mock_users = MagicMock()

    # ✅ HASH REAL BCRYPT (NO FAKE)
    mock_users.find_one.return_value = {
        "email": "test@test.com",
        "hashed_password": get_password_hash("password123")
    }

    mock_db.users = mock_users

    mongodb.get_database = lambda: mock_db

    yield mock_db


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client