#unit 5
#session 2
#ver 2
#prob 4

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def ll_length(head):
  length = 0
  curr_node = head
  while curr_node:
    length += 1
    curr_node = curr_node.next
  return length

num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)

# Linked List: num1 -> num2 -> num3
head = num1
print(ll_length(head))

# Empty Linked List
head = None
print(ll_length(head))

