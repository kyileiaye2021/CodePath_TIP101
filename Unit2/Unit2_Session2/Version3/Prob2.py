#unit 2
#Session 2
#ver 3
#prob 2


def dict_difference(d1, d2):
  unique_dict = {}
  for key in d1:
    if key not in d2:
      unique_dict[key] = d1[key]
    else:
      if d1[key] != d2[key]:
        unique_dict[key] = d1[key]
  return unique_dict

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 2, 'd': 1}
print(dict_difference(d1, d2))