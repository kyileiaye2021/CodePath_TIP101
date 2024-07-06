#unit 5
#session 2
#ver 1
#prob 5

#unit 5
#session 2
#ver 1
#prob 5

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def ll_replace(head, original, replacement):
  curr_node = head
  while curr_node:
    if curr_node.next:
      if curr_node.value == original:
        curr_node.value = replacement
      print(f"{curr_node.value} -> ", end='')
    else:
      if curr_node.value == original:
        curr_node.value = replacement
      print(f"{curr_node.value}")
    curr_node = curr_node.next

num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")
# updated linked list: "banana" -> 6 -> "banana"

