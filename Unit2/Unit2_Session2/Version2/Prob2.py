#unit 2
#session 2
#ver 2
#prob 2

def dict_intersection(d1, d2):
  common_dict = {}
  for key in d1:
    if key in d2 and d1[key] == d2[key]:
      common_dict[key] = d2[key]

  return common_dict

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 4}
print(dict_intersection(d1,d2))