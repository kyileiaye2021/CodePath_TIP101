#unit 6
#session 2
#ver 2
#prob 1

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def print_ll(head):
  curr_head = head
  temp_head = head
  print(f"{curr_head.value} -> ", end='')
  curr_head = curr_head.next

  while curr_head.value != temp_head.value:
    print(f"{curr_head.value} -> ", end='')
    curr_head = curr_head.next
  print(curr_head.value)

def make_circular(head):
  curr_head = head
  while curr_head.next:
    curr_head = curr_head.next
  curr_head.next = head
  return head

# Input List: num1 -> num2 -> num3
num_1 = Node(1)
num_2 = Node(2)
num_3 = Node(3)
num_1.next = num_2
num_2.next = num_3
updated_ll = make_circular(num_1)
print_ll(updated_ll)