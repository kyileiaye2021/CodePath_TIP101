#unit 5
#session 2
#ver 3
#prob 7

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def ll_remove(head, val):
  curr_head = head
  while curr_head:
    if curr_head.next.value == val:
      curr_head.next = curr_head.next.next
      return head
    curr_head = curr_head.next

  return head

def print_list(head):
  curr_head = head
  while curr_head:
    if curr_head.next:
      print(f'{curr_head.value} -> ',end='')
    else:
      print(curr_head.value)
    curr_head = curr_head.next

node_4 = Node(8)
node_3 = Node(7, node_4)
node_2 = Node(6, node_3)
node_1 = Node(5, node_2)
removed_list = ll_remove(node_1, 6)
print_list(removed_list)
# Linked List: 5 -> 6 -> 7 -> 8
# Input: head = 5, val = 6
# Expected Output: 5 -> 7 -> 8