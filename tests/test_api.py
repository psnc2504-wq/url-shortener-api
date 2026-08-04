from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "running"


def test_shorten_url():

    response = client.post(
        "/shorten",
        json={
            "url": "https://www.google.com"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "short_url" in data


def test_invalid_short_code():

    response = client.get("/thisdoesnotexist")

    assert response.status_code == 404