#unit 5
#session 1
#ver 3
#prob 2

class Player():
  def  __init__(self, character, kart):
    self.character = character
    self.kart = kart
    self.items = []

  def get_player(self):
    return f"{self.character} driving the {self.kart}"

player_one = Player('Yoshi', 'Super Blooper')
player_two = Player('Bowser', 'Pirahna Prowler')
print(f'Match: {player_one.get_player()} vs {player_two.get_player()}')