#unit 5
#session 1
#ver 2
#prob 3

class Card():
  def  __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

def print_card(self):
  print(f"{self.rank} of {self.suit}")

card = Card('Hearts', 'Ace')
print_card(card)