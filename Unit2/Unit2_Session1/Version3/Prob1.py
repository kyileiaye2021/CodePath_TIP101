#unit 2
#session 1
#ver 3
#prob 1

#compare the first and sec ele of the lst to determine the lst is increasing or decreasing
#create a var to keep track of the prev's index
#iterate over the lst 

#if the lst is increasing and the curr ele < prev ele, return the prev's index
#if the lst is decreasing and the curr ele > prev ele, return the prev's index

def peak_index_in_mountain_list(lst):
  if lst[0] < lst[1]:
    increasing = True
  else:
    increasing = False

  peak_index = 0
  for i in range(1,len(lst)):
    if (increasing and lst[i] < lst[i-1])  or (not increasing and lst[i] > lst[i-1]):
      peak_index = i - 1

  return peak_index


mountain_lst = [0,3,8,0]
peak = peak_index_in_mountain_list(mountain_lst)
print(peak)