#unit 6
#session 1
#ver 3
#prob 2

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def frequency_map(head):
  freq_map = {}
  curr_head = head
  while curr_head:
    if curr_head.value in freq_map:
      freq_map[curr_head.value] += 1
    else:
      freq_map[curr_head.value] = 1
    curr_head = curr_head.next
  return freq_map

head = Node(1, Node(2, Node(3, Node(4, Node(2, Node(3))))))
print(frequency_map(head))

# Input List: 1 -> 2 -> 3 -> 4 -> 2 -> 3
# Input: head = 1
# Expected Output: { 1: 1, 2: 2, 3: 2, 4: 1}