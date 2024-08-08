#unit 10
#session 1
#ver 2
#prob 2

# reverse the linked list

'''Edge cases'''
# input - None, output - None
# input - Node(1), output - Node(1)

'''Happy cases'''
# input - 1 -> 2 -> 3 -> 4
# output - 4 -> 3 -> 2 -> 1

# Plan
# create a pointer to point to prev node which firstly is none
# create another pointer temp to iterate over the nodes in the lst
# in each iterateion
#   assign the next of the curr node to temp
#   assign prev node to curr node's next
#   assign curr node to prev node
#   assign curr next node to curr node

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def reverse(head):
  prev = None

  curr_node = head
  while curr_node:
    next_node = curr_node.next
    curr_node.next = prev
    prev = curr_node
    curr_node = next_node

  return prev

def print_ll(root):
  while root.next:
    print(f'{root.val} -> ')
    root = root.next

  print(root.val)

head = Node(1, Node(2, Node(3, Node(4))))
print_ll(reverse(head)) #4 -> 3 -> 2 -> 1

head = Node(1)
print_ll(reverse(head)) # 1

head = None
print_ll(reverse(head)) # None
  

