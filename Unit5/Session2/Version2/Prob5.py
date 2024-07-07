#unit 5
#session 2
#ver 2
#prob 5

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def delete_tail(head):
  curr_node = head
  while curr_node:
    if not curr_node.next.next:
      curr_node.next = None
    curr_node = curr_node.next

  while head:
    if head.next:
      print(f'{head.value} -> ', end='')
    else:
      print(head.value)
    head = head.next

num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)
delete_tail(num1)
'''
Example Usage:

# linked list: num1 -> num2 -> num3
delete_tail(num1)

# linked list: num1 -> num2
'''