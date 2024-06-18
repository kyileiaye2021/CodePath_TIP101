#unit 1
#session 1 ver 2
#problem 15

#a func with a list as a parameter
#return the integer (the num of even elements in the list)
#for loop to find the even integer
#num % 2 =0
# a variable to store the num of even nums

def count_evens(lst):
  even_num_count = 0
  for i in lst:
    if i % 2 == 0:
      even_num_count += 1

  return even_num_count

lst1 = [1,5,7,9]
count1 = count_evens(lst1)
print(count1)

lst2 = [2,4,6,8]
count2 = count_evens(lst2)
print(count2)