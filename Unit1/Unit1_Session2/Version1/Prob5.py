#Unit1 
#Session2
#Ver 1
#Problem 5

#create a func with the list as a param
#return the max difference between the largest and smallest val in the list
#firstly, set the first ele of the lst as both smallest and largest ele in the list
#update smallest and largeest var in each iteration
#return largest - smallest

def max_difference(lst):
  #initialize largest and smallest ele as the first ele of the lst
  largest = lst[0]
  smallest = lst[0]

  for ele in lst:
    #use two if statements because we have to check for both largest and smallest vars in each iteration
    #if-else and if-elif can only check either of one of the var
    if ele > largest:
      largest = ele

    if ele < smallest:
      smallest = ele

  return largest - smallest


lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)