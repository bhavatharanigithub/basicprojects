import random
num1=int(input("Enter a range within that we just start : "))
random_number=random.randint(0,num1)
guesses=0
while True:
  guesses += 1
  guess_a_number=int(input("Make your guess: "))

  if random_number==guess_a_number:
    print("you won")
    break
  else:
    if(guess_a_number>random_number):
      print("YOUR GUESS IS HIGH")
    else:
      print("YOUR GUESS IS LOW")
print("You won in",guesses,'Guesses', "IT\'S GOOD:)")