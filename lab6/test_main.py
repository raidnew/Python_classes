import sys, os
from fastapi.testclient import TestClient
"""
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
"""
#from lab6app.main import app
from lab6app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/api/teacher")
    assert response.status_code == 200
    assert response.json() == {"status":"success","results":2,"teachers":[{"name":"ASDASD","id":1},{"name":"CXVBCXBXCBV","id":2}]}

