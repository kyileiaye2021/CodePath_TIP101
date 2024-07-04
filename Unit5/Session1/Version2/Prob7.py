#unit 5
#session 1
#ver 2
#prob 7

class Card():
  def  __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    
  def get_value(self):
    int_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
    if self.rank in int_ranks:
      return int(self.rank)
    elif self.rank == 'Ace':
      return 1
    elif self.rank == "Jack":
      return 11
    elif self.rank == "Queen":
      return 12
    elif self.rank == "King":
      return 13
    else:
      return False


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



def sum_hand(hand):
  total = 0
  for card in hand.cards:
    total += card.get_value()
  return total
  
card_one = Card("Hearts", "3")
card_two = Card("Hearts", "Jack")
card_three = Card("Spades", "3")

hand = Hand()
hand.add_card(card_one)
hand.add_card(card_two)
hand.add_card(card_three)

sum = sum_hand(hand)
print(sum)
