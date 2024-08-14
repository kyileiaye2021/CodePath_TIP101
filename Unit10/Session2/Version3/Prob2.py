#unit 10
#session 2
#ver 3
#prob 2

# Are the values in the tree sorted?

'''Happy Cases'''
# head 1 - a1 -> a2 -> c1 -> c2 -> c3
# head 2 - [b1,b2,b3,c1,c2,c3]
# output - [c1,c2,c3]

'''Edge Case'''
# head1 - a1
# head2 - a1
# output = a1

# head1 = [a1,a2,a3]
# head2 = [b1,b2]
# output - None

# head1 - None
# head2 - None
# output - None

# List Appraoch

# Two pointer approach
# 1) Initialize two pointers, pointer_a and pointer_b, to the heads of the two linked lists.
# 2) Traverse the lists until the two pointers meet:
#     a) If pointer_a reaches the end of listA, switch it to the head of listB.
#     b) If pointer_b reaches the end of listB, switch it to the head of listA.
#     c) Move both pointers one step forward.
# 3) The meeting point of the two pointers is the intersection node, or None if they do not intersect.
# 4) Return the intersection node.


class Node:
  def __init__(self, val, next_node = None):
      self.val = val
      self.next = next_node

def find_intersection(headA, headB):
  
  intersection_point = None
  if not headA or headB:
    return intersection_point
  
  pointer_a = headA
  pointer_b = headB

  while pointer_a != pointer_b:
    
    if not pointer_a.next:
      pointer_a.next = headB
    if not pointer_b.next:
      pointer_b.next = headA
      
    pointer_a = pointer_a.next
    pointer_b = pointer_b.next

  if pointer_a.val == pointer_b.val:
    intersection_point = pointer_a

  return intersection_point

head1 = Node('a1', Node('a2', Node('c1', Node('c2',Node('c3')))))
head2 = Node('b1', Node('b2', Node('b3', Node('c1', Node('c2', Node('c3'))))))
intersection_node = find_intersection(head1,head2)
print(intersection_node.val)