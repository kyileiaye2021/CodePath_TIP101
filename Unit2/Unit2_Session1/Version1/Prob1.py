#unit 2
#session 1
#ver 1
#problem 1

#check the current ele in the sequence list isn't in lst 
#if it's, return false

def is_subsequence(lst, sequence):
  for ele in sequence:
    if ele not in lst:
      return False
  return True

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))