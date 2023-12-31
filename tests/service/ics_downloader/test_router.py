from fastapi.testclient import TestClient

from app.application import app

client = TestClient(app)

response = client.get('/download/trip/65915d3abd6eb1e6ae071420')

file_path = 'tests/service/ics_downloader/trip65915d3abd6eb1e6ae071420.ics'

with open(file_path, "wb") as f:
    f.write(response.content)