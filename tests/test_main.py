from fastapi.testclient import TestClient
from app.main import app, addition

client = TestClient(app)


def test_addition():
    assert addition(10, 20) == 30


def test_addition_negative():
    assert addition(-5, 5) == 0


def test_addition_decimal():
    assert addition(2.5, 3.5) == 6.0


def test_add_api_post():
    response = client.post(
        "/add",
        json={"num1": 10, "num2": 20}
    )
    assert response.status_code == 200
    assert response.json()["addition"] == 30


def test_add_api_get():
    # Test GET /add with query params
    response = client.get("/add?num1=15&num2=25")
    assert response.status_code == 200
    assert response.json()["addition"] == 40

    # Test GET /add without params (returns helpful message, not 405 Method Not Allowed)
    response_no_params = client.get("/add")
    assert response_no_params.status_code == 200
    assert "example_url" in response_no_params.json()


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to Addition API"
