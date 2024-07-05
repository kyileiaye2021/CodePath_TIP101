#unit 5
#session 1
#ver 3
#Prob 7

class Player:
  def __init__(self, character, kart):
      self.character = character
      self.kart = kart
      self.items = []
#... methods from previous problems
def add_item(self, item_name):
  valid_items = ["banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"]
  if item_name in valid_items:
    self.items.append(item_name)

def print_inventory(self):
  if len(self.items) == 0:
    print("Inventory empty")
    return

  inventory_dict = {}
  for ele in self.items:
    if ele not in inventory_dict:
      inventory_dict[ele] = 1
    else:
      inventory_dict[ele] += 1

  print("Inventory:", end=" ")
  for item, quantities in inventory_dict.items():
    if item != self.items[len(self.items) - 1]:
      print(f"{item}: {quantities}, ", end='')
    else:
      print(f"{item}: {quantities} ")

def print_results(race_results):
  for i, character in enumerate(race_results):
    print(f"{i+1}. {character.character}")

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")
race_one = [peach, mario, luigi]

print_results(race_one)