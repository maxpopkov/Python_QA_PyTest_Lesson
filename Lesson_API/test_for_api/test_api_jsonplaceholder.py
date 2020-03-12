"""Тесты для jsonplaceholder"""
import pytest
from jsonschema import validate


def test_api_status(api_client):
    response = api_client.get()
    assert response.ok


@pytest.mark.parametrize('userid', [1, 10])
def test_api_filtering(api_client, userid):
    response = api_client.get(path='/posts', params={'userId': userid})
    assert response.json() != []


@pytest.mark.parametrize('invalid_userid', [-1, 0, 11])
def test_api_invalid_filtering(api_client, invalid_userid):
    response = api_client.get(path='/posts', params={'userId': invalid_userid})
    assert response.json() == []


@pytest.mark.parametrize('input_id, output_id',
                         [
                             (101, '101'),
                             (-1, '-1'),
                             (0, '0')
                         ])
@pytest.mark.parametrize('input_body, output_body',
                         [
                             ('test_body', 'test_body'),
                             ('!@#$', '!@#$'),
                             (200, '200')
                         ])
def test_api_create_resource(api_client, input_id, output_id, input_body, output_body):
    response = api_client.post(path='/posts',
                               data={'title': 'foo',
                                     'body': input_body,
                                     'userId': input_id}).json()
    assert response['title'] == 'foo'
    assert response['body'] == output_body
    assert response['userId'] == output_id


def test_api_json_schema(api_client):
    response = api_client.get(path='/albums/1')

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "title": {"type": "string"},
            "userId": {"type": "number"}
        },
        "required": ["id", "title", "userId"]
    }

    validate(instance=response.json(), schema=schema)
