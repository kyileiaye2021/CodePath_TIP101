#unit 6
#session 2
#ver 3
#prob 6

"""
Input List:
0 -> 3- > 1 -> 0 -> 4 -> 5 -> 2 -> 0
Input: head = 0

Expected Return value: 4
Expected Result list: 4 -> 11

Explanation: 3 + 1 = 4, 4 + 5 + 2 = 11

Input List: 
O -> 1 -> 0 -> 3 -> 0 -> 2 -> 2-> 0
Input: head = 0

Expected Return Value: 1
Expected Result List: 1 -> 3 -> 4

Explanation: 1, 3, 2+ 2 = 4
"""

# everytime we find the 0, create a new node with value 0
# keep iterating the next nodes
# if the node is not 0, add the curr node's val to new node


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

def merge_nodes(head):
  curr_new_node = Node(0)
  curr_sum = 0
  tail = curr_new_node

  curr_head = head
  while curr_head:
    if curr_head.value == 0:
      if curr_sum > 0:
        new_node = Node(curr_sum)
        tail.next = new_node
        tail = tail.next
        curr_sum = 0
    else:
      curr_sum += curr_head.value
    curr_head = curr_head.next

  return curr_new_node.next

#0 -> 3- > 1 -> 0 -> 4 -> 5 -> 2 -> 0
head = Node(0, Node(3, Node(1, Node(0, Node(4, Node(5, Node(2, Node(0))))))))
print_ll(merge_nodes(head))

#O -> 1 -> 0 -> 3 -> 0 -> 2 -> 2-> 0
head2 = Node(0, Node(1, Node(0, Node(3, Node(0, Node(2, Node(2, Node(0))))))))
print_ll(merge_nodes(head2)) #1 -> 3 -> 4

