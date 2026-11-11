from fastapi.testclient import TestClient

from app.api import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "running"}


def test_chat_endpoint():
    response = client.post(
        "/chat",
        json={"message": "How can I check banking hours?"}
    )

    assert response.status_code == 200
    assert "response" in response.json()
