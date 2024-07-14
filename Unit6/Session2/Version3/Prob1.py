#unit 6
#session 2
#ver 3
#prob 1

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def circular_list_length(head):
  length = 1
  curr_head = head
  temp_starting_head = head
  
  while curr_head.next != temp_starting_head:
    length += 1
    curr_head = curr_head.next

  return length

num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num1.next = num2
num2.next = num3
num3.next = num1
print(circular_list_length(num1))