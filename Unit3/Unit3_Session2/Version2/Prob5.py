#unit 3
#session 2
#ver 2
#prob 5


#create a map {ele : lastest index}
#iterate over the str s to fill the map

#create partition list
#create start and end initialized to 0
#iterate over the str
  #assign the largest index of the ele up until the current ele - lastest index in the partition list
  #if curr index == largest lastest index in the partition:
    #add the num of the ele upto that lastest index to the partition list
    #move the start pointer to the next index of the partition list lastest index
#return partition list

def partition_label(s):
  lastest_index = {}
  for i in range(len(s)):
    lastest_index[s[i]] = i

  partition_lst = []
  start, end = 0,0
  for i, char in enumerate(s):
    end = max(end, lastest_index[char])
    if i == end:
      partition_lst.append(end - start + 1)
      start = i+1
  return partition_lst

s1 = "ababcbacadefegdehijhklij"
print(partition_label(s1))

s2 = "abcabcbadefffeda"
print(partition_label(s2))