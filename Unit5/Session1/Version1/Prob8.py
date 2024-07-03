#unit 5
#session 1
#ver 1
#prob 8

'''
Traverse the linked list thru obj
update the current obj with the next object
'''
class Pokemon():
  def  __init__(self, name, types, evolution = None):
    self.name = name
    self.types = types
    self.is_caught = False
    self.evolution = evolution

def get_evolutionary_line(starter_pokemon):
  evolved_lst = []
  current_pokemon = starter_pokemon
  while current_pokemon:
    evolved_lst.append(current_pokemon.name)
    current_pokemon = current_pokemon.evolution
  return evolved_lst

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)
