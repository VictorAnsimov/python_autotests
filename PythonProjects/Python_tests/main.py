import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'bdc71a7fa5b16bab341434372ff22097' 
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN  
}

# Создание
body_create = {
    "name": "generate",
    "photo_id": -1
}

response = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create)
print("Создание покемона:", response.text)  

# id покемона
pokemon_id = response.json().get('id')

# Изменение 
body_change = {
    "pokemon_id": pokemon_id,  
    "name": "Petrovich",
    "photo_id": -1
}

response = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_change)
print("Изменение покемона:", response.text)

#Поймать в покебол
body_catch = {
    "pokemon_id": pokemon_id
}

response = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_catch)
print("Пойман!" , response.text)

#найти противника
response = requests.get(url=f'{URL}/pokemons?in_pokeball=1', headers=HEADER)
print("Вот эти ребята!", response.text)

enemy_id = response.json()['data'][2]['id']



#Провести битву
body_battle = {
    "attacking_pokemon": pokemon_id,
    "defending_pokemon": enemy_id
}

response = requests.post(url=f'{URL}/battle', headers=HEADER, json=body_battle)
print("Кто же?!", response.text)


#Нокаутировать
body_knock = {
    "pokemon_id": pokemon_id
}

response = requests.post(url=f'{URL}/pokemons/knockout' , headers=HEADER, json=body_knock)
print("Хорошая битва!", response.text)
