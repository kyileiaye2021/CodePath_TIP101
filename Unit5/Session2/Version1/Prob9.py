#unit 5
#session 2
#ver 1
#prob 9

class Node:
  def __init__(self, value, next = None, prev = None):
    self.value = value
    self.next = next
    self.prev = prev

poliwrath = Node('Poliwrath')
poliwhirl = Node('Poliwhirl', poliwrath)
poliwag = Node('Poliwag',poliwhirl)

poliwrath.prev = poliwhirl
poliwhirl.prev = poliwag


print(poliwhirl.prev.value, "<->", poliwhirl.value, "<->", poliwhirl.next.value)
#'Poliwag' <-> 'Poliwhirl' <-> 'Poliwrath'`