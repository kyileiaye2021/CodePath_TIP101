#Unit 1
#Session 2
#Ver 1
#Problem 8

#create a func
#use range func to iterate over the nums from 1 to 100 
#check if the current ele in lst is divisible by 5
#prints out if it is

def multiples_of_five():
  for i in range(1, 101):
    if i % 5 == 0: 
      print(i)


multiples_of_five()