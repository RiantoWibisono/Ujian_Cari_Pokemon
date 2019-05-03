# 3 - Cari Pokemon

from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__, static_url_path='')

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/hasil', methods = ['GET', 'POST'])
def hasil():
    namaPokemon = request.form['nama']
    url = 'https://pokeapi.co/api/v2/pokemon/'
    dataPokemon = requests.get(url+namaPokemon)
    pokedex = 'https://pokeapi.co/api/v2/pokedex/1/'
    dataPokedex = requests.get(pokedex)
    for i in range(len(dataPokedex.json()['pokemon_entries'])):
        if namaPokemon == dataPokedex.json()['pokemon_entries'][i]['pokemon_species']['name']:
            return render_template('hasil.html', dataPokemon = dataPokemon)
    else:
        return render_template('error.html')

@app.errorhandler(404)
def notFound(error):            
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug = True)