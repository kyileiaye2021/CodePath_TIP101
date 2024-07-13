#unit 6
#session2
#ver 1
#prob 5

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def add_two_numbers(head_a, head_b):
  # strings to store numbers
  head_a_numbers = ""
  head_b_numbers = ""
  
  curr_head = head_a
  while curr_head:
    head_a_numbers += str(curr_head.value)
    curr_head = curr_head.next

  curr_head = head_b
  while curr_head:
    head_b_numbers += str(curr_head.value)
    curr_head = curr_head.next

  return int(head_a_numbers) + int(head_b_numbers)
  

# list 1: 2 -> 4 -> 3 (342)
# list 2: 5 -> 6 -> 4 (465)
# head_a = 2, head_b = 5
head_a = Node(2, Node(4, Node(3)))
head_b = Node(5, Node(6, Node(4)))
sum = add_two_numbers(head_a, head_b)
print(sum)