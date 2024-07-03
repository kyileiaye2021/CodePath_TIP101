#unit 5
#session 1
#ver 1
#prob 6

'''
Added a new method in class : add_type(new_type)
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

  def catch(self):
    self.is_caught = True

  def choose(self):
    if self.is_caught:
      print(f"{self.name} I choose you!")
    else:
      print(f"{self.name} is wild! Catch them if you can!")

  def add_type(self, new_type):
    self.types.append(new_type)


jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()
