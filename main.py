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