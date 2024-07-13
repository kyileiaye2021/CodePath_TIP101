#unit 6
#session 2
#ver 1
#prob 3

#create two linked list (less and big) and combine
class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def print_lst(head):
  curr_head = head
  while curr_head:
    if curr_head.next:
      print(f"{curr_head.value} -> ", end='')
    else:
      print(curr_head.value)
    curr_head = curr_head.next

def partition(head, val):
  curr_head = head
  less_head = Node(0)
  greater_head = Node(0)

  #keeping the head of less and greater starts of the nodes
  less_head_copy = less_head
  greater_head_copy = greater_head

  while curr_head:
    if curr_head.value < val:
      less_head.next = curr_head
      less_head = less_head.next
    else:
      greater_head.next = curr_head
      greater_head = greater_head.next

    curr_head = curr_head.next

  greater_head.next = None #appending none to greater ll
  less_head.next = greater_head_copy.next #connect the less ll and greater ll
  return less_head_copy.next

head = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
val = 3
updated_ll = partition(head, val) #2->2->3->4->5
print_lst(updated_ll)
# 1 -> 4 -> 3 -> 2 -> 5 -> 2
# head = 1, val = 3

