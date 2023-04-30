import requests
import pytest 

response = requests.post('https://pokemonbattle.me:9104/trainers/reg', json={
    "trainer_token": "996be895cb3582302596e270623b4b92",
    "email": "ill-raksana-myznikova@qa.studio",
    "password": "yRkaRNTibHJ1hgswbwlk"
})

print(response.text)

token = "996be895cb3582302596e270623b4b92"

response_activated = requests.post('https://pokemonbattle.me:9104/trainers/confirm_email', json={
    "trainer_token": token
})

print(response_activated.text)

base_url = 'https://pokemonbattle.me:9104/'

response_add_pokemon = requests.post(f'{base_url}pokemons', headers={'trainer_token': token}, json={
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})

print(response_add_pokemon.text)

response_new_name = requests.put(f'{base_url}pokemons', headers={'trainer_token': token}, json={
    "pokemon_id": "9710",
    "name": "Покемошка",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})

print(response_new_name.text)

response_add_pokeball = requests.post(f'{base_url}trainers/add_pokeball', headers={'trainer_token': token}, json={
    "pokemon_id": "9710"
})

print(response_add_pokeball.text)
