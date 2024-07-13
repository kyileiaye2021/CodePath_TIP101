#unit 6
#session 2
#ver 1
#prob 6

# iterate the ll until it reaches mth node
# prev = None
# iterate the ll starting from mth node until the length is nth node
#  * get next node 
#  * assign the next of the curr node to prev
#  * assign prev to curr node
#  * assign curr node to next node

class Node:
  def __init__(self, value=None, next=None):
    self.value = value 
    self.next = next

def print_lst(head):
  curr_head = head
  while curr_head:
    if curr_head.next:
      print(f"{curr_head.value} -> ", end='')
    else:
      print(curr_head.value)
    curr_head = curr_head.next

def reverse_between(head, m, n):

  if not head:
    return None

  curr_head = head
  length = 1
  first_connect_node = Node()
  last_connect_node = Node()
  while curr_head:
    if length == (m - 1):
      first_connect_node= curr_head
    elif length == (n + 1):
      last_connect_node = curr_head
    length += 1
    curr_head = curr_head.next

  #print(first_connect_node.value)
  #print(last_connect_node.value)
  #iterate until it reaches to mth node
  length = 1 #reset the length to 1
  curr_head = head

  while curr_head and length < m:
    length += 1
    curr_head = curr_head.next

  # at this point, curr_head is pointing to the mth node
  #iterate the ll until it reaches to nth node
  prev = last_connect_node
  while curr_head and length <= n:
    next_node = curr_head.next
    curr_head.next = prev
    prev = curr_head
    curr_head = next_node
    length += 1

  first_connect_node.next = prev
  return head

# input list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))
print_lst(reverse_between(head, 2, 5))