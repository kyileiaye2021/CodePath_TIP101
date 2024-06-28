#unit 4
#session 1
#ver 3
#prob 6

# Assumption
# The str cannot be empty or null
# The str can have more than one repetitive char

# High Level Planning
# * Iterative Approach
#     * Everytime, we see the repetiitve char, delete the char
# * Two Pointer Approach
#     * one pointer iterate thru the str. another pointer points to unique ele index. dele the remaining char starting from
#       unique ele

# Low Level Planning
# create a list
# create unique_index pointer
# iterate over the list
#    if the unique ele is found
#       assign that elel in the index where unique_index currently points to
#       increment unique_index by 1
# delete the ele starting from unique_index
# return the joined list

def squash_spaces(s):
  char_lst = list(s)
  unique_index = 0
  for i in range(0, len(char_lst)):
    if (char_lst[i] != ' '):
      char_lst[unique_index] = char_lst[i]
      unique_index += 1

    else:
      if i != 0 and char_lst[i - 1] != ' ':
        char_lst[unique_index] = char_lst[i]
        unique_index += 1

  del char_lst[unique_index:]
  return "".join(char_lst)

print(squash_spaces("  hello    world  "))
print(squash_spaces("  what  about  this    ?"))
print(squash_spaces("this is my sentence"))