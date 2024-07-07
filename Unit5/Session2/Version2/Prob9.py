#unit 5
#session 2
#ver 2
#prob 9

class Node:
  def __init__(self, value, next = None, prev = None):
    self.value = value
    self.next = next
    self.prev = prev

head = Node("First")
tail = Node("Last")

head.next = tail
tail.prev = head

print(head.value, "<->", head.next.value)
print(tail.prev.value, "<->", tail.value)