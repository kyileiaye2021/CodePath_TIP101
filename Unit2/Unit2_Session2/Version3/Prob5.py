#unit 2
#session 2
#ver 3
#prob 5

#create a map {ele : index}
#iterate over the list
#in each iteration,
  #if the ele already in the map, update the index value
  #else, add the ele in the map
#create a list
#iterate over the dict sorted by itsvalue
  #append the key value into the list


def remove_duplicates_from_front(nums):
  map = {}
  for i in range(len(nums)):
    map[nums[i]] = i
    '''
    if nums[i] in map:
      map[nums[i]] = i
    else:
      map[nums[i]] = i'''

  res_lst = []

  #sorting the dict by its value
  #sorted() func returns a list of key_value tuples
  sorted_map_by_value = dict(sorted(map.items(), key=lambda item: item[1]))

  for key in sorted_map_by_value:
    res_lst.append(key)
  return res_lst
  
nums = [6,5,3,5,2,8,3]
print(remove_duplicates_from_front(nums))

'''
Alternate way

1) Create an empty list to store unique numbers
2) Starting at the END of the nums list:
  a) If the number is not already in unique,
     insert it at the beginning of unique
3) Return the unique nums

def remove_duplicates_from_front(nums):
  unique_nums = []
  for i in range(len(nums)-1, -1, -1):
      if nums[i] not in unique_nums:
          unique_nums.insert(0, nums[i])
  return unique_nums

'''