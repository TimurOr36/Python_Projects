import random

emojis = {
  "r": "🪨",
  "p": "📄",
  "s": "✂️"
}
choices = ("r", "p", "s")

while True:
  user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
  if user_choice not in choices:
    print("Invalid choice!")
    continue

  computer_choice = random.choice(choices)

  print(f"Your choice is {emojis[user_choice]}")
  print(f"Computer's choice is {emojis[computer_choice]}")

  if user_choice == computer_choice:
    print("It's a tie!")
  elif ((user_choice == "r" and computer_choice == "s") or
        (user_choice == "p" and computer_choice == "r") or
        (user_choice == "s" and computer_choice == "p")):
    print("You win!")
  else:
    print("You lose!")
    
  play_again = input("Do you want to play again? (y/n): ").lower()
  if play_again == "n":
    break