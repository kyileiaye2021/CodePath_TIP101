#unit 6
#session 2
#ver 3
#prob 3

# Two pointer technique
# create a temp node and set it as a current tail
# put smaller node to the next of the tail 
# update the tail
# return the next node of the temp node

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def print_ll(head):
  curr_head = head
  while curr_head:
    if curr_head.next:
      print(f"{curr_head.value} -> ", end='')
    else:
      print(curr_head.value)
    curr_head = curr_head.next

def merge_two_lists(head_a, head_b):
  temp_head = Node(0)
  tail = temp_head
  curr_head_a_pointer = head_a
  curr_head_b_pointer = head_b

  while curr_head_a_pointer and curr_head_b_pointer:
    if curr_head_a_pointer.value < curr_head_b_pointer.value:
      tail.next = curr_head_a_pointer
      curr_head_a_pointer = curr_head_a_pointer.next

    else:
      tail.next = curr_head_b_pointer
      curr_head_b_pointer = curr_head_b_pointer.next

    tail = tail.next

  if not curr_head_a_pointer:
    tail.next = curr_head_b_pointer
  else:
    tail.next = curr_head_a_pointer

  return temp_head.next

ll_1 = Node(1, Node(4, Node(5)))
ll_2 = Node(3, Node(6, Node(7)))
print_ll(merge_two_lists(ll_1, ll_2)) #1,3,4,5,6,7

head_a = Node(1, Node(2, Node(4)))
head_b = Node(3, Node(4, Node(5, Node(6))))
print_ll(merge_two_lists(head_a, head_b)) #1,2,3,4,4,5,6