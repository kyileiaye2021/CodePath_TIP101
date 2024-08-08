#unit 10
#session 1
#ver 1
#prob 4

'''
In dict, we can't use immutable containers such as dict or lst as key
Hashmap
* using tuple as key in hashmap
* using lst as value in hashmap
'''
# Example #1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Expeced Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example #2:
# Input: strs = [""]
# Expected Output: [[""]]

# Example #3:
# Input: strs = ["a"]
# Expected Output: [["a"]]

# Hashmap approach
# main_dict = {{the char in each word}: [words that are made up of chars in its corresponding key]}
# iterate over the list
#   create a new dict to store each char and its freq
#   for each iteration, 
#      create a list
#      append each char of curr word into the lst
#      sort the list (important because tuple needs to be in order)
#      conver the list to tuple
#   check if the tuple is in the main_dict
#     put the curr word to the value list of the main_dict
#   put the tuple key in the dict and create a list with that curr word
# create a res_lst
# iterate over the values of main_dict 
#   put each value lst of main_dict to the res_list
# return that res_lst

def group_anagrams(strs):
  main_dict = {}

  for word in strs:
    char_lst = []

    for char in word:
      char_lst.append(char)

    char_tuple = tuple(sorted(char_lst))

    if char_tuple not in main_dict:
      main_dict[char_tuple] = [word]
    else:
      main_dict[char_tuple].append(word)

  res_lst = []

  for val_lst in main_dict.values():
    res_lst.append(val_lst)

  return res_lst

strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs)) # [["bat"],["nat","tan"],["ate","eat","tea"]]

strs = [""]
print(group_anagrams(strs)) # [['']]

strs = ["a"]
print(group_anagrams(strs)) # [["a"]]



