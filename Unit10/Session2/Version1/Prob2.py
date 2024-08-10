# unit 10
# session 2
#ver 1
#prob 2: Remove Element

# Input: nums = [3,2,2,3], val = 3

# Two pointer 
# First pointer and sec pointer (both will point to 0 at first)

'''
1. create variable k (starts at 0)
2. iterate through nums (variable i)
3. if statement to detwermine if nums[i] != val 
4. if so, we reassign nums[i] with k
5. increment k
6. return k

Time complexity - O(n)
Space complexity - O(1)
'''

def remove_element(nums, val):
  k = 0
  for i in range(len(nums)):
    if nums[i] != val:
      nums[k] = nums[i]
      k+=1
  #return 
  return k


nums = [3,2,2,3]
val = 3
print(remove_element(nums, val)) # 2

nums = [0,1,2,2,3,0,4,2]
val = 2
print(remove_element(nums,val)) #5
