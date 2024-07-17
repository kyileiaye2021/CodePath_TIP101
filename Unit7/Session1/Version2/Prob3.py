#Unit 7
#session 1
#ver 2
#prob 3

'''
Base case is important.
In this case, lst become empty or none at some point so we have 
to check lst is none or not as base case
'''
def list_product(lst):
  if not lst:
    return 1
  return (lst[0] * list_product(lst[1:]))

lst = [1,2,3,4,5]
print(list_product(lst))
# Example Input: [1, 2, 3, 4, 5]
# Expected Output: 120
# Explanation: 1 * 2 * 3 * 4 * 5 = 120