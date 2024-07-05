#unit 5
#session 1
#ver 3
#prob 10

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

mouse = Node("Jerry")
cat = Node("Tom", mouse)
dog = Node("Spike", cat)

print(dog.value)
print(dog.next)
print(dog.next.value)
print(cat.next)
print(cat.next.value)
print(mouse.next)