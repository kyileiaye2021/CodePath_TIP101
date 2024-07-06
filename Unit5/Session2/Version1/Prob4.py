class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def get_tail(head):
  if not head:
    return None

  curr_node = head
  while curr_node:
    if not curr_node.next:
      return curr_node.value
    curr_node = curr_node.next

# linked list: num1->num2->num3
num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)
head = num1
tail = get_tail(num1)
print(tail)
