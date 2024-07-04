# unit 5
# session 1
# ver 2
# Prob 8

class Card():
  def  __init__(self, suit, rank, next = None):
    self.suit = suit
    self.rank = rank
    self.next = next

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


def print_hand(starting_card):
  card_lst = []
  current_card = starting_card
  while current_card:
    card_lst.append(current_card)
    current_card = current_card.next

  for card in card_lst:
    print(f'{card.suit}, {card.rank}')

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "King")

card_one.next = card_two
card_two.next = card_three

print_hand(card_one)