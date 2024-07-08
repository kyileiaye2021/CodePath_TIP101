#Unit 5
#session 2
#ver 3
#prob 3

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def add_second(head, val):
  new_node = Node(val)
  temp_node = head.next
  head.next = new_node
  new_node.next = temp_node

  curr_head = head
  while curr_head:
    if curr_head.next:
      print(f'{curr_head.value} -> ')
    else:
      print(curr_head.value)
    curr_head = curr_head.next

node_3 = Node(4)
node_2 = Node(3, node_3)
node_1 = Node(1, node_2)
add_second(node_1, 2)
# linked list: 1 -> 3 -> 4
# add_second(head, 2)
# result: 1 -> 2 -> 3 -> 4
