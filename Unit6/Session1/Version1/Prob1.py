#unit 6
#session 1
#ver 1
#prob 1

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def print_ll(head):
  curr_head = head
  while curr_head:
    if curr_head.next:
      print(f"{curr_head.value} -> ",end='')
    else:
      print(curr_head.value)
    curr_head = curr_head.next

head = Node(4,Node(3, Node(2)))
print_ll(head)