#unit 1
#session 1 ver 2
#problem 7

#arrange the lines of code in order
#dividing the elements of the list by 2

'''
result = []
b. for number in lst:
c. result.append(halved)
d. halved = number/2
e. halve_list([2,4,6,8])
f. return result
g. def halve_lst(lst):
'''

def halve_lst(lst):
  result = []

  for number in lst:
    halved = number / 2
    result.append(halved)

  return result

print(halve_lst([2,4,6,8]))
