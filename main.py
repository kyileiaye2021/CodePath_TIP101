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
