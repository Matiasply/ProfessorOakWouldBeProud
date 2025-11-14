import requests

'''Coleta de dados da PokéAPI e salvamento em Csv.
   irei fazer um loop para pegar os 151 primeiros pokémons
   referentes a Kanto.'''

def main():

    url_base = "https://pokeapi.co/api/v2/pokemon/"
    pokemons = []

    for i in range(1, 152):
        url = f'{url_base}{i}/'
        response = requests.get(url)
        if (response.status_code == 200):
            data = response.json()
            # Criamos um dicionário com as informações desejadas de cada pokémon
            pokemon_info = {
                'Pokédex': data['id'],
                'Nome': data['name'],
                'Tipo1': data['types'][0]['type']['name'],
                'Tipo2': data['types'][1]['type']['name'] if len(data['types']) > 1 else '',
                'Altura': data['height'],
                'Peso': data['weight'],
                'HP': data['stats'][0]['base_stat'],
                'Ataque': data['stats'][1]['base_stat'],
                'Defesa': data['stats'][2]['base_stat'],
                'Ataque Especial': data['stats'][3]['base_stat'],
                'Defesa Especial': data['stats'][4]['base_stat'],
                'Velocidade': data['stats'][5]['base_stat']
            }
            pokemons.append(pokemon_info)
        else:
            print(f'Erro ao buscar dados para o Pokémon ID {i}')

    with open('pokemons_kanto.csv', 'w') as file:
        # Escreve o cabeçalho do CSV
        file.write('Pokédex,Nome,Tipo1,Tipo2,Altura,Peso,HP,Ataque,Defesa,Ataque Especial,Defesa Especial,Velocidade\n')
        for pokemon in pokemons:
            file.write(f"{pokemon['Pokédex']},{pokemon['Nome']},{pokemon['Tipo1']},{pokemon['Tipo2']},{pokemon['Altura']},{pokemon['Peso']},{pokemon['HP']},{pokemon['Ataque']},{pokemon['Defesa']},{pokemon['Ataque Especial']},{pokemon['Defesa Especial']},{pokemon['Velocidade']}\n")

if (__name__ == "__main__"):
    main()