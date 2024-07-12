#unit 6
#session 1
#ver 3
#prob 6

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

def reverse_first_k(head, k):
  length = 0
  curr_head = head
  while length < k:
    curr_head = curr_head.next
    length += 1

  prev = curr_head #prev will point to node 4 in this case
  curr_head = head #reset the curr_head to the start of the original linked list

  while curr_head and length > 0: #reverse the first 3 nodes in linked list and connect with node 4
    next_node = curr_head.next
    curr_head.next = prev
    prev = curr_head
    curr_head = next_node
    length -= 1

  #At the end of the loop, prev node points to the head of the reversed list
  return prev

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
updated_ll = reverse_first_k(head,3)
print_lst(updated_ll)
# Input List: 1 —> 2 —> 3 —> 4 —> 5
# Input: head = 1, k = 3
# 3 -> 2 -> 1 -> 4 -> 5