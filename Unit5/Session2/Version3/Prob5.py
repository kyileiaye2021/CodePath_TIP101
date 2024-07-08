#unit 5
#session 2
#ver 3
#prob 5

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def copy_ll(head):
  curr_node = head
  temp_new_head = Node(head.value)
  new_head = temp_new_head

  while curr_node.next:
    next_node = Node(curr_node.next.value)
    temp_new_head = Node(curr_node.value, next_node)
    curr_node = curr_node.next
    temp_new_head = temp_new_head.next

  new_head.next = None
  return new_head

node_3 = Node(7)
node_2 = Node(6, node_3)
node_1 = Node(5, node_2)
head = node_1
# Linked List: 5 -> 6 -> 7
copy = copy_ll(head) # Linked List Copy: 5 -> 6 -> 7
print(head.value, copy.value)

# Change original list -- should not affect the copy
head.value = 10
print(head.value, copy.value)