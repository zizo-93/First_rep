import requests
import pprint

main_link = 'https://www.ida.liu.se/~TDP002/pokeapi/api/v2/pokemon/'
half_main_link = main_link[:-16]


def request_to_dict(url):
    req_link = requests.get(url)
    data = req_link.json()
    return data

root_dict = request_to_dict(main_link)


pok_name = input('Enter pokemon name: ')


def getting_pokemon_url(pokemon_name):        
    dict = root_dict.get('results')
    for pokemon in dict:
      if pokemon.get('name') == pok_name:
        pok_url = (pokemon['url'])
        return pok_url
    else:
      print(f'{pok_name} was not found..')
   

  
pokemon_url = getting_pokemon_url(pok_name)


specific_pokemon_root_dic = request_to_dict(half_main_link + pokemon_url)        # Gives the root_dict to specifik pokemon 

def getting_pokemon_ability(pokemon_name):
   ability = specific_pokemon_root_dic.get('abilities')
   pprint.pp(len(ability))

getting_pokemon_ability(pok_name)





    
       
    

    



