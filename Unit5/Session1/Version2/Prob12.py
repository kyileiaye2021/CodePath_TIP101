#unit 5
#session 1
#ver 2
#prob 12

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next= next

def print_linked_list(head):
  node_lst = []
  current_head = head
  while current_head:
    node_lst.append(current_head.value)
    current_head = current_head.next
  return node_lst

e = Node('e')
d = Node('d', e)
c = Node('c', d)
b = Node('b', c)
a = Node('a', b)
print(print_linked_list(a))
#[`a`,`b`,`c`,`d`,`e`]