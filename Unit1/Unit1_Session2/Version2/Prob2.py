#unit1
#session2
#ver 2
#problem 2

#create a func with an integer list
#iterate over each ele in the list to sum up the total sum
#count the num of ele 
#create a var initialized to 0
#update that var in each iteration
#after the loop, divide the total sum by the var count
#return the avg

def average(scores):
  total = 0
  count = 0
  for ele in scores:
    total += ele
    count += 1

  return (total / count)


scores = [84,73,92,95,88]
avg_score = average(scores)
print(avg_score)