#unit 6
#session 1
#ver 2
#prob 6
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def count_critical_points(head):
  num_of_critical_points = 0
  curr_head = head
  prev_node = None

  while curr_head:
    next_node = curr_head.next
    
    if not prev_node: #if the prev node is none, skip the curr node and go to next node
      prev_node = curr_head
      curr_head = curr_head.next
      continue
      
    if not next_node:
      break

    if (curr_head.value > next_node.value and curr_head.value > prev_node.value) or (curr_head.value < next_node.value and curr_head.value < prev_node.value):
      num_of_critical_points += 1

    prev_node = curr_head
    curr_head = curr_head.next
    
  return num_of_critical_points

head = Node(1, Node(2, Node(3, Node(3, Node(3, Node(5, Node(1, Node(3))))))))
print("Num of Critical Points:",count_critical_points(head))
# Input List: 1 -> 2 -> 3 -> 3 -> 3 -> 5 -> 1 -> 3
# Input: head = 3
# Expected Return Value: 2
# Explanation:
#  - Critical point 1 (local maxima) 3 -> 5 -> 1
#  - Critical point 2 (local minima): 5 -> 1 -> 3