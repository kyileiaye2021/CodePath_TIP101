
#unit 6
#session 1
#ver 1
#prob 5
#need multiple pass
'''
When comparing first half and second half of the ll, notice that prev pointer curr points to the first of the second half of the ll.
'''
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def is_palindrome(head):
  if not head and not head.next:
    return True

  #finding half of the linked list
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  #reverse the second half of the linked list
  prev = None
  while slow:
    new_node = slow.next
    slow.next = prev
    prev = slow
    slow = new_node

  #compare first half and second half of the list
  left, right = head, prev
  while right:
    if left.value != right.value:
      return False
    left = left.next
    right = right.next
  return True

head = Node(1, Node(2, Node(1)))
head1 = Node(1, Node(2, Node(2, Node(1))))
head2 = Node(1, Node(2, Node(3, Node(4))))
print(is_palindrome(head))
print(is_palindrome(head1))
print(is_palindrome(head2))
# Input List:
# 1 -> 2 -> 1
# 1 -> 2 -> 2 -> 1
# Input: head = 1