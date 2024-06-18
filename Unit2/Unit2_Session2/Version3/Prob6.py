#unit 2
#session 2
#ver 3
#prob 6

#create a index dict {ele: index}
#create an occurence dict {ele: occurence}
#iterate over the list
  #if the ele is already in the list, update the occurence
  #else, add the ele to the dict with 1 occurence | add the index to the dict
#iterate over the dict
  #if the occurence isn't 1, return the index of the key
#If no duplicates, return None


def find_min_index_of_repeating(nums):
  index_dict = {}
  occurence_dict = {}
  for i in range(len(nums)):
    if nums[i] in occurence_dict:
      occurence_dict[nums[i]] += 1

    else:
      occurence_dict[nums[i]] = 1
      index_dict[nums[i]] = i

  for key in occurence_dict:
    if occurence_dict[key] != 1:
      return index_dict[key]
    
  return None
  
nums = [5, 6, 3, 4, 3, 6, 4]
nums2 = [5, 6, 3, 4]
nums3 = [ 5, 6, 2, 4, 3, 4, 3]
print(find_min_index_of_repeating(nums))
print(find_min_index_of_repeating(nums2))
print(find_min_index_of_repeating(nums3))