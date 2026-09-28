import random

emojis = {
  "r": "🪨",
  "p": "📄",
  "s": "✂️"
}
choices = tuple(emojis.keys())
computer_wins = 0
user_wins = 0

while True:
  choose_rounds = int(input("How many rounds do you want to play (1-10)? "))
  if choose_rounds < 1 or choose_rounds > 10:
    print("Invalid number of rounds! Please choose between 1 and 10.")
    continue

  while choose_rounds > 0:
    user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
    if user_choice not in choices:
      print("Invalid choice!")
      continue

    computer_choice = random.choice(choices)

    print(f"Your choice is {emojis[user_choice]}")
    print(f"Computer's choice is {emojis[computer_choice]}")

    if user_choice == computer_choice:
      choose_rounds -= 1
      print(f"It's a tie! You have {choose_rounds} rounds left.")
      print(f"Current Score - You: {user_wins}, Computer: {computer_wins}")
    elif ((user_choice == "r" and computer_choice == "s") or
          (user_choice == "p" and computer_choice == "r") or
          (user_choice == "s" and computer_choice == "p")):
      user_wins += 1
      choose_rounds -= 1
      print(f"You win! You have {choose_rounds} rounds left.")
      print(f"Current Score - You: {user_wins}, Computer: {computer_wins}")
    else:
      choose_rounds -= 1
      computer_wins += 1
      print(f"You lose! You have {choose_rounds} rounds left.")
      print(f"Current Score - You: {user_wins}, Computer: {computer_wins}")

    if choose_rounds == 0:
      print(f"Game Over! Final Score - You: {user_wins}, Computer: {computer_wins}")
      if user_wins > computer_wins:
        print("Congratulations! You won the game!")
      elif user_wins < computer_wins:
        print("Sorry! The computer won the game!")
      else:
        print("It's a tie game!")
      break
    
  play_again = input("Do you want to play again? (y/n): ").lower()
  if play_again == "n":
    break