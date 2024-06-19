#unit 3
#session 1
#ver 1
#prob 5

#we need to return the first index of the non-repetitive char
#create a frequency map {ele : frequency}
#iterate over the str
  #if char in frequency map
    #increment the frequency by 1
  #else
    #add the key_val in the frequency map
#iterate over the dict
  #check the value of the curr key is 1
    #return the key

def first_unique_char(my_str):
  dict = {}
  for letter in my_str:
    if letter in dict:
      dict[letter] += 1
    else:
      dict[letter] = 1

  for letter in range(len(my_str)):
    if dict[my_str[letter]] == 1:
      return letter

  return -1

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))