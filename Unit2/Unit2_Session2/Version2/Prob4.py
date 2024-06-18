#unit 2
#session 2
#ver 2
#probl 4

#create a dict {value, occurence}
#iterate over the list and fill the dict
#create a list
#iterate over the dict
#check the curr item's val is even or not
#add the odd value item in the lst
#return the list

def find_odd_occurrences(nums):
  occurence_dict = {}
  for n in nums:
    if n in occurence_dict:
      occurence_dict[n] += 1
    else:
      occurence_dict[n] = 1

  unique_key_lst = []
  for key in occurence_dict:
    if occurence_dict[key] % 2 != 0:
      unique_key_lst.append(key)

  return unique_key_lst

nums = [1,4,2,3,2,3,3,4,4,4]
odd_list = find_odd_occurrences(nums)
print(odd_list)