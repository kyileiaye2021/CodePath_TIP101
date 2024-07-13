#unit 6
#session 2
#ver 1
#prob 4

#iterate thru the linked list once to find the length of the list
#iterate the linked list for that amount and operate over each node in each iteration to know the decimal val

# * Low level planning
# * create a var to keep track of length
#   * iterate over the ll and update the length of the ll in each iteration
# * create a var to keep track of the total val of decimal
# * iterate over the ll again from the start
#   * in each iteration, multiply the val of each node by (2 * total_length) and add it to total decimal
#   * decrement the total_length by 1
#   * shift the curr node to the next node
# * return total decimal val

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def binary_to_int(head):
  length = -1
  curr_head = head
  while curr_head:
    length += 1
    curr_head = curr_head.next

  total_decimal_val = 0

  curr_head = head #reset curr_head to the start of the orig ll
  while curr_head and length >= 0:
    curr_decimal_val = (2 ** length) * curr_head.value
    total_decimal_val += curr_decimal_val
    length -= 1
    curr_head = curr_head.next

  return total_decimal_val

# 1 -> 0 -> 1
num1 = Node(1)
num2 = Node(0)
num3 = Node(1)
num4 = Node(0)
num1.next = num2
num2.next = num3
num3.next = num4
int_num = binary_to_int(num1)
# 1010 in binary 

print(int_num)