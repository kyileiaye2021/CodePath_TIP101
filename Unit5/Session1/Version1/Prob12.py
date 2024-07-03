#unit 5
#session 1
#ver 1
#prob 12

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next= next

def print_linked_list(head):
  current_start = head

  while current_start:
    if current_start.next:
      print(f'{current_start.value}->',end='')
    else:
      print(current_start.value)
    current_start = current_start.next
    
e = Node('e')
d = Node('d',e)
c = Node('c',d)
b = Node('b',c)
a = Node('a',b)
print_linked_list(a)