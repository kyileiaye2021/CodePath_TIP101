#unit 4
#session 1
# ver 2
#prob 5

# Assumption
# There will or will not be vowels in the str
# Str can be empty
# Str cannot be null
# case must be insensitive

# High Level Planning
# * Two pointer approach
# * create a lst using str. iteraate over the lst and swap the two pointers if they point to vowels

# Low Level Planning
# create a list using str
# create a vowel str
# create two pointers
# iterate over the lst until l passes r
  # check l var is vowel
    # check r var is vowel
      # swap l and r var
    # shift the r to left by 1
  # shift the l to right by 1
# return the joined list


def reverse_vowels(s):
  char_lst = list(s.lower())
  vowels = 'aeiou'
  l, r = 0, len(s) - 1

  while l < r:
    if char_lst[l] in vowels:
      if char_lst[r] in vowels:
        temp = char_lst[l]
        char_lst[l] = char_lst[r]
        char_lst[r] = temp
      r -= 1
    else:
      l += 1
  return ''.join(char_lst)

s1 = "hello"
rev_s1 = reverse_vowels(s1)
print(rev_s1)

s2 = "leetcode"
rev_s2 = reverse_vowels(s2)
print(rev_s2)