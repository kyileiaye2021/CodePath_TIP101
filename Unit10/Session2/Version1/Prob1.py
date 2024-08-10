#unit 10
#session 2
#ver 1
#Problem 1: Contains Duplicates

# Example #1: 
# Input: nums = [1,2,3,1]
# Output: True

# Example #2:
# Input: nums = [1,2,3,4]
# Output: False

# Example #3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: True

'''

array of nums ->  return true if a value appeart twice and false if all values or unique 

Match -> Traverse and dictonary/set

Plan -> 
#Define empty set
#while i in nums iterate and append values into the set
#If value in set: 
return false
    --> Pass

#Return True

Time complexity - O(n)
Space complexity - O(n)

'''

def contains_duplicate(nums):
  unique_ele = set()
  for i in range(len(nums)): 
    if nums[i] in unique_ele:
      return True

    else:
      unique_ele.add(nums[i])

  return False

nums = [1,2,3,1]
print(contains_duplicate(nums)) # true

nums = [1,2,3,4]
print(contains_duplicate(nums)) # false

nums = [1,1,1,3,3,4,3,2,4,2]
print(contains_duplicate(nums)) # true
