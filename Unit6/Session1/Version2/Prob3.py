#unit 6
#session 1
#ver 2
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
  #print()

# Function with a bug!
def remove_by_value(head, val):
  # Check if the list is empty
  if head is None:
      return head

  # If the node to be removed is the head of the list
  if head.value == val:
      return head.next

  # Initialize pointers
  current = head

  # Traverse the list to fnd the node to remove
  while current.next:
      if current.next.value == val:
          node_to_be_removed = current.next
          current.next = node_to_be_removed.next #skip the node_to_be_removed
          return head
      current = current.next

  # If no node was found with the value `val`, return the original head
  return head

# Input List: 1 -> 2 -> 3 -> 4
# Value to Remove: 3
head = Node(1, Node(2, Node(3, Node(4))))
val_to_be_removed = 3
updated_ll = remove_by_value(head, val_to_be_removed)
print_list(updated_ll)
# Expected Return Value: 1
# Expected Result List: 1 -> 2 -> 4
