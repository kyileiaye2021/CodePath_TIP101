#unit 4
#session 2
#ver 3
#Prob 4

'''
When putting the ele in the new list, iterate thru the list from the end to beginning
'''
# *Two pointer approach
# * create a list to store the squared ele
# * create two pointers one at index 0 and one at last index
# * iterate over the list from the beginning to end
#    * check if the abs value of left is greater than right 
#        * square it and increment left by 1
#    * otherwise
#        * square it and decrement right by 1
#    * put that var in the new list at the curr position 

def sorted_squares(nums):
  squared_lst = [0] * len(nums)
  left, right = 0, len(nums) - 1
  for i in range(len(nums)-1, -1, -1):
    if abs(nums[left]) > abs(nums[right]):
      square = nums[left] ** 2
      left += 1
    else:
      square = nums[right] ** 2
      right -= 1
    squared_lst[i] = square
  return squared_lst

nums = [1,2,3,4]
sq_nums = sorted_squares(nums)
print(sq_nums)
nums2 = [-4,-1,0,3,10]
sq_nums2 = sorted_squares(nums2)
print(sq_nums2)



