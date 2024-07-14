#unit 6
#session 2
#ver 2
#prob 4

class Node:
  def __init__(self, value, next= None):
    self.value = value
    self.next = next

def is_identical(head_a, head_b):
  curr_head_a = head_a
  curr_head_b = head_b
  while curr_head_a and curr_head_b:
    if curr_head_a.value != curr_head_b.value:
      return False
    curr_head_a = curr_head_a.next
    curr_head_b = curr_head_b.next
  return not curr_head_a and not curr_head_b 

# list1: 1->2->3->4
# list2: 1->2->3->4
# head_a = 1, head_b = 1,
list1 = Node(1, Node(2, Node(3, Node(4))))
list2 = Node(1, Node(2, Node(3, Node(4))))
print(is_identical(list1, list2))

# list1: 1->2->3->4
# list2: 1->3->4->2
# head_a = 1, head_b = 1,
lst1 = Node(1, Node(2, Node(3, Node(4))))
lst2 = Node(1, Node(3, Node(4, Node(2))))
print(is_identical(lst1, lst2))