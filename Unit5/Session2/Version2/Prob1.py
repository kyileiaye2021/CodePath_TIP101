#unit 5
#session 2
#ver 2
#prob 1

class Card():
  def  __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

def is_two_pair(player_hand):
  rank_frequency = {}
  for card in player_hand:
    if card.rank not in rank_frequency:
      rank_frequency[card.rank] = 1
    else:
      rank_frequency[card.rank] += 1

  rank_count = 0
  for rank in rank_frequency:
    if rank_frequency[rank] == 2:
      rank_count += 1

  if rank_count == 2:
    return True
  return False

card_one = Card("Hearts", "Ace")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "Ace")
card_four = Card("Diamonds", "4")
card_five = Card("Diamonds", "6")
card_six = Card("Diamonds", "7")

player_one_hand = [card_one, card_two, card_three, card_four, card_five]
print(is_two_pair(player_one_hand))

player_two_hand = [card_two, card_three, card_four, card_five, card_six]
print(is_two_pair(player_two_hand))