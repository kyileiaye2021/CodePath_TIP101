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
      start = i + 1
  return partition_lst

s1 = "ababcbacadefegdehijhklij"
print(partition_label(s1))

s2 = "abcabcbadefffeda"
print(partition_label(s2))