class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

mouse = Node("Jerry")
cat = Node("Tom")
cat.next = mouse

print(cat.value)
print(cat.next)
print(cat.next.value)
print(mouse.value)
print(mouse.next)