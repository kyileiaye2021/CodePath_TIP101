#unit 2
#session 2
#ver 2
#probl 1

#itereate over the dict
#if the name is in the dict, update the score
#if not, add the name and score

def update_score(scores, players, points):
  if players in scores:
    scores[players] += points
  else:
    scores[players] = points

  return scores

scores = {"Alice": 100, "Bob": 90}
update_score(scores, "Alice", 10)
print(scores)
update_score(scores, "Calvin", 20)
print(scores)
update_score(scores, "Calvin", 5)
print(scores)