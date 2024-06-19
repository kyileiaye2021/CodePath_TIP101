#Unit 3
#session 1
#ver 3
#prob 5

'''
If we found a duplicate is found, we can ignore the chars upto the first index of the duplicated char
So, the start_index of the longest substr re-begins at the index after the first index of the duplicated char
Keep track of the max_length (i - start + 1)
'''

#create a var to keep track of the max_length of the substr
#crate a var to maintain the start index of the substr
#create a dict {char: index} #need to do because we need to update the start var 
#iterate over s str
  #if curr char is already in the dict
    #update the start index
  #else:
    #update the max_length 
  #add the curr char in the dict


def length_of_longest_substring(s):
  max_length = 0
  start_index = 0
  index_dict = {}

  for i, char in enumerate(s):
    if char in index_dict:
      start_index = index_dict[char] + 1 
    else:
      max_length = max(max_length, i - start_index + 1)
    index_dict[char] = i

  return max_length

s = "abcdeefghhhhh"
count = length_of_longest_substring(s)
print(count)

s2 = "aaaaaaaaaaaaaaa"
count = length_of_longest_substring(s2)
print(count)
