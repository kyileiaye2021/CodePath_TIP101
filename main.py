def reverse_only_letters(s):
  letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  char_lst = list(s)
  l, r = 0, len(char_lst) - 1

  while l < r:
    if char_lst[l] in letters:
      if char_lst[r] in letters:
        temp = char_lst[l]
        char_lst[l] = char_lst[r]
        char_lst[r] = temp
      r -= 1
    l += 1
  return "".join(char_lst)
  
s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)