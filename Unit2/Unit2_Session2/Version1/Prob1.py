#unit 2
#session 2
#ver 1
#prob 1


#if the str is already in the key of the dict, update the value
#else, add the key-val pair in the dict

def cast_vote(votes, candidate):
  if candidate in votes:
    votes[candidate] += 1
  else:
    votes[candidate] = 1
  return votes

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)