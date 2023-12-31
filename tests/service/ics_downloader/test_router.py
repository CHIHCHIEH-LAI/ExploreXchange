from fastapi.testclient import TestClient

from app.application import app

client = TestClient(app)

response = client.get('/download/trip/65915d3abd6eb1e6ae071420')