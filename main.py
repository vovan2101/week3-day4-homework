import requests

class Pokemon_API:
    base_url = "https://pokeapi.co/api/v2/pokemon/"

    def __init__(self, name):
        self.name = name

    def _get(self):
         pokemon_data = f"{self.base_url}{self.name}"
         pokemon_respons = requests.get(pokemon_data)
         if pokemon_respons.ok:
             return pokemon_respons.json()
         else:
             print('There was an error')

    def height_and_weight(self):
        pokemon_h_and_w = self._get()
        return f"{pokemon_h_and_w['name']}'s height is {pokemon_h_and_w['height']} and weight is {pokemon_h_and_w['weight']}"

pokemon_1 = Pokemon_API("bulbasaur")

pokemon_1.height_and_weight()