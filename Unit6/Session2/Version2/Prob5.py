#unit 6
#session 2
#ver 2
#prob 5

class Node:
  def __init__(self, value, next=None):
      self.value = value

      self.next = next

def print_ll(head):
  curr_head = head
  while curr_head:
    if curr_head.next:
      print(f"{curr_head.value} -> ", end='')
    else:
      print(curr_head.value)
    curr_head = curr_head.next


def rotate_right(head, k):
  if not head:
    return head

  length = 1
  curr_head = head 

  while curr_head.next:
    length += 1
    curr_head = curr_head.next

  curr_head.next = head #making a circular ll

  length_to_iterate = length - (k % length) #calculate length to iterate ll until the new head is found

  current_head = head #iterate the ll from the beginning upto length to iterate
  for _ in range(length_to_iterate - 1):
    current_head = current_head.next

  new_head = current_head.next #found the new head
  current_head.next = None #put none to current_head

  return new_head


head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print_ll(rotate_right(head, 2))

head2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print_ll(rotate_right(head2, 5))

head3 = Node(1, Node(2, Node(3)))
print_ll(rotate_right(head3, 4))# num1 -> num2 -> num3
