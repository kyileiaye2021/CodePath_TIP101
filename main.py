def reverse_only_letters(s):
  char_lst = list(s)
  right = len(char_lst) - 1
  i = 0

  while i < right:

    if char_lst[i].isalpha():

      if char_lst[right].isalpha():
        temp = char_lst[i]
        char_lst[i] = char_lst[right]
        char_lst[right] = temp

      right -= 1
    i += 1

  s = ''.join(char_lst)
  return s

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)
