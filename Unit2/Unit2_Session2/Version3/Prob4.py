#unit 2
#session 2
#ver 3
#prob 4

'''
KEY TAKEAWAYS
1. the value of the dictionaries can be list
2. To append the ele in the list of the value in the dict, dict[key].append()
3. To add the key_val pair, dict[key] = [value]
'''
#create a dict for frequency map
#iterate over the list and fill the frequency map
#create a dict to store the result {frequency : [elements]}
#iterate over the frequency map
def group_by_frequency(lst):
  frequency_map = {}
  for ele in lst:
    if ele not in frequency_map:
      frequency_map[ele] = 1
    else:
      frequency_map[ele] += 1

  result_dict = {}

  for key in frequency_map:

    if frequency_map[key] in result_dict:
      result_dict[frequency_map[key]].append(key)
    else:
      result_dict[frequency_map[key]] = [key]

  return result_dict


lst = ['a', 'b', 'c', 'd', 'd', 'c', 'e', 'e', 'e']
print(group_by_frequency(lst))