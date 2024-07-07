#unit 5
#session 2
#ver 2
#prob 6

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def find_max(head):
  max_val = float('-inf')
  curr_node = head
  while curr_node:
    if curr_node.value > max_val:
      max_val = curr_node.value
    curr_node = curr_node.next
  return max_val

num4 = Node(10)
num3 = Node(30, num4)
num2 = Node(15, num3)
num1 = Node(20, num2)

# linked list: num1 -> num2 -> num3 -> num4
max_val = find_max(num1)
print(max_val)