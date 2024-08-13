#Unit 10
#session 2
#ver 2
#prob 2

'''Happy Case'''
# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# Output: [2]

'''Edge CAse'''
# INput: nums1 = [1,3,4], nums2 = [2,5,8]
# Output: []

# Input: nums1= [], and nums2 = []
# Output: []

# Dictionary Approach
# create a list to store the intersection nums
# createa a dict for a list
# iterate over another list 
#   check if the curr char in the dict
#     check if the char is not already in the list
#        add it to the lst
def intersection(nums1, nums2):
  intersection_lst = []
  dict = {}

  for ele in nums1:
    if ele not in dict:
      dict[ele] = 1

    else:
      dict[ele] += 1

  for ele in nums2:
    if ele in dict and ele not in intersection_lst:
        intersection_lst.append(ele)

  return intersection_lst

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2)) #[2]

nums1 = [1,3,4]
nums2 = [2,5,8]
print(intersection(nums1, nums2)) #[]

nums1 = []
nums2 = []
print(intersection(nums1, nums2)) #[]

# time complexity - O(n)
# space complexity - O(m)