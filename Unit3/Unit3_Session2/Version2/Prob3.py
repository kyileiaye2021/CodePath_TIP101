#unit 3
#session 2
#ver 2
#prob 3

#get the smallest str in the list
#iterate over that smallest str
  #iterate over the other str in the list
    #compare each char of other str and smallest str
    #if it's a mismatch, return the smallest_str starting from first char up until the current char


def longest_common_prefix(strings):

  if not strings:
    return ""
  smallest_str = strings[0]

  for word in strings:
    if len(word) < len(smallest_str):
      smallest_str = word

  for i, char in enumerate(smallest_str):
    for other in strings:
      if char != other[i]:
        return smallest_str[:i]


strings = ["flower", "flow", "flight"]
common_string = longest_common_prefix(strings)
print(common_string)

strs = ["dog", "racecar", "car"]
common_str = longest_common_prefix(strs)
print(common_str)