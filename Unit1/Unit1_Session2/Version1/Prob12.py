#unit 1
#session 2
#ver 1
#problem 12

#create a func with a list and a value as params
#iterate over each ele in the list to look for that value in the list
#if found, return the index of the ele in the list
#if not, return -1

def linear_search(lst, target):
  for i in range(len(lst)):
    if lst[i] == target:
      return i

  return -1

lst = [1,4,5,2,8]
position = linear_search(lst,5)
print(position)

lst = [1,4,5,2,8]
position = linear_search(lst,10)
print(position)
