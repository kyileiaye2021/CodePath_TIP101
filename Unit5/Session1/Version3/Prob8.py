#unit 5
#session 1
#ver 3
#Prob 8

class Player:
  def __init__(self, character, kart, opponent=None):
      self.character = character
      self.kart = kart
      self.items = []
      self.ahead = opponent

def get_place(my_player):
  current_player = my_player
  number = 1
  while current_player:
    number += 1
    current_player = current_player.ahead

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M", peach)
luigi = Player("Luigi", "Super Blooper", mario)

player1_rank = get_place("Luigi")
print(player1_rank)

player2_rank = get_place("Peach")
print(player2_rank)

player3_rank = get_place("Mario")
print(player3_rank)

