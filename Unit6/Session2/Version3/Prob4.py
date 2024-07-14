#unit 6
#session 2
#ver 3
#prob 4

# temp_node
# iterate thru the ll until it reaches none
# check if m > 0:
  # attach the curr node to next of temp_node 
  # move the curr node to next node
  # decrement m by 1
  # if m == 0:
    # reset n to orig n val
# else if check n > 0:
  # move the curr node to next node
  # decrement n by 1
  # if n == 0:
    # reset m to orig m val
"""
Example usage:

Input: List 1: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10
Input: head = 1, m = 2, n = 3

Output: 1 -> 2 -> 6 -> 7 
Explanation: Keep first two nodes 1 & 2, delete next three nodes 3, 4, & 5
Keep next two nodes 6 & 7, delete remaining three nodes 8, 9, & 10


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
"""

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

def skip_and_remove(head, m, n):
  temp_node = Node(0)
  tail = temp_node
  m_val = m
  n_val = n
  curr_head = head

  while curr_head:
    for i in range(m):

      if not curr_head:
        tail.next = None
        return temp_node.next

      tail.next = curr_head
      tail = tail.next
      curr_head = curr_head.next

    for i in range(n):

      if not curr_head:
        tail.next = None
        return temp_node.next

      curr_head = curr_head.next

  tail.next = None
  return temp_node.next

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10))))))))))
print_ll(skip_and_remove(head, 2, 3))


