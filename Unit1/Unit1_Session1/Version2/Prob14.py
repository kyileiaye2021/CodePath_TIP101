#unit1
#session 1 ver 2
#Problem 14

#create a func with a list and integer as params
#return a list that includes the elements of the orig list multiplied by the integer para
#create a list to store the var and return
#use for loop to iterate over the lst and multiply every element with the multiplier

def multiply_list(lst, multiplier):
  res = []
  for i in lst:
    res.append(i * multiplier)

  return res

lst = [1,2,3]
new_lst = multiply_list(lst, 3)
print(new_lst)