#unit 5
#session 1
#ver 2
#prob 1

class Card():
  def  __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

card = Card('Spades', 8)
print(card.suit)
print(card.rank)