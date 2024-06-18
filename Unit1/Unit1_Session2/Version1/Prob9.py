#Unit 1
#Session 2
#ver 1
#Problem 9

#create a func with an integer as a param
#crate a new list 
#if the passed integer as an argument is divisible by the currnt ele in the list, put it in the new list
#return the new list

def find_divisors(n):
  new_list = []
  #the nums should be checked from 0 to n
  for ele in range(1,n+1): #we have to set the start num as 1 because n % 0 would cause a compiler error
    if (n % ele) == 0:
      new_list.append(ele)

  return new_list

lst = find_divisors(6)
print(lst)