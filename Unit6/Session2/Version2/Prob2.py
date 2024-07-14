#unit 6
#session 2
#ver 2
#prob 2

# use two pointer technique to find the circular in ll
# if a circle is found, find the starting point of the cycle
# store the ele of the cycle in the lst
class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def find_circular_list(head, meetingpoint):
  circle_lst = []
  curr_head = head

  while curr_head != meetingpoint:
    curr_head = curr_head.next
    meetingpoint = meetingpoint.next

  #At this point, we got the starting point of the circle in ll
  circle_lst.append(meetingpoint.value)
  starting_point_copy = meetingpoint
  meetingpoint = meetingpoint.next

  while meetingpoint != starting_point_copy:
    circle_lst.append(meetingpoint.value)
    meetingpoint = meetingpoint.next

  return circle_lst

def collect_cycle_nodes(head):
  #check if there is a circle in the ll
  circle_lst = []
  slow, fast = head, head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast: #circle is found
      circle_lst = find_circular_list(head, fast)
      break

  return circle_lst

# num1 -> num2 -> num3 -> num4 -> num2
num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num4 = Node(4)
num1.next = num2
num2.next = num3
num3.next = num4
num4.next = num2
lst = collect_cycle_nodes(num1)
print(lst)

var1 = Node(1)
var2 = Node(2)
var3 = Node(3)
var4 = Node(4)
var1.next = var2
var2.next = var3
var3.next = var4
# var1 -> var2 -> var3 -> var4
lst2 = collect_cycle_nodes(var1)
print(lst2)


