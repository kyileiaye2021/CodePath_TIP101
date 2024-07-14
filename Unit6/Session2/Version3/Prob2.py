#unit 6
#session 2
#ver 3
#prob 2

#Time complexity - O(n)
#Space complexity - O(1)

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next
    
def print_ll(head):
  curr_head = head
  while curr_head:
    if curr_head.next:
      print(f"{curr_head.value} -> ", end="")
    else:
      print(curr_head.value)
    curr_head = curr_head.next

  
def find_cycle_head(head, meetingpoint):
  curr_head = head
  while curr_head != meetingpoint:
    curr_head = curr_head.next
    meetingpoint = meetingpoint.next

  # At this point, we know the starting point of ll
  while meetingpoint.next != curr_head:
    meetingpoint = meetingpoint.next
  meetingpoint.next = None
  return head
  
def detect_and_remove_cycle(head):
  
  if not head:
    return None
  if not head.next:
    return head.value
    
  #check if there is a cycle in ll
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return find_cycle_head(head, fast)


num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num4 = Node(4)
num1.next = num2
num2.next = num3
num3.next = num4
num4.next = num1
print_ll(detect_and_remove_cycle(num1))
  