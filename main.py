class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def find_middle_node(head):
  length = 0
  curr_node = head
  while curr_node:
    length += 1
    curr_node = curr_node.next

  mid = length // 2 - 1 if length % 2 == 0 else length // 2

  i = 0
  while head:
    if i == mid and head:
      return head.value
    i += 1
    head = head.next

num4 = Node(4)
num3 = Node(3, num4)
num2 = Node(2, num3)
num1 = Node(1, num2)
head = num1
mid = find_middle_node(head)
print(mid)