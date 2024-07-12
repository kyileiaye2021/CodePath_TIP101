#unit 6
#session 1
#ver 1
#prob 6

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
         
def reverse(head):
  prev = None
  curr_head = head
  while curr_head:
    next_node = curr_head.next
    curr_head.next = prev
    prev = curr_head
    curr_head = next_node
  return prev

head = Node(1, Node(2, Node(3, Node(4))))
reversed_ll = reverse(head)
print_ll(reversed_ll)