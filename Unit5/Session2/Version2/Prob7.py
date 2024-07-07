#unit 5
#session 2
#ver 2
#prob 7

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def ll_pop(head, i):
  index = 0
  curr_node = head
  while curr_node:
    if index == i - 1:
      temp_node = curr_node.next
      curr_node.next = temp_node.next
    index += 1
    curr_node = curr_node.next

  while head:
    if head.next:
      print(f'{head.value} -> ', end="")
    else:
      print(head.value)
    head = head.next

num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)
ll_pop(num1, 1)
'''
Example Usage:

# linked list: num1 -> num2 -> num3
ll_pop(num1, 1)
# result: num1 -> num3
'''