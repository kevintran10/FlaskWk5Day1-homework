from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def pokemon_home():
    return '<h1>Welcome to the Pokedex!</h1>'


@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon_details():
    if request.method == 'POST':
    
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'

        response = requests.get(url)
        response.status_code
        data = response.json()
        all_pokemon = get_pokemon_database('data')
    else:
        return render_template('pokelogin.html', all_pokemon=all_pokemon)

def get_pokemon_database(data):
    pokemon_dictionary = {
        'name' : data['forms'][0]['name'],
        'ability_name' : data['abilities'][0]['ability']['name'],
        'base_experience' : data['base_experience'],
        'sprites' : data['sprites']['front_shiny'],
        'attack_base_stat' : data['stats'][1]['base_stat'],
        'hp_base_stat' : data['stats'][0]['base_stat'],
        'defense_base_stat' : data['stats'][2]['base_stat']
    }
    return pokemon_dictionary