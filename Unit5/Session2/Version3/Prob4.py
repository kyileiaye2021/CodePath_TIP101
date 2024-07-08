#unit 5
#session 2
#ver 3
#prob 4

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def increment_ll(head):
  curr_head = head
  while curr_head:
    curr_head.value += 1
    curr_head = curr_head.next
  return head

def print_list(head):
  curr_head = head
  while  curr_head:
    if curr_head.next:
      print(f"{curr_head.value} -> ", end='')
    else:
      print(curr_head.value)
    curr_head = curr_head.next

node_3 = Node(7)
node_2 = Node(6, node_3)
node_1 = Node(5, node_2)
my_list = node_1
# my_list: 5 -> 6 -> 7
print_list(my_list)

my_list = increment_ll(my_list)
# my_list: 6 -> 7 -> 8
print_list(my_list)

my_list = increment_ll(my_list)
# my_list: 7 -> 8 -> 9
print_list(my_list)