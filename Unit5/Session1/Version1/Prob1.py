#unit 5
#session 1
#ver 1
#prob 1

class Pokemon:
  def __init__(self, name, types):
      self.name = name
      self.types = types
      self.is_caught = False


my_pokemon = Pokemon("Pikachu", "Electric")
print(my_pokemon.name)
print(my_pokemon.types)
