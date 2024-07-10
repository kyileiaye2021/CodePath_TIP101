#unit 2
#session 1
#ver 1
#prob 2
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def count_element(head, val):
  current = head
  freq_count = 0
  if current is None: 
    return None
  while current: 
    if current.value == val:
      freq_count += 1
    current = current.next
  return freq_count    

# Input List: 3 -> 1 -> 2 -> 1
# Input: head = 3, val = 1
head = Node(3, Node(1, Node(2, Node(1))))
freq = count_element(head, 1)
print(freq)
