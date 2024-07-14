#unit 6
#session 2
#ver 2
#prob 3

# Delete Duplicates in a Linked List
# iterate over the ll until the next node is None
# check the next node is the same node as the curr node
#   connect the curr node with the next node's next

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

def delete_dupes(head):
  curr_head = head
  while curr_head.next:
    next_node = curr_head.next
    if curr_head.value == next_node.value:
      curr_head.next = next_node.next
    curr_head = curr_head.next

  return head

# 1 -> 2 -> 3 -> 3 -> 4 -> 5
head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))
unique_ll = delete_dupes(head)
print_ll(unique_ll)