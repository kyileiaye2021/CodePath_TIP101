#unit 2
#sessioin 1
#ver 3
#prob 7

#create a score_dict for keeping track of total score of each team
#create a occurence_dict to keep track of how many times the team occurs in the list
#iterate over the list
#if the team is already in the dicts, update the score and add 1 to occurence
#if it's not, add the team, score, and 1 to occurence

#create a var for keeping track of highest_avg_score
#create a var for the team that has highest_avg_score
#iterate over the score dict
#find the avg of the current score 
#check if the current avg is greater than highest_avg_score
#update the highest_avg_score if it's 
#return the highest_avg_score

def team_with_best_average_score(games):
    score_dict = {}
    occurence_dict = {}
    for game in games:
        if game["team_name"] in score_dict:
            score_dict[game["team_name"]] += game["score"]
            occurence_dict[game["team_name"]] += 1

        else:
            score_dict[game["team_name"]] = game["score"]
            occurence_dict[game["team_name"]] = 1

    highest_avg_score = 0
    best_team = ""
    for score in score_dict:
        curr_avg = score_dict[score] / occurence_dict[score]
        if curr_avg > highest_avg_score:
            highest_avg_score = curr_avg
            best_team = score

    return best_team

games = [{
    "team_name": "Lions",
    "score": 23
}, {
    "team_name": "Tigers",
    "score": 30
}, {
    "team_name": "Lions",
    "score": 27
}, {
    "team_name": "Bears",
    "score": 20
}, {
    "team_name": "Tigers",
    "score": 24
}, {
    "team_name": "Bears",
    "score": 22
}]

print(team_with_best_average_score(games))
