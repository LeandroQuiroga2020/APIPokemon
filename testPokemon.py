import unittest
import requests
import json



class TestPokemon(unittest.TestCase):  
    def test_search_pokemon(self):
        pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/kakuna')  
        my_pokemon = pokemon.json()      #pido el json de la pagina

        print(pokemon.status_code)  # trae el status, si  esta todo bien trae 200

        with open(r"C:\Users\LeandroQA\Desktop\ProyectoAutomatizacion\PokemonAPI\kakuna.json") as kakuna:  #tuve que poner el path completo porque no lo tomaba
            data = json.load(kakuna)

        #movimientos = ['string-shot','harden','iron-defense','bug-bite','electroweb'] lo guardo en el archivo kakuna.json
        #print(my_pokemon)   # me trae todo el json
        print(my_pokemon['name'])
        print(my_pokemon['weight'])
       # print(my_pokemon['move']['name']) esta mal porque tengo que recorrer a traves de un for

        self.assertEqual(200,pokemon.status_code)

        self.assertEqual(data['weight'],my_pokemon['weight'])  # data['weight'] lo saca del archivo kakuna.json lo compara con my_pokemon['weight'] que es dew la API

        for i in my_pokemon['moves']:
            print(i['move']['name'])  
            self.assertTrue(i['move']['name'] in data['moves'])  #comparo datos con datos dentro del JSON ,data['moves']  lo saca del archivo kakuna.json con los de la pagina de la API 'https://pokeapi.co/api/v2/pokemon/kakuna'
    


    def test_search_pokemon_by_number(self):
        pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/1')  
        my_pokemon = pokemon.json()

        self.assertEqual(200,pokemon.status_code)

        self.assertEqual('bulbasaur',my_pokemon['name'])


if __name__ == '__main__':
    unittest.main()
