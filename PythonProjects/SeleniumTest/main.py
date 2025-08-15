import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = '705837f87e75dcf72675051e42363c9c'
HEADER = {'Content-type' : 'application/json', 'trainer_token': TOKEN }

body_create = {
    "name": "generate",
    "photo_id": -1
}


response_create = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

poke_id = response_create.json()['id']
print(poke_id)


body_change = {
    "pokemon_id": poke_id,
    "name": "generate",
    "photo_id": -1
}

response_change = requests.put(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_change)
print(response_change.json())

body_pokeball = {
    "pokemon_id": poke_id
}

response_pokeball = requests.post(url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.json())