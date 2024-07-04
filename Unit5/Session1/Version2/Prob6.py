#unit 5
#session 1
#ver 2
#prob 6

class Card():
  def  __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

class Hand:
  def __init__(self):
      self.cards = []

  def add_card(self, card):
    self.cards.append(card)

  def remove_card(self, card):
    self.cards.remove(card)
  def print_card(self):
    for i in self.cards:
      print(f"{i.suit}, {i.rank}")

card_one = Card("Hearts", "3")
card_two = Card("Spades", "8")

player1_hand = Hand()
# cards = []
player1_hand.print_card()
print()

player1_hand.add_card(card_one)
# cards = [card_one]
player1_hand.print_card()
print()

player1_hand.add_card(card_two)
# cards = [card_one, card_two]
player1_hand.print_card()
print()

player1_hand.remove_card(card_one)
# cards = [card_two]
player1_hand.print_card()
