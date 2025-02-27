from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_check_pico_placa_allowed():
    response = client.post("/predictor/check", json={"plate_number": "ABC-1234", "date": "2025-02-28", "time": "10:00"})
    assert response.status_code == 200
    assert response.json()["can_drive"] == True

def test_check_pico_placa_restricted():
    response = client.post("/predictor/check", json={"plate_number": "ABC-1231", "date": "2025-02-24", "time": "08:00"})
    assert response.status_code == 200
    assert response.json()["can_drive"] == False