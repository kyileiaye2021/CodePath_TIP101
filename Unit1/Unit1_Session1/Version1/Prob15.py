#print_negatives()
#a func with a list and prints neg num in the list(elements in the list are int type)
#iterate over a list and if the current element is less than 0, print it out
#if there is no neg num, print None
#a bool var to detect whehter there are neg num or not

def print_negatives(lst):
  neg_in_list = False
  for i in lst:
    if i < 0:
      print(i)
      neg_in_list = True

  if not neg_in_list:
    print("None")

print_negatives([3,-2,2,1,-5])
print_negatives([1,2,3,4,5])
