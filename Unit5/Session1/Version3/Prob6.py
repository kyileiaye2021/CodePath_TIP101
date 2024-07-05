#unit 5
#session 1
#ver 3
#prob 6


class Player():
  def  __init__(self, character, kart):
    self.character = character
    self.kart = kart
    self.items = []

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


player_one = Player("Yoshi", "Super Blooper")
player_one.items = ["banana", "bob-omb", "banana", "super star"]
player_two = Player("Peach", "Dolphin Dasher")

player_one.print_inventory()
player_two.print_inventory()