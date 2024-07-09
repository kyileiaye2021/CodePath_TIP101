#unit 5
#session 2
#ver 3
#prob 8

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def tail_to_head(head):
  #iterating thru head list until it reaches to the last one
  curr_head = head
  while curr_head.next:
    curr_head = curr_head.next

  node_to_be_inserted = Node(curr_head.value)
  node_to_be_inserted.next = head
  return node_to_be_inserted

def print_lst(head):
  curr_head = head
  while curr_head:
    if curr_head.next:
      print(f"{curr_head.value} -> ", end='')
    else:
      print(curr_head.value)
    curr_head = curr_head.next

node_4 = Node(4)
node_3 = Node(3, node_4)
node_2 = Node(2, node_3)
node_1 = Node(1, node_2)

print_lst(tail_to_head(node_1))
# Input: 1 -> 2 -> 3 -> 4
# Output: 4 -> 1 -> 2 -> 3
