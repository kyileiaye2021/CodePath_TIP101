#unit 2
#session 2
#ver 2
#prob 6

#sort the list firsst
#create a dict to store value and smaller number count
#iterate over the sorted list
#fill the dict like {val: index}
#create a list
#iterate over the nums
#check each item is in the dict
#if it's, put it in the list

def smallerNumbersThanCurrent(nums):
  sorted_nums = sorted(nums)
  temp_dict = {}

  for i in range(len(sorted_nums)):
    if sorted_nums[i] not in temp_dict:
      temp_dict[sorted_nums[i]] = i 
    else:#same key in the list #the array is sorted so the prev item = the curr item
      temp_dict[sorted_nums[i]] = i - 1

  smaller_count_lst = []
  for n in nums:
    if n in temp_dict:
      smaller_count_lst.append(temp_dict[n])

  return smaller_count_lst

nums = [6,1,2,2,3]
ans = smallerNumbersThanCurrent(nums)
print(ans)
# ans == [4,0,1,1,3]