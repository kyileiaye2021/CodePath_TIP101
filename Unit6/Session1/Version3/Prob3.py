#unit 6
#session 1
#ver 3
#prob 3

class Node:
  def __init__(self, value=None, next=None):
      self.value = value
      self.next = next

# Helper function to print the linked list
def print_list(node):
  current = node
  while current:
      print(current.value, end=" -> " if current.next else "")
      current = current.next
  print()

# Function with a bug!
def remove_by_value(head, val):
  # Handle empty list and removal from the head
  if not head:
      return None
  if head.value == val:
      return head.next  # Return the second node as the new head

  current = head
  while current.next:
      if current.next.value == val:
          current.next = current.next.next  # Skip the node with the value
          return head  # Return the original head
      current = current.next

  # If no node was found with the value `val`, return the original head
  return head

head = Node(1, Node(2, Node(3, Node(4))))
val_to_be_removed = 3
updated_ll = remove_by_value(head, val_to_be_removed)
print_list(updated_ll)
# Input List: 1 -> 2 -> 3 -> 4
# Value to Remove: 3
# Expected Return Value: 1
# Expected Result List: 1 -> 2 -> 4