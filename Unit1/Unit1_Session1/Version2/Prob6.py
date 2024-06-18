
#Unit 1
#Session 1 Ver 2
#param: string
#prints out who wins

def rock_paper_scissors(player1, player2):
  match player1:

    case "rock":
      if player2 == "scissor":
        print("player1 wins")
      elif player2 == "paper":
        print("player2 wins")
      else:
        print("It's a tie.")

    case "scissors":
      if player2 == "paper":
        print("player1 wins")
      elif player2 == "rock":
        print("player2 wins")
      else:
        print("It's a tie.")


    case "paper":
      if player2 == "rock":
        print("player1 wins")
      elif player2 == "scissor":
        print("player2 wins")
      else:
        print("It's a tie.")

    case _:
      print("None")

rock_paper_scissors("rock", "rock")
rock_paper_scissors("scissors", "rock")
rock_paper_scissors("scissors", "paper")
rock_paper_scissors("rock", "paper")
rock_paper_scissors("paper", "rock")


