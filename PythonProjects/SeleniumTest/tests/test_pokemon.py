import requests
import pytest

URL = 'https://api.pokemonbattle.ru'
TOKEN = '705837f87e75dcf72675051e42363c9c'
HEADER = {'Content-type' : 'application/json', 'trainer_token': TOKEN }
TRAINER_ID = '38159'

def test_status_code():
    response = requests.get(url=f'{URL}/v2/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_trainer_id():
    response_get = requests.get(url=f'{URL}/v2/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == TRAINER_ID
