#unit 1
#session 2
#ver 2
#problem 4

#create a func with a int list and a var as a para
#iterate over the ele in the list 
#check if the target var is in list
#return true if it's
#return false if it's not

def check_num(lst, num):
  for i in lst:
    if i == num:
      return True

  return False

lst = [5,2,3,9,10]
flag1 = check_num(lst,9)
flag2 = check_num(lst,4)
print(flag1)
print(flag2)