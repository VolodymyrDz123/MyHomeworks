import requests
import pytest


@pytest.fixture()
def headers():
    return {
        'accept': 'application/xml',
        'Content-Type': 'application/json'
    }


@pytest.fixture()
def pet_info_json():
    yield {
           "id": 11,
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
    requests.delete("https://petstore3.swagger.io/api/v3/pet/11")


@pytest.fixture()
def pet_info_xml():
    pet_info_text = """
            {
              "id": 10,
              "name": "TextDoggie",
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
            """
    yield pet_info_text
    requests.delete("https://petstore3.swagger.io/api/v3/pet/10")


@pytest.fixture()
def post_pet(headers, pet_info_json):
    requests.post(f"https://petstore3.swagger.io/api/v3/pet", headers=headers, json=pet_info_json)
    yield
    requests.delete("https://petstore3.swagger.io/api/v3/pet/11")


@pytest.mark.parametrize("status, response_code", [("available", 200),
                                                   ("pending", 200),
                                                   ("sold", 200),
                                                   ("", 400)])
def test_get_status(status, response_code):
    pet_status = requests.get(f"https://petstore3.swagger.io/api/v3/pet/findByStatus?status={status}")
    assert pet_status.status_code == response_code


def test_post_pet_xml(pet_info_xml, headers):
    pet_status = requests.post(f"https://petstore3.swagger.io/api/v3/pet", headers=headers, data=pet_info_xml)
    assert pet_status.status_code == 200


def test_post_pet_json(pet_info_json, headers):
    pet_status = requests.post(f"https://petstore3.swagger.io/api/v3/pet", headers=headers, json=pet_info_json)
    assert pet_status.status_code == 200


def test_post_pet_input_error(headers):
    pet_status = requests.post(f"https://petstore3.swagger.io/api/v3/pet", headers=headers, json={"id": "f"})
    assert pet_status.status_code == 400


def test_put_pet(headers, pet_info_json, post_pet):
    pet_put = requests.put("https://petstore3.swagger.io/api/v3/pet", headers=headers, json=pet_info_json)
    assert pet_put.status_code == 200


def test_put_not_found(headers, pet_info_json):
    pet_put = requests.put("https://petstore3.swagger.io/api/v3/pet", headers=headers, json={
                                                                                              "id": 1464,
                                                                                              "name": "doggdssa1sgie",
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
                                                                                            })
    assert pet_put.status_code == 404


def test_put_invalid_id(headers, pet_info_json):
    pet_put = requests.put("https://petstore3.swagger.io/api/v3/pet", headers=headers, json={"id": "dasf"})
    assert pet_put.status_code == 400
