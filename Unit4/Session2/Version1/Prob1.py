#unit 4
#session 2
#ver 2
#prob 1

# Assumption
# the str cannot be empty or null
# the length of the string may or may not be the same
# the str can have repetitive char 
# every char in the name

# High Level planning
# * Iterative Approach
#   * iterate over the name and for each char in name, iterate over the typed and check the curr ele is in the type
# * Frequency Map Approach
#   * create a map for the typed. iterate over the name and check if the curr char is in typed or not and update the frequency
# * Two Pointer Approach
#   * create two pointers one pointing to the index 0 of name and another to iterate over the typed.
#   * compare the two pointer vars are matched. If they are not matched and the curr typed char is the same as it's previous
#     one, move the pointer of typed to another char in typed

# Low level planning
# * Two pointer approach
#   * return False if the len of name is greater than the len of typed
#   * create a two pointer representing two indices of the two str
#   * iterate over the loop until the typed pointer var ends the end of the typed 
#      * compare the current i index name var and j index typed var
#      * if they are not matched, check the curr j index typed var with the prev one in typed 
#      * if they are equal, increment j by 1
#      * otherwise, return False
#   * return True

def is_long_pressed(name, typed):
  if len(name) > len(typed):
    return False
  i = 0
  j = 0

  while j < len(typed):
    if name[i] != typed[j]:
      if typed[j] != typed[j-1]:
        return False
    else:
      i += 1
      
    j += 1
  return True
  
name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))

