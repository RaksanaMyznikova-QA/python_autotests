import requests
import pytest

def test_status_code():
    token = '996be895cb3582302596e270623b4b92'
    response = requests.get('https://pokemonbattle.me:9104/trainers', headers={'trainer_token': token}, json={
    "trainer_id": "4202"
})
    assert response.status_code == 200

def test_part_of_body():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params={'trainer_id': 4202})
    assert response.json()['trainer_name'] == 'URL' 