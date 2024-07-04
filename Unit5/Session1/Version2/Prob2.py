#unit 5
#seesion 1
#ver 2
#prob 2

class Card():
  def  __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

def print_card(self):
  print(f"{self.rank} of {self.suit}")

card = Card('Clubs', 'Ace')
print_card(card)