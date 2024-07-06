#unit 5
#session 2
#ver 1
#prob 7

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def ll_insert(head, val, i):
  index = 0
  curr_node = head
  while curr_node:
    if index == i - 1:
      temp_node = curr_node.next
      new_node = Node(val,temp_node)
      curr_node.next = new_node
    index += 1
    curr_node = curr_node.next

  curr_node = head
  while curr_node:
    if curr_node.next:
      print(f"{curr_node.value} -> ", end='')
    else:
      print(curr_node.value)
    curr_node = curr_node.next

num3 = Node(9)
num2 = Node(12, num3)
num1 = Node(8, num2)
head = Node(3, num1)
# linked list: 3 -> 8 -> 12 -> 9
ll_insert(head, 20, 2)

# result linked list: 3 -> 8 -> 20 -> 12 -> 9