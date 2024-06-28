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