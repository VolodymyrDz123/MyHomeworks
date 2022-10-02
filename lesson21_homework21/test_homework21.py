import pytest
import requests


@pytest.fixture()
def pet_headers():
    return {
        'accept': 'application/xml',
        'Content-Type': 'application/json'
    }


@pytest.fixture()
def pet_info_create():
    return {
        "id": 1110,
        "name": "JsonDoggie",
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }


@pytest.fixture()
def pet_info_update():
    return {
          "id": 1110,
          "name": "JsonDoggie",
          "category": {
            "id": 1,
            "name": "Dogs"
          },
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 0,
              "name": "string"
            }
          ],
          "status": "sold"
        }


def test_session_create_update_delete(pet_headers, pet_info_create, pet_info_update):
    with requests.session() as http_session:
        http_session.headers.update(pet_headers)

        pet_post = http_session.post("https://petstore3.swagger.io/api/v3/pet", json=pet_info_create)
        assert pet_post.status_code == 200
        assert '1110' in http_session.get("https://petstore3.swagger.io/api/v3/pet/1110").text
        assert 'JsonDoggie' in http_session.get("https://petstore3.swagger.io/api/v3/pet/1110").text
        assert 'Dogs' in http_session.get("https://petstore3.swagger.io/api/v3/pet/1110").text
        assert 'available' in http_session.get("https://petstore3.swagger.io/api/v3/pet/1110").text

        pet_put = http_session.put("https://petstore3.swagger.io/api/v3/pet", json=pet_info_update)
        assert pet_put.status_code == 200
        assert 'available' not in http_session.get("https://petstore3.swagger.io/api/v3/pet/1110").text
        assert 'sold' in http_session.get("https://petstore3.swagger.io/api/v3/pet/1110").text

        pet_delete = http_session.delete("https://petstore3.swagger.io/api/v3/pet/1110")
        assert pet_delete.status_code == 200
        assert http_session.get("https://petstore3.swagger.io/api/v3/pet/1110").status_code == 404








