#unit 5
#session 1
# ver 2
# Prob 9

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

tail = Node(200)
head = Node(100,tail)

print(head.value) 
print(head.next.value) 
print(tail.value) 
print(tail.next) 
