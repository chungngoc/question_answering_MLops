from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.mark.slow
def test_predict_endpoint():
    # Sample input for testing
    payload = {
        "question": "What is the capital of France?",
        "context": "France is a country in Europe. The capital of France is Paris."
    }
    
    # Send POST request to the /predict endpoint
    response = client.post("/predict", json=payload)
    
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Check if the response contains the expected answer
    data = response.json()
    assert "answer" in data
    assert data["answer"] == "Paris"
    assert "score" in data
    assert isinstance(data["answer"], str)
    assert data["score"] >= 0 and data["score"] <= 1

def test_version_endpoint():
    response = client.get("/version")
    assert response.status_code == 200

    data = response.json()
    assert "app" in data
    assert "version" in data
    assert "env" in data
    assert "model" in data
