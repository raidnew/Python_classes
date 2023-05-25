from fastapi.testclient import TestClient
import lab6app

client = TestClient(lab6app)

def test_root():
    response = client.get("/api/teacher")
    assert response.status_code == 200
    assert response.json() == {"status":"success","results":0,"teachers":[]}

