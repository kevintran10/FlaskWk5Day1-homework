from flask import request, render_template
import requests
from app import app

@app.route('/')
@app.route('/home')
def pokemon_home():
    return '<h1>Welcome to the Pokedex!</h1>'


@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon_details():
    if request.method == 'POST':
        pokemon_name = request.form.get('pokemon_name')
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'

        response = requests.get(url)
        data = response.json()
        all_pokemon = get_pokemon_database(data)
        return render_template('pokelogin.html', all_pokemon=all_pokemon)
    else:
        return render_template('pokelogin.html')

def get_pokemon_database(data):
    for pokemon in data:
        new_pokemon_data = []
        pokemon_dictionary = {
            'name' : data['forms'][0]['name'],
            'ability_name' : data['abilities'][0]['ability']['name'],
            'base_experience' : data['base_experience'],
            'sprites' : data['sprites']['front_shiny'],
            'attack_base_stat' : data['stats'][1]['base_stat'],
            'hp_base_stat' : data['stats'][0]['base_stat'],
            'defense_base_stat' : data['stats'][2]['base_stat']
        }
        new_pokemon_data.append(pokemon_dictionary)
        return new_pokemon_data