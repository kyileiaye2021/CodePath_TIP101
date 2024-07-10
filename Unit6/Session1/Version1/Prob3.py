#unit 6
#session 1
#ver 1
#prob 3

class Node:          #Value 
  def __init__(self, value, next=None):
      self.value = value
      self.next = next


# Helper function to print the linked list
def print_list(node):
  current = node
  while current:
      print(current.value, end=" -> " if current.next else "")
      current = current.next
  print()


# I have a bug! 
def remove_tail(head):
  if head is None: # If the list is empty, return None
      return None
  if head.next is None: # If there's only one node, removing it leaves the list empty
      return None 

# Start from the head and find the second-to-last node
  current = head
  while current.next.next: 
      current = current.next

  current.next = None # Remove the last node by setting second-to-last node to None
  return head

def print_ll(head):
  curr_head = head
  while curr_head:
    if curr_head.next:
      print(f"{curr_head.value} -> ",end='')
    else:
      print(curr_head.value)
    curr_head = curr_head.next

head = Node(1, Node(2, Node(3, Node(4))))
new_ll = remove_tail(head)
print_ll(new_ll)
# Input List: 1 -> 2 -> 3 -> 4
# Input: head = 1
