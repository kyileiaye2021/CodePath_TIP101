
def sum_of_unique_elements(lst1, lst2):
  if not lst1 and not lst2:
    return 0
  if len(lst1) == 0:
    return 0
  sum = 0
  frequency = {}

  for ele in lst1:
    if ele in frequency:
      frequency[ele] += 1
    else:
      frequency[ele] = 1

  for key in frequency:
    if frequency[key] == 1 and key not in lst2:
      sum += key

  return sum

'''
lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]
lstD = []

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1) #3

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2) #0

sum3 = sum_of_unique_elements(lstD, lstC)
print(sum3) #0

sum4 = sum_of_unique_elements(lstB, lstD)
print(sum4) #18

'''
lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]
lstD = []
lstE = None 
lstF = None
lstG = []
lstH = [1,2,3,4]
lstI = [1,2,2,3]
lstJ = [1,2,5,6]


sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1) #3

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2)#0

sum4 = sum_of_unique_elements(lstE, lstF)
print(sum4) #0

sum6  = sum_of_unique_elements(lstD, lstG)
print(sum6) #0

sum3 = sum_of_unique_elements(lstD, lstC)
print(sum3) #0

sum5 = sum_of_unique_elements(lstC, lstD)
print(sum5) #0

sum7 = sum_of_unique_elements(lstA, lstH)
print(sum7) #0

sum8 = sum_of_unique_elements(lstI, lstC)
print(sum8) #4

sum9 = sum_of_unique_elements(lstA, lstJ)
print(sum9) #7