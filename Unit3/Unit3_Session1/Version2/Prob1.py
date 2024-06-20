#unit 3
#session 1
#ver 2
#prob 1

def match_made(dictionary):
  for key, value in dictionary.items():
    print( f"{key} and {value} are a perfect match.")

dict = {'Penut butter': 'Jelly', 'Spongebob': 'Patrick', 'Ash':'Pikachu'}
match_made(dict)