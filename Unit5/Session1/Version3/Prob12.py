class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def chase_list(chase):
  returned_str = ""
  current_animal = chase
  while current_animal:
    returned_str += f"{current_animal.value} "
    if current_animal.next:
      returned_str += "chases "

    current_animal = current_animal.next
  return  returned_str

dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese

print(chase_list(dog))