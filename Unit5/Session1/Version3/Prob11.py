#unit 5
#session 1
#ver 3
#prob 11

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

cheese = Node("Gouda")
mouse = Node("Jerry", cheese)
cat = Node("Tom", mouse)
dog = Node("Spike", None)

print(dog.value)
print(dog.next)
print(dog.next.value)
print(cat.next)
print(cat.next.value)
print(mouse.next)
print(mouse.next.value)