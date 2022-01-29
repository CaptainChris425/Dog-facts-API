import json
from urllib import response
from fastapi.testclient import TestClient

from src.server import app

with open("./database/data.json") as json_file:
    data = json.load(json_file)
    dataLength = len(data)

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

def test_bad_request():
    response = client.get("/api/v1/resources/")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Not Found"
}

def test_api_all():
    response = client.get("/api/v1/resources/dogs/all")
    assert response.status_code == 200
    assert response.json() == data


def test_number_bad_request():
    response = client.get("/api/v1/resources/dogs")
    assert response.status_code == 404
    assert response.json() == {
	"detail": "The resource could not be found. Please check your query"
    }


def test_number_incorrect_query():
    response = client.get("/api/v1/resources/dogs?number=0&index=0")
    assert response.status_code == 404
    assert response.json() == {
	"detail": "The resource could not be found. Please check your query"
    }

def test_number():
    response = client.get("/api/v1/resources/dogs?number=1")
    assert response.status_code == 200