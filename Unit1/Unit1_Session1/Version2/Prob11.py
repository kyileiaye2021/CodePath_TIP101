#unit 1
#session 1 ver 2
#Problem 11

#a func with a list as a para
#return the length of the list without a built-in func

def list_length(lst):
  length = 0
  for ele in lst:
    length += 1

  return length


lst = [2,4,6,8,10]
length = list_length(lst)
print(length)
