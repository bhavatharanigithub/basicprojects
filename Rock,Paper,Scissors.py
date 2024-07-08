import random
you_wins=0
computer_wins=0
options=["rock","paper","scissors"]
while True:
  choice=input("Just pick anyone:ROCK/PAPER/SCISSORS.WHEN YOU ARE DECIDE TO QUIT PLEASE ENTER q ").lower()
  if choice=="q":
     break
  if choice not in options:
    print("PLEASE ENRER AS I TOLD")
    continue
  computer_choice=random.randint(0,2)
  computer_pick=options[computer_choice]
  print("computer picks",computer_pick,".")
  if choice=="rock" and computer_pick=="scissors":
    print("you won")
    you_wins+=1
  elif choice=="scissors" and computer_pick=="paper":
    print("you won")
    you_wins+=1
  elif choice=="paper" and computer_pick=="rock":
    print("you won")
    you_wins+=1
  else:
    print("you lost")
    computer_wins+=1
print("YOU WINS",you_wins,"TIMES")
print("COMPUTER WINS",computer_wins,"TIMES")
