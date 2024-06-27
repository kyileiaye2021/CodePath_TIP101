#unit 4
#session 1
#ver 1
#prob 2

#Two pointer approach (don't need to create a new list)
#create two pointers 
# make for loop until a pass b
#   swap two pointers var 
#    move a to right by 1
#    move b to left by 1
#return original lst

def reverse_list(lst):
  l = 0 
  r = len(lst) - 1
  while l < r:
    temp = lst[l]
    lst[l] = lst[r]
    lst[r] = temp
    l += 1
    r -= 1
  return lst
lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))
lst = []
print(reverse_list(lst))
#Time complexity - O(n) 
#Space complexity - O(1)
