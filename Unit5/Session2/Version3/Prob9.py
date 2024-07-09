#unit 5
#session 2
#ver 3
#prob 9

class Node:
  def __init__(self, value, next=None, prev=None):
      self.value = value
      self.next = next
      self.prev = prev

crazy_in_love = Node("Crazy in Love")
formation = Node("Formation")
texas_hold_em = Node("Texas Hold 'Em")
crazy_in_love.next = formation
formation.next = texas_hold_em

curr_head = crazy_in_love
curr_head.prev = None
while curr_head:
  if curr_head.next:
    curr_head.next.prev = curr_head
  curr_head = curr_head.next

print(texas_hold_em.prev.value)
print(formation.prev.value)
print(crazy_in_love.prev)


# Current Singly Linked List: Crazy in Love -> Formation -> Texas Hold 'Em
# Desired Doubly Linked List: Crazy in Love <-> Formation <-> Texas Hold 'Em