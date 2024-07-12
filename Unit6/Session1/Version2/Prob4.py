#unit 6
#session 1
#ver 2
#prob 4

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def middle_match(head, val):
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  return slow.value == val


# Input List:
# 1 -> 2 -> 3
# Input: head = 1, val = 2

# Input List:
# 1 -> 2 -> 3 -> 4
# Input: head = 1, val = 2
head = Node(1, Node(2, Node(3)))
head1 = Node(1, Node(2, Node(3, Node(4))))
print(middle_match(head, 2))
print(middle_match(head1, 2))
  
# Expected Return Value: True
# Expected Return Value: False