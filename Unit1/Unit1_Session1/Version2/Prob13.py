#unit 1
#session 1 ver 2
#Problem 13

#create a func with a list param and return a list 
#the returned list elements are doubled to the original list

def squares(nums):
  res = []
  for i in nums:
    res.append(i*i)

  return res

lst = squares([1,2,3,4])
print (lst)

