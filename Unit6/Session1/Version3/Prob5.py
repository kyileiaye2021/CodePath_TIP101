#unit 6
#session 1
#ver 3
#prob 5

class Node:
  def __init__(self, value=None, next=None):
      self.value = value
      self.next = next

#finding the length of the cycle of ll
def cycle_length(head):
  '''
  we have to loop until the loop reaches back to the head of the cycle
  '''
  length = 1
  curr_head = head.next
  start = head
  while curr_head.value != start.value:
    length += 1
    curr_head = curr_head.next
  return length
  
#finding where the cycle starts
def find_loop_start(meet_point, head):
  slow2 = head
  while slow2 != meet_point:
      slow2 = slow2.next
      meet_point = meet_point.next

  return cycle_length(slow2)

#finding if the ll is the cycle 
def get_loop_start(head):
  slow = fast = head
  while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
          # A loop has been detected, find its start
          return find_loop_start(slow, head)
  return None  # No loop found.

# Create the linked list with a loop
head = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
head.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_2

# Detect the loop start
loop_start = get_loop_start(head)
print(get_loop_start(head))  # Expected output: 3
