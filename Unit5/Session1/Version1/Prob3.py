#unit 5
#session 1
#ver 1
#prob 3

'''Updating is_caught var to True value
'''
class Pokemon:
  def __init__(self, name, types):
      self.name = name
      self.types = types
      self.is_caught = False

  def print_pokemon(self):
      print({
          "name": self.name,   # Output: "name": "Squirtle",
          "types": self.types, # Output: "types": ["Water"],
          "is_caught": self.is_caught # Output: "is_caught": False
      })


squirtle = Pokemon("Squirtle", ["Water"])
squirtle.is_caught = True
squirtle.print_pokemon()