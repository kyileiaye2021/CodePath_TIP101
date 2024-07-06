#unit 5
#session 2
#ver 1
#prob 6

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def listify_first_n(head, n):
  lst = []
  curr_node = head
  while n > 0 and curr_node:
    lst.append(curr_node.value)
    curr_node = curr_node.next
    n -= 1
  return lst

# linked list: a -> b -> c
c = Node('c')
b = Node('b',c)
a = Node('a',b)

head = a
lst = listify_first_n(head,2)
print(lst)

# linked list: j -> k -> l 
l = Node('l')
k = Node('k', l)
j = Node('j', k)
head2 = j
lst2 = listify_first_n(head2,5)
print(lst2)

'''
Example output:
[`a`, `b`]
[`j`, `k`, `l`]
'''