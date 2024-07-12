#unit 6
#session 1
#ver 2
#prob 1

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def print_lst(head):
  curr_head = head
  while curr_head:
    if curr_head.next:
      print(f"{curr_head.value} -> ", end='')
    else:
      print(curr_head.value)
    curr_head = curr_head.next
    
wario = Node("Wario")
luigi = Node("Luigi", wario)
head = Node("Mario", luigi)
print_lst(head)
