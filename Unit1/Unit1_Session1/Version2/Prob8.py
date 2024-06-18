#unit 1
#session 1 ver 2
#create a func with a list and an int type var params
#returns a list from the func
#use for loop to iterate over the given list
#append the elements only greater than the threshold num

def above_threshold(lst, threshold):
  res = []
  for element in lst:
    if element > threshold:
      res.append(element)

  return res

lst = [8,2,13,11,4,10,14]
new_lst = above_threshold(lst, 10)
print(new_lst)