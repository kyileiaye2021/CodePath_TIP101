def is_long_pressed(name, typed):
  if len(name) > len(typed):
    return False
  i = 0
  j = 0

  while j < len(typed):
    if name[i] != typed[j]:
      if typed[j] != typed[j-1]:
        return False
    else:
      i += 1

    j += 1
  return True

name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))


