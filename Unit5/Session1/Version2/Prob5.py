#unit 5
#session 1
#ver 2
#prob 5


class Card():
  def  __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def get_value(self):
    int_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
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

card = Card("Hearts", "7")
print(card.get_value())

card_two = Card("Spades", "Jack")
print(card_two.get_value())