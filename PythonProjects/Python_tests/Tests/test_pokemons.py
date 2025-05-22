import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'bdc71a7fa5b16bab341434372ff22097' 
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN  
}
TRAINER_ID = '33466'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id' : TRAINER_ID}, headers=HEADER)
    assert response.status_code == 200

def test_trainers_name():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id' : TRAINER_ID}, headers=HEADER)
    assert response.json()['data'][0]['trainer_name'] == 'Debeli'


