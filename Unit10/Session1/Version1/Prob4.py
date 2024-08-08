#unit 10
#session 1
#ver 1
#prob 4

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
#      if the char is not in the freq dict
#         put the char in the freq dict
#      else:
#         increment the char freq by 1
#   check if the freq dict is in the main_dict
#     put the curr word to the value list of the main_dict
#   put the freq dict key in the dict and create a list with that curr word
# create a res_lst
# iterate over the values of main_dict 
#   put each value lst of main_dict to the res_list
# return that res_lst

def group_anagrams(strs):
  main_dict = {}

  for word in strs:
    freq_dict = {}
    
    for char in word:
      if char not in freq_dict:
        freq_dict[char] = 1
      else:
        freq_dict[char] += 1

    if freq_dict not in main_dict:
      main_dict[freq_dict] = [word]
    else:
      main_dict[freq_dict].append(word)

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



