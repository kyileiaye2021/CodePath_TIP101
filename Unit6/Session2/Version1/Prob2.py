#unit 6
#session 2
#ver 1
#prob 2

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def last_node(head, meeting_point):
  curr_head = head
  while curr_head.value != meeting_point.value:
    curr_head = curr_head.next
    meeting_point = meeting_point.next

  start_node = curr_head #at this point, the start node of the cycle is found
  curr_head = curr_head.next 

  while curr_head.next.value != start_node.value: #iterate again to get the end of the cycle
    curr_head = curr_head.next
  return curr_head.value

def find_last_node_in_cycle(head):
  slow, fast = head,head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast: #found that the linked list is cycle
      return last_node(head, slow) 
  return None

head = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
head.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = node_2
print(find_last_node_in_cycle(head))
