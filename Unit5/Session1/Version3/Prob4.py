#unit 5
#session 1
#ver 3
#prob 4

class Player():
  def  __init__(self, character, kart):
    self.character = character
    self.kart = kart
    self.items = []
  
  def set_player(self, name):
    valid_names = ["Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", "Bowser"]
    if name in valid_names:
      self.character = name
      print("Character Updated")

    else:
      print("Invalid character")

player_one = Player('Yoshi', 'Super Blooper')
player_two = Player('Bowser', 'Pirahna Prowler')
player_one.set_player("Peach")
player_two.set_player("Kermit")