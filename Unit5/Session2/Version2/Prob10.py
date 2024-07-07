#unit 5
#session 2
#ver 2
#prob 10

class SLLNode:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next

class DLLNode:
  def __init__(self, value, next = None, prev = None):
    self.value = value
    self.next = next
    self.prev = prev

def dll_to_sll(dll_head):
  #getting last node of double linked list
  curr_node = dll_head
  while curr_node.next:
    curr_node = curr_node.next 
  #At this stage, the curr_node pointer will point to the last item in doubly linked list

  #create a singly linked list by iterating over the doubly linked list in reverse
  sll_node = SLLNode(curr_node.value)
  while curr_node.prev:
    if not curr_node.next:
      sll_node = SLLNode(curr_node.value)
    else:
      sll_node = SLLNode(curr_node.value, curr_node.next)
    curr_node = curr_node.prev
  sll_node = SLLNode(curr_node.value, curr_node.next) #the iteration will stop at the first node, so create a node for that node

  while sll_node:
    if sll_node.next:
      print(f"{sll_node.value} -> ", end='')
    else:
      print(sll_node.value)
    sll_node = sll_node.next
   
Ice = DLLNode('Ice')
Water = DLLNode('Water')
Steam = DLLNode('Steam')
Ice.next = Water
Water.next = Steam
Water.prev = Ice
Steam.prev = Water

dll_head = Ice
sll_head = dll_to_sll(dll_head)

'''
# DLL: Ice <-> Water <-> Steam
dll_head = Ice
sll_head = dll_to_sll(dll_head)

#SLL: Ice -> Water -> Steam
'''