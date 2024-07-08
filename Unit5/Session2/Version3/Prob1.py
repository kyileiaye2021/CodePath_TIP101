#unit 5
#session 2
#ver 3
#prob 1

class Player:
  def __init__(self, character, kart, outcomes):
      self.character = character
      self.kart = kart
      self.items = []
      self.race_outcomes = outcomes

  def get_tournament_place(self, opponents):

    #getting the avg of current obj
  
    own_avg = sum(self.race_outcomes) / len(self.race_outcomes)
    
    place = 1
    for opponent in opponents:
      opponent_avg = sum(opponent.race_outcomes) / len(opponent.race_outcomes)
      if opponent_avg < own_avg:
        place += 1

    return place


player1 = Player("Mario", "Standard", [1, 2, 1, 1, 3])
player2 = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
player3 = Player("Peach", "Standard", [3, 3, 2, 3, 1])

opponents = [player2, player3]
print(f"{player1.character} was number {player1.get_tournament_place(opponents)}")
print(f"{player2.character} was number {player2.get_tournament_place(opponents)}")

'''
Example Output:

Mario was number 1 # Mario's average place is 1.6, Luigi's is 2.0, and Peach's is 2.4
'''