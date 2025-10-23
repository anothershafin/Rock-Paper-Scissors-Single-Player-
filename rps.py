import random

def play_round(rounds):
  emojis={"r":"🪨", "p": "📜", "s":"✂️"}
  moves=("r","p","s")
  p_score=0
  c_score=0
  for i in range(rounds):
    print("-"*20)
    print(f"Round-{i+1}:")
    print("-"*20)
    c_move=random.choice(moves)
    while True:
      p_move=input("Rock! Paper! Scissors? (r/p/s) or q to quit:").strip().lower()
      if (p_move in moves) or (p_move=="q"):
        break
      else:
        print("Enter valid move (r, p, or s) or q to quit.")

    if p_move=="q":
      return p_score, c_score, i


    print(f"You chose:{emojis[p_move]}\nComputer Chose:{emojis[c_move]}")
    if c_move==p_move:
      print("Tied!")
    elif(
        (p_move=="r" and c_move=="s") or 
        (p_move=="p" and c_move=="r") or
        (p_move=="s" and c_move=="p") 
    ):
      print("You Won!")
      p_score+=1
    else:
      print("You Lost!")
      c_score+=1
  return p_score, c_score, i



def game_start():
  while True:
    try:
      rounds=int(input("How many rounds do want to play?:"))
      if rounds>0:
        break
    except ValueError:
      print("Invalid Number. Enter a positive integer.")
  
  status=True
  while status:
    p_score, c_score, played=play_round(rounds)

    if played==0:
      game_end()
      return None

    print("-"*20)
    print(f"Results:")
    print("-"*20)
    print(f"You have played {played+1} rounds.\nWon {p_score} times.\nLost {c_score} times")
    tie=(played+1)-(p_score+c_score)
    if tie!=0:
      print(f"Tied {tie} times.")
    print(f"Your score: {p_score}\nComputers Score: {c_score}")
    if p_score>c_score:
      print("You are the Winner🏆!")
    elif p_score<c_score:
      print("Computer is the Winner!\nBetter Luck Next time!")
    else:
      print(f"The Game is Entirely Tied!")


    while True:
      out=input("Do you want to play again? (y/n):").strip().lower()
      if out=="y":
        break
      elif out=="n":
        status=False
        break
      else:
        print("Enter valid input y or n.")
  print("Thank you for Playing!🎊")




def game_end():
  print("Thank you for your time!")


print("Welcome to Rock Paper Scissors!")
print("="*40)
while True:
  start=input("Start the game?(y/n)").strip().lower()
  if start=="y":
    game_start()
    break
  elif start=="n":
    game_end()
    break
  else:
    print("Enter a Valid Input y or n.")
