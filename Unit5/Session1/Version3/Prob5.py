#unit 5
#session 1
#ver 3
#prob 5

class Player():
  def  __init__(self, character, kart):
    self.character = character
    self.kart = kart
    self.items = []

  def add_item(self, item_name):
    valid_items = ["banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"]
    if item_name in valid_items:
      self.items.append(item_name)

player_one = Player("Yoshi", "Dolphin Dasher")
# items = []

player_one.add_item("red shell")
# items = ["red shell"]

player_one.add_item("super star")
# items = ["red shell", "super star"]

player_one.add_item("super smash")
# items = ["red shell", "super star"]
print(player_one.items)