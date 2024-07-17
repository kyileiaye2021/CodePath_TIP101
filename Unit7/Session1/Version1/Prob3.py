#unit 7
#session 1
#ver 1
#prob 3

# Time complexity: O(N)
# Space complexity: O(N) 
def sum_list(lst):
  # base case:
  if not lst: #if the list is empty, return 0
    return 0
  # recursive case:
  else:
    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4, 5]))