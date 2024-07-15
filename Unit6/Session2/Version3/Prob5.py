#unit 6
#session 2
#ver 3
#prob 5

# iterate thru ll to know the length of the whole ll and make ll circular
#calculate length_to_iterate thru the ll in prev order
# iterate from the current last node to prev nodes for length_to_iterate times
#when the loop stops, the current pointer will point to the new head of ll

"""
Input List
1 <-> 2 <-> 3 <-> 4 <-> 5
Input: head = 1, k = 2

Expected Return value: 4
Expected Output List: 3 <-> 4 <-> 5 <-> 1 <-> 2

Explanation: 
Rotation 1: 2 <-> 3 <-> 4 <-> 5 <-> 1
Rotation 2: 3 <-> 4 <-> 5 <-> 1 <-> 2

Input List
0 <-> 1 <-> 2
Input: head = 0, k = 4

Expected Return value: 4
Expected Output List: 1 <-> 2 <-> 0
Explanation: 

Rotation 1: 1 <-> 2 <-> 0
Rotation 2: 2 <-> 0 <-> 1 
Rotation 3: 0 <-> 1 -> 2
Rotation 4: 1 <-> 2 <-> 0

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
"""
#CAn k be greater than or equal to length of ll?
#can k be 0?
class Node:
  def __init__(self, value, prev=None, next=None):
      self.value = value
      self.prev = prev
      self.next = next

def print_ll(head):
  curr_head = head
  while curr_head:
    if curr_head.next:
      print(f"{curr_head.value} -> ", end='')
    else:
      print(curr_head.value)
    curr_head = curr_head.next

def rotate_doubly_linked_list(head, k):
  length = 1
  curr_head = head

  while curr_head.next:
    length += 1
    curr_head = curr_head.next

  #making the ll circular
  curr_head.next = head 
  head.prev = curr_head

  length_to_iterate = k % length #calculate length to iterate to reach the start of the ll

  current_head = head #iterate the ll from the beginning again
  for _ in range(length_to_iterate):
    current_head = current_head.next

  new_head = current_head #stop the iteration when it reaches the start of the new head
  new_last = current_head.prev #getting the end of circular ll
  new_last.next = None 
  new_head.prev = None

  return new_head

num1 = Node(1)
num2 = Node(2,num1)
num3 = Node(3,num2)
num4 = Node(4,num3)
num5 = Node(5,num4)
num1.next = num2
num2.next = num3
num3.next = num4
num4.next = num5

print_ll(rotate_doubly_linked_list(num1, 2))


var1 = Node(0)
var2 = Node(1, var1)
var3 = Node(2, var2)
var1.next = var2
var2.next = var3
print_ll(rotate_doubly_linked_list(var1, 4))
