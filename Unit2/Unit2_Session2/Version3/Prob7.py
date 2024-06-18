#unit 2
#session 2
#ver 3
#prob 7

#create a map {ele : index}
#create a list
#iterate over the nums list
  #diff = target - curr_ele
  #check if the diff is already in the map
    #if it's, put the value of the dict's key in the list
    #put the current index in the list 
    #return that list (Should be in the if condition since we only need the pair of indices one time)
  #else: 
    #fill the map with the curr ele
def two_sum(nums, target):
  map = {}
  result_list = []
    
  for i in range(len(nums)):
    diff = target - nums[i]
    if diff in map:
      result_list.append(map[diff])
      result_list.append(i)
      return result_list
    map[nums[i]] = i

nums = [2,7,11,15]
q_1 = two_sum(nums,9)
q_2 = two_sum(nums,18)

nums2 = [3,3]
q_3 = two_sum(nums2,6)

print(q_1)
print(q_2)
print(q_3)
