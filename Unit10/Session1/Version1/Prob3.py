#unit 10
#session 1
#version 1
#prob 3

# two pointer 
# create a pointer to maintain the head_a to keep track of the merged list
# create a pointer pointing to the head of head_a
# create another pointer pointing to the head of head_b
# iterate until head_a pointer reaches its end and head_b pointer reaches its end
#   append the head_a pointer node to merged_list pointer
#   move head_a pointer to next node
#   append the head_b pointer node to merged_list pointer
#   move head_b pointer to next node
#   move the merge_list pointer to next node
# while there are nodes to iterate in head_a 
#   append those nodes into merged list
# while there are nodes to iterate in head_b
#   append those nodes into merged list

class linked_lst:
  def __init__(self, val, next=None) -> None:
    self.val = val
    self.next = next

def shuffle_merge(head_a, head_b):
  merged_lst = linked_lst(0)
  temp_lst = merged_lst

  #head_a_pointer = head_a
  #head_b_pointer = head_b

  while head_a and head_b:
    temp_lst.next = head_a
    head_a = head_a.next
    temp_lst = temp_lst.next

    temp_lst.next = head_b
    head_b = head_b.next
    temp_lst = temp_lst.next

  while head_a:
    temp_lst.next = head_a
    head_a = head_a.next
    temp_lst = temp_lst.next

  while head_b:
    temp_lst.next = head_b
    head_b = head_b.next
    temp_lst = temp_lst.next

  return merged_lst.next

def print_ll(root):
  while root.next:
    print(f"{root.val} -> ",end="")
    root = root.next

  print(root.val)

# Input Lists: List 1: 1 —> 2 —> 3, List 2: 4 —> 5 —> 6
# Input: head_a = 1, head_b = 4
# Expected Return value: 1
# Expected Result List: 1 —> 4 —> 2 —> 5 —> 3 —> 6

# Input Lists: List 1: 1 —> 2 —> 3, List 2: 4
# Expected Return value: 1
# Expected Result List: 1 —> 4 —> 2 —> 3

head_a = linked_lst(1, linked_lst(2, linked_lst(3)))
head_b = linked_lst(4, linked_lst(5, linked_lst(6)))
print_ll(shuffle_merge(head_a, head_b)) #1 —> 4 —> 2 —> 5 —> 3 —> 6

head_c = head_a = linked_lst(1, linked_lst(2, linked_lst(3)))
head_d = linked_lst(4)
print_ll(shuffle_merge(head_c, head_d)) #1 —> 4 —> 2 —> 3

# time complexity - O(n)
# space complexity - O(1)