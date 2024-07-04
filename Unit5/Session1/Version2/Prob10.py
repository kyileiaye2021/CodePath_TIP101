#unit 5
#session 1
#ver 2
#Prob 10

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
    
tail = Node(200)
middle = Node(150, tail)
head = Node(100,middle)

print(head.next.value) 
print(middle.next.value)
if tail.next:
  print(tail.next.value) 
else:
  print("None")