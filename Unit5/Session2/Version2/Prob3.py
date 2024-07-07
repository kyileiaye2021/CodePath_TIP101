#unit 5
#session 2
#ver 2
#prob 3

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def add_first(head, val):
  new_node = Node(val,head)
  return new_node

node_C = Node('C')
node_B = Node('B', node_C)
node_A = Node('A', node_B)

new_list = add_first(node_A, 0)
curr_node = new_list
while curr_node:
  if curr_node.next:
    print(f'{curr_node.value} -> ', end='')
  else:
    print(curr_node.value)
  curr_node = curr_node.next
    
'''
Example:

# Linked List: A -> B -> C
new_list = add_first(node_a, 0)
# New List: 0 -> A -> B -> C
'''