#unit 5
#session 2
#ver 3
#prob 6

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def find_min(head):
  curr_min_val = head.value
  curr_head = head
  while curr_head:
    if curr_head.value < curr_min_val:
      curr_min_val = curr_head.value
    curr_head = curr_head.next
    
  return curr_min_val


node_4 = Node(7)
node_3 = Node(6, node_4)
node_2 = Node(5, node_3)
node_1 = Node(8,node_2)
print(find_min(node_1))