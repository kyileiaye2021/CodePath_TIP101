#unit 4
#session 2
#version 3
#prob 3

# Two pointer approach
# create two pointers to point s and t last index
def get_next_valid_index(string, index):
  backspace = 0
  while index >= 0:
    if string[index] == '#':
      backspace += 1
    elif backspace > 0:
      backspace -= 1
    else:
      break
    index -= 1
  return index
  
def backspace_compare(s, t):
  i, j = len(s) -1, len(t) - 1
  while i >= 0 and j >= 0:
    i = get_next_valid_index(s, i)
    j = get_next_valid_index(t, j)

    if i >= 0 and j >= 0 and s[i] != s[j]:
      return False

    i -= 1
    j -= 1
    
  return True

s = "ab#c"
t = "ad#c"
print(backspace_compare(s, t))

m = "ab##"
n = "c#d#"
print(backspace_compare(m, n))

a = "a#c"
b = "b"
print(backspace_compare(a, b))
