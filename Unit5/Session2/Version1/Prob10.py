#unit 5
#session 2
#ver 1
#prob 10

class Node:
  def __init__(self, value, next = None, prev = None):
    self.value = value
    self.next = next
    self.prev = prev

def print_reverse(tail):
  curr_node = tail
  while curr_node:
    if curr_node.prev:
      print(f"{curr_node.value} ->", end='')
    else:
      print(curr_node.value)
    curr_node = curr_node.prev
  
poliwrath = Node('Poliwrath')
poliwhirl = Node('Poliwhirl', poliwrath)
poliwag = Node('Poliwag',poliwhirl)

poliwrath.prev = poliwhirl
poliwhirl.prev = poliwag

#              (head)                       (tail)
# Linked List: Poliwag <-> Poliwhirl <-> Poliwrath
print_reverse(poliwrath)